homem1 = int(input("digite a idade do primeiro homem: "))
homem2 = int(input("digite a idade do segundo homem: "))

mulher1 = int(input("digite a idade da primeira mulher: "))
mulher2 = int(input("digite a idade da segunda mulher: "))

homem_velho = max(homem1, homem2)
homem_novo = min(homem1, homem2)

mulher_velha = max(mulher1, mulher2)
mulher_nova = min(mulher1, mulher2)

soma = homem_velho + mulher_nova
produto = homem_novo * mulher_velha

print("soma:", soma)
print("produto:", produto)

