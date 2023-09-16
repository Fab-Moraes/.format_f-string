nome = "Fabiano Moraes"
idade = 39
profissao = "Programador"
linguagem = "Python"


#  Metodo Format
print("Olá, me chamo {}. Eu tenho {} anos de idade,trabalho como {} e estou matriculado no curso de {}."
      .format(nome, idade, profissao, linguagem))

#  Tbm posso buscar pela posição
print("Olá, me chamo {3}. Eu tenho {2} anos de idade,trabalho como {1} e estou matriculado no curso de {0}." 
      .format(nome, idade, profissao, linguagem))

#  f-string
print(f"Olá, me chama {nome}. Eu tenho {idade} anos de idade, trabalho como {profissao} e estou matriculado no curso de {linguagem}.")


#  Formatar strings com f-string
#  EX

PI = 3.14159

print(f"Valor de PI: {PI:.2f}")
#  ou
print(f"Valor de PI: {PI:10.2f}")
