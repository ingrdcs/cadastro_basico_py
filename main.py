aluno_nome=[] 
aluno_email=[]
aluno_curso=[]
todos =[aluno_nome,aluno_email, aluno_curso]


def menu():
    print("Menu\n[1]Cadastrar novo aluno\n[2]Lista de alunos cadastrados\n[3]Buscar aluno\n[4]Remover Aluno\n[5]Atualizar o nome do Aluno\n[6]Salvar Arquivo\n[0]Sair ")
    opt= int(input("Escolha uma opção:"))
    return opt

def add():
    aluno=str(input("Digite o nome do Aluno:"))
    if aluno in aluno_nome:
        print("O Aluno já consta na lista!")
    else:

        aluno_nome.append(aluno)
        curso=str(input("Digite o curso:"))
        email=str(input("Digite o email:"))
        aluno_curso.append(curso)
        aluno_email.append(email)
        print("Aluno cadastrado com sucesso!\n\n")

    pass
    menu()

def ver_tudo():
    print("Alunos Cadastrados:\n")
    print(todos)
    pass
   


def pesquisa():
    aluno=str(input("Digite o nome do aluno:"))
    if aluno in aluno_nome:
        print(aluno_nome)
    else:
        print("O nome não se encontra na lista. Tente novamente!")
    pass 


def remover():
    aluno=str(input("Digite o nome do aluno:"))
    if aluno in aluno_nome:
        aluno_nome.remove(aluno)
        print("Aluno removido com sucesso!")

    else:
        print("Aluno não encontrado. Tente novamente!")

    pass


def edit():
    aluno=str(input("Digite o nome do Aluno que deseja alterar:"))
    if aluno in aluno_nome:
        aluno_nome.remove(aluno)
        aluno=str(input("Digite o nome do novo aluno"))
        aluno_nome.append(aluno)
        ask=str(input("Deseja alterar Curso e Email Também? [S/N]"))
        if ask == "Ss":
            curso=str(input("Digite o nome do curso que deseja alterar:"))
            aluno_curso.remove(curso)
            curso=str(input("Digite o nome do novo curso:"))
            aluno_curso.append(curso)
            email=str(input("Digite o email que deseja alterar:"))
            aluno_email.remove(email)
            email=str(input("Digite um novo email"))
            aluno_email.append(email)
            print("Alterações feitas com sucesso")
        else:
            print("Nome alterado com sucesso!")

           
def salvar():
    save=str(input("Deseja salvar arquivo? [S/N]"))
    if save == "Ss":
        arquivoName=str(input("Digite o nome do arquivo:"))
        for i in arquivoName:
            arquivo=open(arquivoName,"w")
            arquivo.write(str(i))
        arquivo.close()
    else:
        print("Obrigado por utilizar nosso sistema!")

    pass


opcao = menu()
while True:
    if opcao == 1:
        add()
    elif opcao == 2:
        ver_tudo()
    elif opcao == 3:
        pesquisa()
    elif opcao == 4:
        remover()
    elif opcao == 5:
        edit()
    elif opcao == 6:
        salvar()

    elif opcao == 0:
        print("Obrigado por utilizar um de nossos serviços.")
    break