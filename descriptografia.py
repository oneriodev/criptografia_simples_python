# Ler a chave salva
with open("chave.key", "rb") as key_file:
    key = key_file.read()

cipher = Fernet(key)

# Realizar a leitura do arquivo criptografado
with open("documento_encriptado.txt", "rb") as file:
    texto_cifrado = file.read()

# Comando para descriptografar
texto_original = cipher.decrypt(texto_cifrado).decode()

# Cria um novo pdf com o texto original
novo_pdf = fitz.open()
pagina = novo_pdf.new_page()
pagina.insert_text((50, 50), texto_original)

novo_pdf.save("documento_descriptado.pdf")
novo_pdf.close()

print("Pdf descriptografado.")

# Para download e visualização
files.download("documento_descriptado.pdf")