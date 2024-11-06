livros = {
    '1': 'O Grande Gatsby',
    '2': 'A República',
    '3': 'O Príncipe',
    '4': 'Madame Bovary',
    '5': 'Rei Lear'
}

livro_escolhido = input("◾ Escolha um livro para contagem de letras (1 - O Grande Gatsby, 2 - A República, 3 - O Príncipe, 4 - Madame Bovary, 5 - Rei Lear): ")

if livro_escolhido in livros:
    livro = livros[livro_escolhido]
    contagem = {}
    print(133 * "-")

    for letra in livro:
        if letra.isalpha():  # Verifica se é uma letra
            contagem[letra] = contagem.get(letra, 0) + 1

    print(f'◾ Contagem de letras em "{livro}":')
    print(40 * "-")
    for letra, quantidade in sorted(contagem.items()):
        print(f"{letra}: {quantidade}")

    total_letras = sum(contagem.values())
    print(40 * "-")
    print(f"◾ Total de letras: {total_letras}")
else:
    print("Livro não encontrado. Por favor, escolha um número válido.")
