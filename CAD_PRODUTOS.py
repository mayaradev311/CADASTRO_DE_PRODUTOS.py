import os

opcao = 0

produto_nome = []
produto_preco = []
produto_qtd = []
produto_codigo = []


while opcao != 4:

    print("------MENU------")   
    print("1 - Cadastrar produtos")
    print("2 - Listar produtos")
    print("3 - Excluir produtos")
    print("4 - Sair do sistema")
    print("5 - Alterar cadastro")
    print("6 - Venda de produto")

    opcao = int(input("Escolha sua opção: "))

    if opcao == 1:

        nome = input("Digite o nome do produto: ")
        produto_nome.append(nome)

        codigo = input("Digite o código do produto: ")
        produto_codigo.append(codigo)

        preco = input("Digite o preço: ")
        produto_preco.append(preco)

        qtd = int(input("Digite a quantidade: "))
        produto_qtd.append(qtd)

        arquivo = open("produto.txt" , "a")
        arquivo.write(f"{nome}, {codigo}, {preco}, {qtd}\n")
        arquivo.close()

        print("Produto cadastrado com sucesso!")
        input("Pressione ENTER para continuar...")
        os.system("cls")



    elif opcao == 2:
        print("-----------PRODUTOS----------")

        arquivo = open("produto.txt","r")

        if len(produto_nome) == 0:
            print("Nenhum produto cadastrado.")
        else:
            for linha in arquivo:
                nome, codigo, preco, qtd = linha.strip().split(",")
                print(f"    Nome: {nome}")
                print(f"    Código: {codigo}")
                print(f"    Preço: {preco}")
                print(f"    Quantidade: {qtd}")
                print("-----------------------------")
            arquivo.close()

        input("Pressione ENTER para continuar...")
        os.system("cls")


    elif opcao == 3:
        print("-----------EXCLUIR PRODUTO----------")

        if len(produto_nome) == 0:
            print("Nenhum usuário para excluir.")
        else:
            for i, nome in enumerate(produto_nome):
                print(f"{i} - {nome}")

            excluir = int(input("Digite o número do produto que deseja excluir: "))

            if excluir >= 0 and excluir < len(produto_nome):
                produto_nome.pop(excluir)
                produto_codigo.pop(excluir)
                produto_preco.pop(excluir)
                produto_qtd.pop(excluir)
                print("Produto removido com sucesso!")
            else:
                print("Número inválido!")

        input("Pressione ENTER para continuar...")
        os.system("cls")


    elif opcao == 5:
        print("-----------ALTERAR PRODUTO----------")

        if len(produto_nome) == 0:
            print("Nenhum usuário cadastrado.")
        else:
            for i, nome in enumerate(produto_nome):
                print(f"{i} - {nome}")

            indice = int(input("Digite o número do usuário que deseja alterar: "))

            if indice >= 0 and indice < len(produto_nome):

                print("O que deseja alterar?")
                print("1 - Nome")
                print("2 - Código")
                print("3 - Preço")
                print("3 - Quantidade")

                escolha = int(input("Escolha: "))

                if escolha == 1:
                    novo_nome = input("Digite o novo nome: ")
                    produto_nome[indice] = novo_nome

                elif escolha == 2:
                    novo_codigo = input("Digite o novo código: ")
                    produto_codigo[indice] = novo_codigo

                elif escolha == 3:
                    novo_preço = input("Digite o novo preço: ")
                    produto_preco[indice] = novo_preço
                elif escolha == 4:
                    novo_qtd = input("Digite a nova quantidade: ")
                    produto_qtd[indice] = novo_qtd
                else:
                    print("Opção inválida!")

                print("Dados atualizados com sucesso!")

            else:
                print("Número inválido!")

        input("Pressione ENTER para continuar...")
        os.system("cls")


    elif opcao == 4:
        print("SISTEMA ENCERRADO")
        break


    if opcao == 6:
        print("----------VENDA-DE-PRODUTOS------------")
        if len(produto_nome) == 0:
            print("Nenhum produto cadastrado")

        else:
            for i, nome in enumerate(produto_nome):
                print(f"Nome: {produto_nome[i]}")
                print(f"Código: {produto_codigo[i]}")
                print(f"Preço: {produto_preco[i]}")
                print(f"Quantidade: {produto_qtd[i]}")


            indice = int(input("Qual produto você deseja vender: "))

            if indice >= 0 and indice < len(produto_nome):
                quantidade = int(input("Qual a quantidade vendida: "))

                if quantidade > produto_qtd[indice]:
                    print("Quantidade indisponível!")

                else:
                    produto_qtd[indice] -= quantidade

                    print("Produto vendido com sucesso!")

            else: 
                print("Produto inválido")

        input("Pressione ENTER para continuar: ")
        os.system("cls")


            
        
