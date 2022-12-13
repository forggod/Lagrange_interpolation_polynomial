import math


def crBasicPolynomal(i, x_ar):
    """
        Li(x) = composition((x-xj)/(xi-xj))
        L(x) = sum(yi*Li(x))
    """
    def basicPolynomal(x):
        dividend = 1
        divider = 1
        for j in range(len(x_ar)):
            if j != i:
                dividend *= x - x_ar[j]
                divider *= x_ar[i] - x_ar[j]
        return dividend/divider
    return basicPolynomal


def crLagrangePolynomial(x_array, y_array):
    def lagrangePolynomal(x):
        value = 0
        for i in range(len(y_array)):
            value += y_array[i]*bs_pol[i](x)
        return value

    bs_pol = []
    for i in range(len(x_array)):
        bs_pol.append(crBasicPolynomal(i, x_array))
    return lagrangePolynomal


x = [1, 1/2, 1/4, 1/8]
y = [round(math.sin((math.pi*el)/2), 8) for el in x]

lag_pol = crLagrangePolynomial(x, y)
x_ex = [0.2, 0.4]
y_ex = [round(lag_pol(el), 8) for el in x_ex]

print()

###################################################################################################################

print(" y = sin((PI * x) / 2) ".center(40, '#'))
print(f'Точное значение'.center(40, '-'))
[print(f'x = {el} | y = {round(math.sin((math.pi*el)/2), 8)}'.center(40, " ")) for el in x_ex]
print(f'Приблизительное значение'.center(40, '-'))
[print(f'x = {x_ex[i]} | y = {y_ex[i]}'.center(40, " ")) for i in range(2)]
print(f'Погрешность'.center(40, '*'))
[print(f'{round(abs(round(math.sin((math.pi*x_ex[i])/2), 8) - y_ex[i]), 10)}'.center(40, " ")) for i in range(2)]

###################################################################################################################

print()
