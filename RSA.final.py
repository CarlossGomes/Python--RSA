__authors__ = "Carlos Daniel Almeida Gomes e Welder Paulo da Silva"

import random
from math import gcd

s = input("Digite algo:")
txt = [ord(x) for x in s]
list_e = []
crypto = []
decrypt = []
pq = []
qq = []

# Range de numero
num = 100

for i in range(num):
    prim = gcd(i, num)
    if (i > 1) and (i < num) and (prim == 1):
        pq.append(i)
P = random.choice(pq)

for i in pq:
    if i > P:
        qq.append(i)
Q = random.choice(qq)

# P e Q chaves privadas escolhidas pelo usuario sendo P e Q numeros primos
# P = 17
# Q = 41

# N chave publica gerada atraves das chaves privadas P e Q
N = P * Q

# Definiçao phiN
phiN = (P - 1) * (Q - 1)

# Chave publica E
for i in range(phiN):
    prim = gcd(i, phiN)
    if (i > 1) and (i < phiN) and (prim == 1):
        list_e.append(i)
E = random.choice(list_e)

# Definicao chave privada D, fazendo calculo inverso modular
D = pow(E, phiN - 1, phiN)

# Criptografar msg
for i in txt:
    C = (i ** E) % N
    crypto.append(C)
print(crypto)

# Print valor criptografado
print(''.join(chr(i) for i in crypto))

# Decriptografar msg
for i in crypto:
    C = (i ** D) % N
    decrypt.append(C)
print(decrypt)

# Print valor descriptografado
print(''.join(chr(i) for i in decrypt))

print(E)
print(P, Q)
