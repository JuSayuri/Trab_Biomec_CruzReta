#coding: utf-8
"""
Nome: Juliana Sayuri Sakamoto
Nº USP: 11858411
Professor: Paulo Santiago
Trabalho Biomecânica - cruzamento de retas
"""
"""
A seguir são as fórmulas que faça a mesma coisa da planilha cruzreta.xlsx
"""
"""
Valores de xc1, yc1, xp1, yp1, xc2, yc2, xp2, yp2 da planilha cruzreta.xlsx
"""
xc1 = [365.800, 365.800, 107.000]
yc1 = [211.000, 107.000, 211.000]
xp1 = [0.000, 0.000, 50.900]
yp1 = [133.90, 50.900, 133.900]
xc2 = [131.400, 131.400, 151.800]
yc2 = [384.800, 151.800, 384.800]
xp2 = [179.400, 179.400, 17.100]
yp2 = [0.000, 17.100, 0.000]

print("MENU")
print("1 - Prosseguir com valores pre-definidos")
print("2 - Inserir manualmente valores para calculos")
print("3 - sair")

menu_options = {
    1: 'Option 1',
    2: 'Option 2',
    3: 'Exit',
}
def print_menu():
    for key in menu_options.keys():
        print (key, '--', menu_options[key] )
option = int(input('Escolha uma opcao: '))
if option == 1:
    pass
elif option == 2:
    xc1[0] = float(input("xc1 - Valor 1: "))
    xc1[1] = float(input("xc1 - Valor 2: "))
    xc1[2] = float(input("xc1 - Valor 3: "))
    yc1[0] = float(input("yc1 - Valor 1: "))
    yc1[1] = float(input("yc1 - Valor 2: "))
    yc1[2] = float(input("yc1 - Valor 3: "))
    xp1[0] = float(input("xp1 - Valor 1: "))
    xp1[1] = float(input("xp1 - Valor 2: "))
    xp1[2] = float(input("xp1 - Valor 3: "))
    yp1[0] = float(input("yp1 - Valor 1: "))
    yp1[1] = float(input("yp1 - Valor 2: "))
    yp1[2] = float(input("yp1 - Valor 3: "))
    xc2[0] = float(input("xc2 - Valor 1: "))
    xc2[1] = float(input("xc2 - Valor 2: "))
    xc2[2] = float(input("xc2 - Valor 3: "))
    yc2[0] = float(input("yc2 - Valor 1: "))
    yc2[1] = float(input("yc2 - Valor 2: "))
    yc2[2] = float(input("yc2 - Valor 3: "))
    xp2[0] = float(input("xp2 - Valor 1: "))
    xp2[1] = float(input("xp2 - Valor 2: "))
    xp2[2] = float(input("xp2 - Valor 3: "))
    yp2[0] = float(input("yp2 - Valor 1: "))
    yp2[1] = float(input("yp2 - Valor 2: "))
    yp2[2] = float(input("yp2 - Valor 3: "))
    print("Valores inseridos: ")
    print(xc1)
    print(yc1)
    print(xp1)
    print(yp1)
    print(xc2)
    print(yc2)
    print(xp2)
    print(yp2)
else:
    print('Invalid option. Please enter a number between 1 and 4.')

"""
Valores de mr1 - coeficiente angular
"""
mr1a = (yp1[0] - yc1[0])/(xp1[0] - xc1[0])
mr1b = (yp1[1] - yc1[1])/(xp1[1] - xc1[1])
mr1c = (yp1[2] - yc1[2])/(xp1[2] - xc1[2])

"""
Valores de mr2 - coeficiente angular
"""
mr2a = (yp2[0] - yc2[0])/(xp2[0] - xc2[0])
mr2b = (yp2[1] - yc2[1])/(xp2[1] - xc2[1])
mr2c = (yp2[2] - yc2[2])/(xp2[2] - xc2[2])

"""
Valores de br1 - coeficiente linear
"""
br1a = (-1*(mr1a*xc1[0]-yc1[0]))
br1b = (-1*(mr1b*xc1[1]-yc1[1]))
br1c = (-1*(mr1c*xc1[2]-yc1[2]))

"""
Valores de br2 - coeficiente linear
"""
br2a = (-1*(mr2a*xc2[0]-yc2[0]))
br2b = (-1*(mr2b*xc2[1]-yc2[1]))
br2c = (-1*(mr2c*xc2[2]-yc2[2]))

"""
Valores de X
"""
Xa = (-(mr2a*xc2[0]) + yc2[0] + (mr1a*xc1[0]) - yc1[0])/(mr1a - mr2a)
Xb = (-(mr2b*xc2[1]) + yc2[1] + (mr1b*xc1[1]) - yc1[1])/(mr1b - mr2b)
Xc = (-(mr2c*xc2[2]) + yc2[2] + (mr1c*xc1[2]) - yc1[2])/(mr1c - mr2c)

"""
Valores de Y
"""
Ya = (mr1a*Xa) - (mr1a*xc1[0]) + yc1[0]
Yb = (mr1b*Xb) - (mr1b*xc1[1]) + yc1[1]
Yc = (mr1c*Xc) - (mr1c*xc1[2]) + yc1[2]

"""
Valores de REC3D
"""
REC3D_X = (Xa + Xb)/2
REC3D_Y = (Ya + Yc)/2
REC3D_Z = (Yb + Xc)/2

"""
Valores de Real
"""
Real_X = 159.300
Real_Y = 168.200
Real_Z = 74.900

"""
Valores de erro
"""
erro_X = (Real_X - REC3D_X)
erro_Y = (Real_Y - REC3D_Y)
erro_Z = (Real_Z - REC3D_Z)

"""
Valores de erro absoluto
"""
erro_abs_X = (abs(erro_X))
erro_abs_Y = (abs(erro_Y))
erro_abs_Z = (abs(erro_Z))

"""
Valores de erro total
"""

erro_total = (erro_abs_X + erro_abs_Y + erro_abs_Z)/3

print("-----------------------------------------------------------------------------------------")
print("Os valores de MR1 sao:   \t%s\t\t%s\t\t%s" % (mr1a, mr1b, mr1c))
print("Os valores de MR2 sao:   \t%s\t\t%s\t\t%s" % (mr2a, mr2b, mr2c))
print("Os valores de BR1 sao:   \t%s\t\t\t\t\t%s\t\t\t\t\t%s" % (br1a, br1b, br1c))
print("Os valores de BR2 sao:   \t%s\t\t\t\t\t%s\t\t\t\t%s" % (br2a, br2b, br2c))
print("Os valores de X sao:     \t%s\t\t%s\t\t%s" % (Xa, Xb, Xc))
print("Os valores de Y sao:     \t%s\t\t%s\t\t%s" % (Ya, Yb, Yc))
print("Os valores de REC3D sao: \t%s\t\t%s\t\t%s" % (REC3D_X, REC3D_Y, REC3D_Z))
print("Os valores de erro sao:  \t%s\t\t%s\t\t%s" % (erro_X, erro_Y, erro_Z))
print("Os valores de erro abs sao: %s\t\t%s\t\t%s" % (erro_abs_X, erro_abs_Y, erro_abs_Z))
print("O valor de erro total e: \t%s" % (erro_total))