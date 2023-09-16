# .format e f-string
Este código em Python demonstra várias maneiras de formatar strings, incluindo o uso do método .format() e f-strings. Vou comentar sobre cada parte do código:

Você define quatro variáveis: nome, idade, profissao, e linguagem, cada uma com seu próprio valor.

Em seguida, você utiliza o método .format() para criar uma string formatada. Aqui estão três exemplos de formatação de strings:

No primeiro exemplo, você insere as variáveis diretamente na string usando {} como espaços reservados e, em seguida, usa o método .format() para substituir os espaços reservados pelos valores correspondentes das variáveis.

No segundo exemplo, você especifica a posição das variáveis usando índices numéricos dentro das chaves {}. Isso permite que você especifique a ordem em que as variáveis serão inseridas na string.

No terceiro exemplo, você utiliza f-strings (strings formatadas) começando com f". Isso permite que você insira as variáveis diretamente na string usando {} como espaços reservados e o Python substitui automaticamente esses espaços reservados pelos valores das variáveis quando a string é criada. Essa é uma maneira mais moderna e legível de formatar strings em Python.

Em resumo, o código ilustra três maneiras diferentes de formatar strings em Python: o método .format(), a especificação de posições usando índices numéricos no método .format(), e o uso de f-strings para criar strings formatadas de forma mais simples e legível. Todas essas abordagens têm o mesmo resultado final, que é gerar uma saída formatada com os valores das variáveis inseridos na string.


-> A última parte do código demonstra como usar f-strings para formatar números:

PI = 3.14159 define a variável PI.

print(f"Valor de PI: {PI:.2f}") imprime o valor de PI com duas casas decimais usando uma f-string.

print(f"Valor de PI: {PI:10.2f}") imprime o valor de PI com duas casas decimais e preenchido com espaços à esquerda para ocupar um total de 10 caracteres.

Em resumo, o código ilustra a formatação de strings em Python usando diferentes métodos: o método .format() e f-strings. Além disso, ele demonstra como formatar números usando f-strings com diferentes precisões e larguras de campo.





