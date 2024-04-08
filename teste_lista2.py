lista = ["Isabela", "Guilherme", "Juliana", "Pablo", "Michael", "Enzo", "Vicenzo", "Guilherme"]

try:
    pos = lista.index("Guilherme", 2)
    print(f"O Guilherme está na posição: {pos}")
except:
    print("Elemento não encontrado")

pos = lista.index("Pablo")
print(f"O Pablo está na posição: {pos}")

print(lista[-1])

try:
    pos = lista.index("João")
    print(f"O João está na posição: {pos}")
except ValueError as err:
    print("Não há João na lista")
    print("Erro: ", err)

# pos = lista.index("João")
# print(f"O João está na posição: {pos}")
