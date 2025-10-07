def converte(numeroEmRomano):
    if numeroEmRomano is None:
        raise ValueError("Entrada não pode ser None")
    numeroEmRomano = numeroEmRomano.strip().upper()

    tabela = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    acumulador = 0
    ultimovizinhodireita = 0
    # percorre da direita para a esquerda
    for i in range(len(numeroEmRomano) - 1, -1, -1):
        atual = tabela.get(numeroEmRomano[i], 0)
        multiplicador = -1 if atual < ultimovizinhodireita else 1
        acumulador += atual * multiplicador
        ultimovizinhodireita = atual

    return acumulador
