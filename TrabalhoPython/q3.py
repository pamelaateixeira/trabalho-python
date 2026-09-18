codigo = int(input("digite o código do produto: "))
quantidade = int(input("digite a quantidade: "))

if codigo == 1:
    preco = 0.50
elif codigo == 2:
    preco = 1.00
elif codigo == 3:
    preco = 4.00
elif codigo == 5:
    preco = 7.00
elif codigo == 9:
    preco = 8.00
else:
    print("código inválido!")
    preco = 0

total = preco * quantidade

print("código:", codigo)
print("quantidade:", quantidade)
print("preço total:", total)

