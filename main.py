from typing import List


def jordan(mat: List[List[float]]) -> List[float]:
    num_coeficientes = len(mat)
    tam_extendido = len(mat[0])

    for i in range(num_coeficientes):
        pivot = mat[i][i]

        for j in range(num_coeficientes):
            if j != i:
                termo = mat[j][i]
                coeficiente = termo / pivot

                for k in range(tam_extendido):
                    mat[j][k] = mat[j][k] - (mat[i][k] * coeficiente)

    res = []
    for i in range(num_coeficientes):
        res.append(mat[i][tam_extendido - 1] / mat[i][i])

    for line in mat:
        print(line)

    return res

def interpolation(points) -> List[float]:
    mat = []
    for point in points:
        row = [1]
        for j in range(len(points) - 1):
            row.append(point[0] ** (j + 1))
        row.append(point[1])
        mat.append(row)

    return jordan(mat)


points = [(-1, 4), (0, 1), (2, -1)]
mat = [
    [1, -1, -1 ** 2, 4],
    [1, 0, 0 ** 2, 1],
    [1, 2, 2 ** 2, -1]
]

res = interpolation(points)
for row in res:
    print(row)
