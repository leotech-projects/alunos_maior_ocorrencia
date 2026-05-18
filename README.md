# alunos_maior_ocorrencia

Projeto em Python para identificar **o nome de aluno que mais aparece** em uma lista.

A lógica principal está na função `conta_elemento_lista`, que:

- recebe uma lista de nomes;
- conta quantas vezes cada nome aparece;
- retorna o nome com maior frequência;
- em caso de empate, retorna o **primeiro em ordem alfabética**;
- retorna `None` se a lista estiver vazia.

---

## Como o código funciona

Arquivo principal: `alunos_maior_ocorrencia.py`.

### 1) Contagem dos nomes

A função usa `Counter` (da biblioteca padrão `collections`) para gerar um dicionário de frequências.

Exemplo:

```python
Counter(["Ana", "Bia", "Ana"])  # {'Ana': 2, 'Bia': 1}
```

### 2) Descoberta da maior ocorrência

Depois de contar, o código busca o maior valor de frequência com `max(contagens.values())`.

### 3) Tratamento de empate

Se mais de um nome tiver a mesma maior ocorrência, o código:

1. filtra os empatados;
2. ordena alfabeticamente (`sorted`);
3. retorna o primeiro da lista ordenada.

Assim o critério de desempate é previsível e determinístico.

### 4) Fluxo interativo (`main`)

Ao executar o script:

1. o programa solicita nomes no terminal;
2. você pode informar vários nomes (um por linha);
3. ao digitar `fim`, a entrada é encerrada;
4. o resultado é exibido na tela.

Também há uma proteção para ignorar entradas vazias.

---

## Exemplo de uso (terminal)

```bash
$ python alunos_maior_ocorrencia.py
Digite o nome do aluno (ou 'fim' para encerrar): Ana
Digite o nome do aluno (ou 'fim' para encerrar): Bia
Digite o nome do aluno (ou 'fim' para encerrar): Ana
Digite o nome do aluno (ou 'fim' para encerrar): fim
O aluno com maior ocorrência é: Ana
```

---

## Como executar

Pré-requisito: Python 3 instalado.

```bash
python alunos_maior_ocorrencia.py
```

---

## Testes

Os testes automatizados estão no arquivo `test_alunos_maior_ocorrencia.py` e cobrem:

- lista vazia (`None`);
- maior ocorrência sem empate;
- empate com desempate alfabético.

Execute:

```bash
pytest -q
```

---

## Estrutura do projeto

```text
.
├── alunos_maior_ocorrencia.py
├── test_alunos_maior_ocorrencia.py
└── README.md
```
