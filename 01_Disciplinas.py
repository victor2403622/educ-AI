import streamlit as st
import pandas as pd
import os

# Define o caminho para o arquivo de dados de disciplinas
DATA_DIR = "data"
SUBJECTS_FILE = os.path.join(DATA_DIR, "subjects.csv")


def ensure_data_file_exists():
    """Cria o diretório de dados e o arquivo subjects.csv se não existirem."""
    if not os.path.exists(DATA_DIR):
        os.makedirs(DATA_DIR)
    if not os.path.exists(SUBJECTS_FILE):
        pd.DataFrame(columns=["nome_disciplina", "descricao"]).to_csv(
            SUBJECTS_FILE, index=False
        )


def load_subjects():
    """Carrega as disciplinas do arquivo CSV."""
    ensure_data_file_exists()
    return pd.read_csv(SUBJECTS_FILE)


st.set_page_config(page_title="Disciplinas", page_icon="📚")

st.title("📚 Gerenciar Disciplinas")

subjects_df = load_subjects()

st.header("Disciplinas Atuais")
if subjects_df.empty:
    st.info("Nenhuma disciplina foi adicionada ainda.")
else:
    st.dataframe(subjects_df, use_container_width=True)

st.header("Adicionar Nova Disciplina")
with st.form("add_subject_form", clear_on_submit=True):
    subject_name = st.text_input("Nome da Disciplina")
    subject_description = st.text_area("Descrição (Opcional)")
    submitted = st.form_submit_button("Adicionar Disciplina")

    if submitted:
        if not subject_name:
            st.error("O nome da disciplina não pode estar vazio.")
        elif subject_name in subjects_df["nome_disciplina"].values:
            st.warning(f"A disciplina '{subject_name}' já existe.")
        else:
            new_subject = pd.DataFrame([{"nome_disciplina": subject_name, "descricao": subject_description}])
            updated_subjects = pd.concat([subjects_df, new_subject], ignore_index=True)
            updated_subjects.to_csv(SUBJECTS_FILE, index=False)
            st.success(f"Disciplina adicionada com sucesso: {subject_name}")
            st.rerun()