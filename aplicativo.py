import os

#restaurantes = ["KFC","Pizza Hut"]

restaurantes = [{"nome": "Cantina toscana" , "categoria": "Italiana", "ativo": True},
                {"nome": "Sushi da Praça", "categoria": "Japonesa", "ativo": False},
                {"nome": "Churrascaria Gaúcha", "categoria": "Brasileira", "ativo": True},
                {"nome": "Padaria Pão Doce", "categoria": "Francesa", "ativo": True}]



def exibir_nome_do_programa():
    print(""" BOB'S """)
    print("")

def menu():
    print('\n1. Cadastrar Restaurante')
    print('2. Listar Restaurante')
    print('3. Ativar Restaurante')
    print('4. Sair')
   
def finalizar_app():
    print("\nFinalizando ...")
 
def opcao_invalida():
    #print("\nDesculpe!Não temos essa opção em nosso sistema.\n")
    input("Digite enter para voltar ao menu principal")  
    main()
   
def cadastrar_restaurante():
    print("\nCadastre-se: ")
    os.system("cls")
    nome_restaurante = input("Qual o nome do seu restaurante? ")
    categoria_restaurante = input("Qual a categoria do seu restaurante: ")
    dados_do_restaurante = {"nome": nome_restaurante, 'categoria': categoria_restaurante, "ativo" : False }
    restaurantes.append(dados_do_restaurante)
    
    print(f"\nO {nome_restaurante} foi cadastrado com sucesso!")
    input("Digite enter para voltar ao menu principal")  
    main()
   
def listar_restaurantes():
    print(f"\nAqui está a lista de restaurantes q estão cadastrados em nosso sistema: ")
    for restaurante in restaurantes:
        
        nome_restaurante = restaurante["nome"]
        categoria_restaurante = restaurante["categoria"]
        ativo_restaurante = restaurante["ativo"]
        print(f"--", nome_restaurante)
        print(f"categoria:", categoria_restaurante, "\n")
        print(f"--", ativo_restaurante,)
    input("Digite enter para voltar ao menu principal")  
    main()

def escolher_opção():
    try:
        opcao = int(input("\nEscolha uma opção: "))
               
        if(opcao == 1):
           cadastrar_restaurante()

        elif(opcao == 2):
            listar_restaurantes()
               
        elif(opcao == 3):
            print("Ativar restaurante")
               
        elif(opcao == 4):
            finalizar_app()
           
        else:
            opcao_invalida()
           
    except:
        opcao_invalida()

   
def main():
    os.system('cls')
    exibir_nome_do_programa()
    menu()
    escolher_opção()
   
if __name__ == '__main__':
    main()