# Verifica se é possível construir um triângulo com as retas digitadas e retorna com o tipo do triângulo.
print('\033[31mCLASSIFICADOR DE TRIÂNGULOS\033[m')
print('\033[31m*\033[m' * 50)
r1 = float(input('Digite o tamanho da reta 1: '))
r2 = float(input('Digite o tamanho da reta 2: '))
r3 = float(input('Digite o tamanho da reta 3: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Com estas retas é possível formar um triangulo ', end=' ')
    if r1 == r2 == r3:
        print('\033[35mEQUILÁTERO\033[m.')
    elif r1 != r2 != r3 != r1:
        print('\033[35mESCALENO\033[m.')
    else:
        print('\033[35mISÓSCELES\033[m.')
else:
    print('Não é possível constuir um triângulo.')