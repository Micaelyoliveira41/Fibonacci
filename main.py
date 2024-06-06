'''Crie um programa onde o usuário informa o número de sequências de Fibonacci a ser calculada.

#Usuário informa o número
def fibonacci(n):
    sequencia = [0,1]
    while len(sequencia) <n:
        número = sequencia[-1] + sequencia [-2]
        sequencia.append(número)
        return número
    n = 10
   
    
#programa principal
n = int(input('Informe um número inteiro: '))

print(f'Fibonacci de {n}: {fibonacci(n)}.')'''

#função para calcular fibonacci
def calcular_fibonacci(n):
    if n <= 1:
        return n
    else:
        return calcular_fibonacci(n-1) + calcular_fibonacci(n-2)
    
#programa principal
n = int(input('Informe um número de sequências inteiro: '))

#exibe o resultado do fatorial
for x in range(n):
    print(calcular_fibonacci(x))