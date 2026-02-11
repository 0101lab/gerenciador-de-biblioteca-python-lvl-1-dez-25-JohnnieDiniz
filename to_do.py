# ideia principal é criar um gerenciador de tarefas de prioridade, com base o kanban

def to_do():
    alta = []
    médio = []
    baixo = []

    proximo_id = 1
    proximo_id += 1

    print('Sistema de Tarefas')
    print('Cadastro de tarefas')

    prioridade = input('Nível de prioridade (alta/médio/baixo): ').strip().lower()

    tarefa = input('Qual tarefa deseja cadastrar? ')

