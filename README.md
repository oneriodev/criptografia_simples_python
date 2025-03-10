# Criptografia de PDF com Python

Este repositório contém um estudo prático sobre **criptografia de arquivos PDF** utilizando **Python**. O objetivo deste projeto é demonstrar como proteger dados sensíveis, como documentos em PDF, por meio de criptografia e descriptografia.

## Tecnologias Utilizadas

- **Python** 3.x
- **PyMuPDF (fitz)**: Para manipulação de PDFs (extração de texto, criação de novos PDFs).
- **Cryptography**: Biblioteca para criptografia simétrica com Fernet.

## Funcionalidades

- **Criptografia de PDF**: O texto extraído de um arquivo PDF é criptografado e armazenado em um arquivo seguro.
- **Descriptografia de PDF**: O conteúdo criptografado é revertido para seu formato original e gerado um novo arquivo PDF com o conteúdo restaurado.

## Como Usar

### Pré-requisitos

Antes de rodar os scripts, é necessário instalar as bibliotecas necessárias. Execute o seguinte comando no terminal:

```bash
pip install pymupdf cryptography
