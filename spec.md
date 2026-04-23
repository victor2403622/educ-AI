---
name: subjects-schema
version: "1.0"
---

# Especificação: Esquema da Tabela 'subjects'

## 1. Visão Geral

Esta especificação define o esquema para a tabela `subjects` no Xano. A tabela armazenará informações sobre as disciplinas acadêmicas.

## 2. Esquema da Tabela

**Nome da Tabela:** `subjects`

- **id**: `integer` (auto-incremento, chave primária)
- **name**: `text` (nome da disciplina)
- **teacher**: `text` (nome do professor)
- **hours**: `integer` (carga horária da disciplina)
- **user_id**: `integer` (chave estrangeira para a tabela `user` do Xano)