from collections import Counter


def conta_elemento_lista(lista_alunos):
    """Retorna o aluno com maior ocorrência na lista.

    Em caso de empate, retorna o primeiro nome em ordem alfabética.
    Retorna ``None`` quando a lista está vazia.
    """
    if not lista_alunos:
        return None

    contagens = Counter(lista_alunos)
    maior_ocorrencia = max(contagens.values())
    alunos_empatados = [nome for nome, qtd in contagens.items() if qtd == maior_ocorrencia]
    return sorted(alunos_empatados)[0]


def main():
    lista_alunos = []

    while True:
        nome = input("Digite o nome do aluno (ou 'fim' para encerrar): ").strip()
        if nome.lower() == "fim":
            break
        if nome:
            lista_alunos.append(nome)

    aluno_mais_participativo = conta_elemento_lista(lista_alunos)

    if aluno_mais_participativo is None:
        print("Nenhum aluno informado.")
    else:
        print(f"O aluno com maior ocorrência é: {aluno_mais_participativo}")


if __name__ == "__main__":
    main()
