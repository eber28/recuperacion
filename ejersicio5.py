#ejercisio de suma
lista=[1,4,3,6,8,7,5,36]
def sumaa(lista):
    total=0
    for numero in lista:
        total += numero
    return total
print(sum(lista))

# ejercicio de multiplicar

def multiplicar(lista):
    resultado=1
    for num in lista:
        resultado*= num
    return resultado
print(multiplicar(lista))
