import sympy
import copy
from matrix import GaussMatrix


DIV = True
PRINT = None


def eps1(A, j, i, k):
    if i == j:
        raise ValueError()
    rowops = r'\add' + f'[{k}]{{{i}}}{{{j}}}'
    for t in range(len(A[j])):
        A[j][t] += k * A[i][t]
    return (A, rowops)


def eps2(A, i, j):
    if i == j:
        raise ValueError()
    rowops = r'\swap' + f'{{{i}}}{{{j}}}'
    A[i], A[j] = A[j], A[i]
    return (A, rowops)


def eps3(A, i, k, div=False, to_int=False):
    if k == 0:
        raise ValueError()
    op = ':' if div else r'\cdot'
    rowops = r'\mult' + f'{{{i}}}{{{op} {k}}}'
    for t in range(len(A[i])):
        if div:
            A[i][t] /= k
        else:
            A[i][t] *= k
        if to_int:
            A[i][t] = int(A[i][t])
    return (A, rowops)


def apply_ops(A, args):
    rowops = []
    for t in args:
        if len(t) == 2:
            f, a = t
            A, ops = f(A, *a)
        else:
            f, a, kw = t
            A, ops = f(A, *a, **kw)
        rowops.append(ops)
    return A, '\n'.join(rowops) + '\n' if rowops else ''


def mod_print(A, ops):
    l = A.to_latex()
    A, rowops = apply_ops(A, ops)
    print(l(rowops))
    return A


def _mods_print(A, args):
    for arg in args:
        A = mod_print(A, arg)
    return A


def mods_print(A, *args):
    i = 0
    cur = []
    while i < len(args):
        if args[i] is PRINT:
            A = mod_print(A, cur)
            cur = []
            i += 1
            continue
        cur.append((args[i], args[i + 1]))
        i += 2
    if cur:
        A = mod_print(A, cur)
    mod_print(A, [])
    return A


def main1():
    A = GaussMatrix([[-9, -6, -2, 1, -13, -25, -13], [24, 16, 5, 1, 46, 56, 31], [5, 3, 1, 1, 12, 9, 6]], 3)
    A = mods_print(A,
                   eps1, (1, 0, 2),
                   eps1, (1, 2, -1),
                   PRINT,
                   eps1, (0, 2, 2),
                   PRINT,
                   eps1, (2, 0, -5),
                   eps1, (1, 0, -1),
                   PRINT,
                   eps1, (2, 1, -3),
    )


def main1_m():
    A = GaussMatrix([
        [-24, 10, 5, 2, -21, -58, 32],
        [3, 1, 0, 1, -6, 7, -2],
        [-5, 2, 1, 2, -4, -12, 5]
    ])
    A = mods_print(A,
                   eps1, (0, 2, -5),
                   PRINT,
                   eps1, (1, 0, -3),
                   eps1, (2, 0, 5),
                   PRINT,
                   eps1, (2, 1, -2),
    )


def main4():
    a = sympy.Symbol('a')
    b = sympy.Symbol('b')
    A = GaussMatrix([[a, 0, -2, -1], [4, 1, 0, 4],
                [8, 4, b, 7]], 1)
    A = mods_print(A,
        (
            (eps1, (1, 2, -2)),
            (eps1, (1, 0, -a / 4)),
        ),
        (
            (eps3, (0, 4)),
            (eps2, (0, 1)),
            (eps3, (2, 2, {'div': True})),
        ),
        (
            (eps1, (2, 1, a)),
            (eps2, (1, 2)),
        ),
        (
        )
    )


main1_m()
