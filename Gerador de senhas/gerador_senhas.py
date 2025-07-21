import random
import string

# Função para gerar uma senha aleatória com critérios específicos (comprimento, uso de maiúsculas, minúsculas, números e símbolos)

def gerar_senha(comprimento, usar_maiusculo=True, usar_minusculo=True, usar_numeros=True, usar_simbolos=True):

    caracteres = ''
    if usar_maiusculo:
        caracteres += string.ascii_uppercase
    if usar_minusculo:
        caracteres += string.ascii_lowercase
    if usar_numeros:
        caracteres += string.digits
    if usar_simbolos:
        caracteres += string.punctuation

    if not caracteres:
        return "Erro: Nenhuma opção de caractere foi selecionada para gerar a senha."
    
    senha = ''.join(random.choice(caracteres) for i in range(comprimento))
    return senha

if __name__ == "__main__":
    print("Gerador de senhas")

    # Entrada do comprimento da senha
    while True:
        try:
            comprimento_str = input("Digite o comprimento da senha desejada (ex: 8):")
            comprimento = int(comprimento_str)
            if comprimento <= 0:
                print("O comprimento da senha deve ser um número positivo. Tente novamente.")
                continue # Volta para o início do loop
            break # Sai do loop se a entrada for válida
        except ValueError:
            print("Entrada inválida. Por favor, digite um número inteiro para o comprimento. Tente novamente.")
    
    # Escolha das opções de caracteres
    print("\nOpções de caracteres (Selecione 's' para sim ou 'n' para não):")
    usar_maiusculo = input("Usar letras maiúsculas? (s/n): ").lower() == 's'
    usar_minuscula = input("Usar letras minúsculas? (s/n): ").lower() == 's'
    usar_numeros = input("Usar números? (s/n): ").lower() == 's'
    usar_simbolos = input("Usar símbolos? (s/n): ").lower() == 's'

    # Chamada da função para exbir o resultado (gerar a senha)
    minha_senha = gerar_senha(comprimento, usar_maiusculo, usar_minuscula, usar_numeros, usar_simbolos)
    print(f"\nSua senha gerada é: {minha_senha}")
