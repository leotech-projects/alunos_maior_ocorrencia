from alunos_maior_ocorrencia import conta_elemento_lista


def test_lista_vazia_retorna_none():
    assert conta_elemento_lista([]) is None


def test_maior_ocorrencia_sem_empate():
    dados = ["Ana", "Bia", "Ana", "Carlos", "Ana"]
    assert conta_elemento_lista(dados) == "Ana"


def test_empate_retorna_primeiro_alfabetico():
    dados = ["Carlos", "Bia", "Carlos", "Bia"]
    assert conta_elemento_lista(dados) == "Bia"
