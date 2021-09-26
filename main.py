from calculadora import Calculadora
from comodo import Comodo

#Declararção do objeto calc
calc = Calculadora()

#declaração do objeto comodo e dentro dela fazer o recebimanto dos dados
comodo = Comodo(
      input('Qual a largura do cômodo? '),
      input('Qual a profundidade do cômodo? '))

#Impressão dos resultados
print('A área das paredes é de',
      calc.calcular_area_paredes(comodo),
      'm².')
print('A área do teto é de',
      calc.calcular_area_teto(comodo),
      'm².')
print('A quantidade de tinta necessária é de',
      calc.calcular_litragem_tinta(),
      'Litros.')