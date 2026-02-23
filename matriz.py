# establecemos valores de matriz
matrix = [
   [2, 4, 6],
   [1, 3, 5],
   [7, 8, 9]
]

# recorremos matriz y presentamos valores en pantalla
for f in range(3):
    for c in range(3):
        print("[" + str(matrix [f][c]), end="]")
    print("")