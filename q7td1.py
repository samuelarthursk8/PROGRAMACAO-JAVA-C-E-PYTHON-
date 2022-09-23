válidos=int(input("Digite o número de votos válidos:"))
brancos=int(input("Digite o número de votos brancos:"))
nulos=int(input("Digite o número de votos nulos:"))
total=válidos+brancos+nulos
válidos=(válidos*100)/total
brancos=(brancos*100)/total
nulos=(nulos*100)/total
print("Total de votos válidos é:", válidos)
print("Total de votos brancos é:", brancos)
print("Total de votos brancos é:", nulos)