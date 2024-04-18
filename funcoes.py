from time import sleep
def adicionar(lista:list):
    #iniciando o dicionario onde ficara os dados da tarefa
    dicionario = {}
    dicionario['tarefa']= str(input("Digite sua tarefa:"))
    while True:
        dicionario['categoria']= str(input("Digite a categoria desta tarefa:[domestica/lazer/]")).lower().strip()
        dicionario['prioridade']= str(input("Qual é a prioridade desta tarefa?[alta/media/baixa]")).lower().strip()#formata o texto que o usuario digitar para minusculo e tira os espacos extras da esquerda e da direita
        if dicionario["categoria"]not in ["domestica","lazer"] and dicionario["prioridade"] not in ["alta","media","baixa"]:
            print("\033[31mDigite valores validos para categoria e prioridade\033[m")
        else:
            print("")
            lista.append(dicionario)
            break
    
    print(".",end='')
    sleep(1)
    print(".",end='')
    sleep(0.5)
    print(".",end='')
    print("\033[32mTarefa adicionada com sucesso\033[m ")
    sleep(3)


def excluir(lista:list):
    tarf = str(input("Qual a tarefa que voce deseja excluir?(Digite somente o nome desta tarefa)"))
    cat = str(input("Digite a categoria desta tarefa"))
    prioridade = str(input("Digite a prioridade desta tarefa "))
    lista.remove({'tarefa':tarf,'categoria':cat,'prioridade':prioridade})


def listar(lista:list):
    while True:
        try:
            opcao = int(input('''
Voce deseja filtrar sua listagem por ;
1-Categoria 
2-prioridade
3-nenhuma
''')
)
            if opcao > 3:
                raise ValueError("Digite um valor valido")
        except:
            return '\033[31mAtenção valor invalido!!!\033[m' 
        sleep(3)

        if opcao == 1:
            cat = str(input("Por qual categoria?[domestica/lazer]"))
            print("=="*30)
            print(f"Filtrando tarefas pela categoria:{cat}")
            print("=="*30)
            sleep(2)
            for item in lista:
                for chave,valor in item.items(): 
                    if item['categoria'] == cat:
                        print(f"{chave}:{valor}")
                print('=='*30)
            sleep(2)
            return ''#finaliza minha chamada da funcao e evita o None retornando no terminal 

        if opcao == 2:
            prio = str(input("Por qual prioridade?[alta/media/baixa]"))
            print("=="*30)
            print(f"Filtrando tarefas por prioridade:{prio}")
            print("=="*30)
            sleep(2)
            for item in lista:
                for chave,valor in item.items(): 
                    if item['prioridade'] == prio:
                        print(f"{chave}:{valor}")
                print('=='*30)
            sleep(2)
            return ''


        if opcao == 3:
            for item in lista:
                for chave,valor in item.items():
                    print(f"{chave}:{valor}")
                print('=='*30)
            return ''#para evitar o None retornando no terminal 
            


if __name__ == '__main__':
    listinha = [{'tarefa':'correr','categoria':'lazer','prioridade':'alta'},{'tarefa':'varrer','categoria':'domestica','prioridade':'alta'},{'tarefa':'ler','categoria':'lazer','prioridade':'media'},{'tarefa':'estudar','categoria':'lazer','prioridade':'alta'}]
    excluir(listinha)
    print(listar(listinha))




