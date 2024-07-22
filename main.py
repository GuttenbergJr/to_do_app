tarefas = []

def inserir_tarefa():
    tarefa = input('Digite sua tarefa: ')
    tarefas.append(tarefa)
    print('Tarefa adicionada com sucesso!')

def verificar_tarefas():
    if len(tarefas) == 0:
        print('Nenhuma tarefa foi adicionada ainda. Por favor, adicione uma.')
    else:
        print('Lista de tarefas pendentes')
        for i,tarefa in enumerate(tarefas, start=1):
            print(f'[{i}] - {tarefa}')

def deletar_tarefa():
    verificar_tarefas()
    if tarefas:
        try:
            numTarefa = int(input('Digite o número da tarefa que quer deletar: ')) - 1
            if 0 <= numTarefa < len(tarefas):
                tarefas.pop(numTarefa)
                print('Tarefa deletada com sucesso!')
            else:
                print("Número da tarefa inválido.")
        except:
            print('Por favor, digite um número válido.')



if __name__ == '__main__':
    while True:
        print('\n')
        print('Lista de afazeres')
        print('Por favor, escolha uma opção abaixo:')
        print('====================================')
        print('[1] - Adicionar nova tarefa')
        print('[2] - Verificar tarefas pendentes')
        print('[3] - Deletar uma tarefa')
        print('[0] - Encerrar Programa')
        print('====================================')

        
        try:
            escolha = int(input('Digite um número -> '))
        except:
            print('Por favor, digite um número válido.')
        
        if escolha == 1:
            inserir_tarefa()
        elif escolha == 2:
            verificar_tarefas()
        elif escolha == 3:
            deletar_tarefa()
        elif escolha == 0:
            break
        else:
            print('Por favor, digite um número válido..')