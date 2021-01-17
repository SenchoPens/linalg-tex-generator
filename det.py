import sympy
from matrix import Matrix


def main4():
    x = sympy.Symbol('x')
    A0 = Matrix([
        [0, 0, x, 0, 0, 2],
        [x, x, 9, x, 0, 1],
        [0, 7, 0, 8, 4, 4],
        [0, 2, 0, 0, 0, 7],
        [5, 4, x, x, 4, 5],
        [0, 4, 2, 2, 5, 5],
    ])
    A = Matrix([
        [0, 0,  x, 0, 0, 2],
        [x, 0,  9, x, 0, 1],
        [0, 7,  0, 8, 4, 0],
        [0, 2,  0, 0, 0, 7],
        [5, -1, x, x, 4, 1],
        [0, 4,  2, 2, 5, 0],
    ])

    p = A.M(1, 3)
    q = A.M(1, 6)
    a = p.M(1, 1)
    b = p.M(4, 1)
    c = q.M(1, 1)
    d = q.M(4, 1)

    print(b.M(1, 2).to_latex(det=True))
    print(b.M(1, 4).to_latex(det=True))
    print(sympy.Matrix(A.d).det())


# main4()


def main4_m():
    x = sympy.Symbol('x')
    A = Matrix([
        [0, 2, x, 0, 0, 0],
        [0, 0, x, 9, 0, x],
        [0, 0, 0, 4, 2, 3],
        [x, 5, 0, 0, x, x],
        [0, 5, 0, 2, 0, 9],
        [8, 5, 5, 1, 1, 2],
    ])

    # p = A.M(1, 3)
    # q = A.M(1, 6)
    # a = p.M(1, 1)
    # b = p.M(4, 1)
    # c = q.M(1, 1)
    # d = q.M(4, 1)

    # print(b.M(1, 2).to_latex(det=True))
    # print(b.M(1, 4).to_latex(det=True))
    print(sympy.Matrix(A.d).det())


# main4_m()


def main5_m():
    x = sympy.Symbol('x')
    A = Matrix([
        [2, x, 4, 0, 1, 0, 7],
        [x, 1, 3, 0, 6, 0, x],
        [4, 3, 1, 8, 8, x, 1],
        [0, 0, 8, 1, x, 6, 5],
        [1, 6, 8, x, 7, 9, 2],
        [0, 0, x, 6, 9, 7, 8],
        [7, x, 1, 5, 2, 8, 1],
    ])
    print(sympy.Matrix(A.d).det())


main5_m()
