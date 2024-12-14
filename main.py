from chave_pix import cria_chave_pix, edita_chave_pix, deleta_chave_pix, gera_qr_code_pix
from dados_pessoais import cria_dado_pessoal, edita_dado_pessoal, deleta_dado_pessoal, gera_qr_code_dados_pessoais
from endereco import cria_endereco, edita_endereco, deleta_endereco, gera_qr_code_endereco
from telefones import cria_telefone, edita_telefone, deleta_telefone, gera_qr_code_telefone

def menu_principal():
    funcoes = [cria_chave_pix, edita_chave_pix, deleta_chave_pix, gera_qr_code_pix,
               cria_dado_pessoal, edita_dado_pessoal, deleta_dado_pessoal, gera_qr_code_dados_pessoais,
               cria_endereco, edita_endereco, deleta_endereco, gera_qr_code_endereco,cria_telefone, edita_telefone, deleta_telefone, gera_qr_code_telefone]
    
    while True:
        opcao = int(input("Selecione uma opção (0 para sair): "))
        
        if opcao == 0:
            print("Tchau")
            break
        elif 1 <= opcao <= 12:
            funcoes[opcao - 1]()  
        else:
            print("Opção inválida.")

menu_principal()
