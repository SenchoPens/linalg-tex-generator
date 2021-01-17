import sympy
import copy


class Matrix:
    def __init__(self, A):
        if isinstance(A, Matrix):
            self.d = copy.deepcopy(A.d)
            self.n = A.n
            self.m = A.m
            return
        self.d = A
        self.m = len(self.d)
        self.n = len(self.d[0])
        for i in range(len(A)):
            for j in range(len(A[i])):
                if not isinstance(self.d[i][j], sympy.Symbol):
                    self.d[i][j] = sympy.Number(self.d[i][j])

    def __getitem__(self, key):
        return self.d[key]

    def __setitem__(self, key, value):
        self.d[key] = value

    def to_latex(self, det=False):
        mtype = ("v" if det else "p") + "matrix"
        l = '\\\\ \n'.join(' & '.join(map(sympy.latex, row)) for row in self.d)
        return f'\\begin{{{mtype}}}\n' + l + f'\n\\end{{{mtype}}}'

    def M(self, i, j):
        return Matrix([[self.d[p][q] for q in range(self.n) if q + 1 != j] for p in range(self.m) if p + 1 != i])

    def A(self, i, j):
        return (-1) ** (i + j) * self.M(i, j)


class GaussMatrix(Matrix):
    def __init__(self, A, n_of_free=1):
        super().__init__(A)
        if isinstance(A, GaussMatrix):
            self.n_of_free = A.n_of_free
        else:
            self.n_of_free = n_of_free

    def insertvrule(self, row):
        row = row[:-self.n_of_free] + [r'\vrule'] + row[-self.n_of_free:]
        return row

    def to_latex(self):
        l = '\\\\ \n'.join(' & '.join(map(sympy.latex, self.insertvrule(row))) for row in self.d)
        def wrap(rowops):
            return '\\begin{gmatrix}[p]\n' + l + '\n' + r'\rowops' '\n' + rowops + r'\end{gmatrix}' + '\n' + r'\leadsto'
        return wrap
