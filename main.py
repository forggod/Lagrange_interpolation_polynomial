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
                divider *= x_array[i] - x_array[j]
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

x_array = [0, 2, 3, 5, 7, 10, 20]
y_array = [1]*len(x_array)

lag_pol = crLagrangePolynomial(x_array, y_array)
# for x in x_array:
#     print("x =", float(x), "\t y =", float(lag_pol(x)))

# на вход отрезок и кол-во узлов в нём
# взять любую точку и подставить в полином Лагранжа, вычислив точное значение

a = int(input("Введите начало отрезка "))
b = int(input("Введите конец отрезка "))
c = int(input("Введите кол-во узлов "))

knot = [float((b-a)/c*i) for i in range(c)]

x_array = knot
y_array = [1, 1, 1, 1, 1, 1, 1]
lag_pol = crLagrangePolynomial(x_array, y_array)

x = float(knot[int(c/2)] + (knot[int((c/2))+1] - knot[int(c/2)])*0.5)
print("x =", float(x), "\t y =", float(lag_pol(x)))
