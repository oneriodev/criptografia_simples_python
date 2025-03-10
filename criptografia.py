# Biblioteca para criptografar o arquivo
import fitz
from cryptography.fernet import Fernet

# Gerar chave de criptografia 
key = Fernet.generate_key()
cipher = Fernet(key)

# Realizar a leitura do arquivo
pdf_path = "documento.pdf"
pdf = fitz.open(pdf_path)

# Extrai somento o texto do pdf
pdf_text = ""
for page in pdf:
    pdf_text += page.get_text()

pdf.close()

# Comando para criptografar
texto_cifrado = cipher.encrypt(pdf_text.encode())

# Realiza o salavn[mento do arquivo criptografado
with open("documento_encriptado.txt", "wb") as file:
    file.write(texto_cifrado)

with open("chave.key", "wb") as key_file:
    key_file.write(key)

print("Pdf criptogafado.")

# Baixar e visualizar o arquivo
from google.colab import files
files.download("documento_encriptado.txt")
files.download("chave.key")