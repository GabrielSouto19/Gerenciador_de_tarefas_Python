import funcoes as fc
lista_tarefas = []

while True:
    print("=-"*30)
    print(f'{"Menu Interativo".center(60)}')
    print("=-"*30)
    try:
        opcao = int(input('''
Digite o numero correspondente ao caminho que deseja seguir 
1->Adicicionar Tarefa
2->Excluir Tarefa
3->Listar Tarefa
4->Finalizar
'''))
    except:
        print("Valor invalido por favor digite um valor valido")
    if opcao == 4:
        break


    if opcao == 1:
        fc.adicionar(lista_tarefas)
        

    if opcao == 2:
        fc.excluir(lista_tarefas)


    if opcao == 3:
        fc.listar(lista_tarefas)

