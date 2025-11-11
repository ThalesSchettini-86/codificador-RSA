# Importações
import time
import math

# Introdução
print(f"\033[34mSeja bem-vindo ao (de)codificador de cifra RSA.")
time.sleep(2)
print("Você gostaria de criptografar ou descriptografar uma mensagem?")
time.sleep(2)
de_cod = int(input("Opções:\n[1] Criptografar\n[2] Descriptografar\n"))
while de_cod != 1 and de_cod != 2:
    print(f"\033[31mInsira uma opção válida!")
    de_cod = int(input(f"\033[34mOpções:\n[1] Criptografar\n[2] Descriptografar\n"))

# Opção 1: Criptografar
if de_cod == 1:
    ascii_list = []
    msg = input(f"\033[0mDigite uma mensagem para ser criptografada: ")
    for letra in msg:
        ascii_list.append(ord(letra))
    # Função para checar se o número escolhido é primo ou não
    def is_prime(num):
        if num <= 1:
            return False
        if num <= 3:
            return True
        if num % 2 == 0 or num % 3 == 0:
            return False
        x = 5
        while x * x <= num:
            if num % x == 0 or num % (x + 2) == 0:
                return False
            x += 6
        return True
    # Criação das chaves P e Q
    p = int(input("Escolha um valor para ser a chave P: "))
    while not is_prime(p) or p < 2:
        p = int(input(f"\033[31mO valor P precisa ser um número primo e positivo! Escolha novamente: "))
    q = int(input(f"\033[0mAgora escolha um valor para ser a chave Q: "))
    while not is_prime(q) or q < 2:
        q = int(input(f"\033[31mO valor Q precisa ser um número primo e positivo! Escolha novamente: "))

   # Cálculo da chave N
    print(f"\033[0mCalculando o valor da chave N.")
    time.sleep(1)
    print("Calculando o valor da chave N..")
    n = p * q
    time.sleep(1)
    print("Calculando o valor da chave N...")
    time.sleep(1)
    print(f"\033[32mSua chave N tem o valor de {n}")
    time.sleep(2)

    # Cálculo da função totiente de N
    print(f"\033[0mCalculando o valor da função totiente de N.")
    time.sleep(1)
    print("Calculando o valor da função totiente de N..")
    fn = (p - 1) * (q - 1)
    time.sleep(1)
    print("Calculando o valor da função totiente de N...")
    time.sleep(1)
    print(f"\033[32mSua função totiente de N tem o valor de {fn}")
    time.sleep(1)

    # Função para determinar os divisores dos números
    def divisores(num):
        divs = []
        x = 1
        while x * x <= num:
            if num % x == 0:
                divs.append(x)
            if x != num // x:
                divs.append(num // x)
            x += 1
        return sorted(divs)

    # Criação da chave E
    e = int(input(f"\033[0mAgora, escolha um valor para e: "))
    divs_e = divisores(e)
    divs_fn = divisores(fn)
    while True:
        if not (1 < e < fn):
            print(f"\033[31mO valor precisa estrar entre 1 e a função totiente de N!")
        elif math.gcd(e, fn) != 1:
            print(f"\033[31mO valor de E e a função totiente de N precisam ser coprimos!")
        else:
            break
        e = int(input(f"\033[0mEscolha novamente um valor para E: "))

    # Cálculo da Inversão Multiplicativa
    print("Calculando o valor da chave I.")
    time.sleep(1)
    i = pow(e, -1, fn)
    print("Calculando o valor da chave I..")
    time.sleep(1)
    print("Calculando o valor da chave I...")
    time.sleep(1)
    print(f"\033[32mSua chave I tem o valor de {i}")
    time.sleep(2)

    #Codificação da mensagem
    print(f"\033[0mCodificando a mensagem.")
    time.sleep(1)
    print("Codificando a mensagem..")
    time.sleep(1)
    print("Codificando a mensagem...")
    time.sleep(1)
    cod = []
    for v in ascii_list:
       C = (v ** e) % n
       cod.append(C)
    msg_cod = " ".join(str(x) for x in cod)
    print(f"\033[32mA mensagem codificada é: {msg_cod}")

# Opção 2: Descriptografar
elif de_cod == 2:
    msg = input(f"\033[0mDigite uma mensagem para ser descriptografada: ")
    cod = [int(x) for x in msg.split()]
    i = int(input("Insira o valor da chave I: "))
    n = int(input("Insira o valor da chave N: "))
    print("Decodificando a mensagem.")
    time.sleep(1)
    print("Decodificando a mensagem..")
    time.sleep(1)
    print("Decodificando a mensagem...")
    time.sleep(1)
    decod = []
    for v in cod:
       M = pow(v, i, n)
       decod.append(M)
    msg_decod = " ".join(chr(x) for x in decod)
    print(f"\033[32mA mensagem decodificada é: {msg_decod}")