def crBasicPolynomal(i, x_ar):
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
y_array = [0, 1, 3, 2, 5, 2, 5]

lag_pol = crLagrangePolynomial(x_array, y_array)
for x in x_array:
    print("x =", float(x), "\t y =", float(lag_pol(x)))
