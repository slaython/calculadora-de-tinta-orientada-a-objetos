from calculadora import Calculadora
calc = Calculadora()

#reeceber as variáveis
largura: float = float(input(
      'Qual a largura do cômodo? '))
altura: float = 2.9
profundidade: float = float(input(
      'Qual a profundidade do cômodo? '))

#calculo das áreas das paredes
#calc.area_paredes: float = (2 * (largura + profundidade) * altura)

#calculo da área do teto
#calc.area_teto: float = (largura * profundidade)

print('A área das paredes é de',
      calc.calcular_area_paredes(altura, largura, profundidade), 'm².')

print('A área do teto é de',
      calc.calcular_area_teto(largura, profundidade), 'm².')

print('A quantidade de tinta necessária é de',
      calc.calcular_litragem_tinta(), 'Litros.')