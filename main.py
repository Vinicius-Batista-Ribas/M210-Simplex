import numpy as np
from simplex import solve_simplex

# def input_vector(name, size):
#     print(f"Digite os elementos do vetor {name} (separados por espaço):")
#     vector = input()
#     vector = np.array(list(map(float, vector.split())), dtype=float)
#     if vector.size != size:
#         print(f"Erro: O vetor {name} deve ter {size} elementos.")
#         return input_vector(name, size)
#     return vector

# def input_matrix(name, rows, cols):
#     print(f"Digite os elementos da matriz {name} (um valor de cada vez, total {rows*cols} valores):")
#     matrix = []
#     for i in range(rows):
#         print(f"Linha {i+1} (separados por espaço):")
#         row = input()
#         row = list(map(float, row.split()))
#         if len(row) != cols:
#             print(f"Erro: A linha {i+1} da matriz {name} deve ter {cols} elementos.")
#             return input_matrix(name, rows, cols)
#         matrix.append(row)
#     return np.array(matrix, dtype=float)

# print("Menu para entrada de dados")

# # Solicita os tamanhos das estruturas
# c_size = int(input("Digite o tamanho do vetor z: "))
# A_rows = int(input("Digite o número de linhas da matriz condicao: "))
# A_cols = int(input("Digite o número de colunas da matriz condicao: "))
# b_size = int(input("Digite o tamanho do vetor LD: "))

# Coleta os dados
# c = input_vector('z', c_size)
# A = input_matrix('condicao', A_rows, A_cols)
# b = input_vector('LD', b_size)

# Exibe os dados inseridos
# print("\nDados inseridos:")
# print("Vetor c:", c)
# print("Matriz A:\n", A)
# print("Vetor b:", b)


# Exemplo 1:  4 variaveis
# c = np.array([80, 70, 100, 16], dtype=float)
# A = np.array([[1, 1, 1, 4], [0, 1, 1, 2], [3, 2, 4, 0]], dtype=float)
# b = np.array([250, 600, 500], dtype=float)

# # Exemplo 2: 2 variaveis
c = np.array([20, 40], dtype=float)
A = np.array([[4, 15], [6, 30], [8, 16]], dtype=float)
b = np.array([60,30,32], dtype=float)

# Exemplo 3: 3 variaveis
# c = np.array([5, 4, 3], dtype=float)
# A = np.array([[1, 1, 1], [2, 2, 1]], dtype=float)
# b = np.array([4,10], dtype=float)

# Exemplo 4: 2 variaveis e 2 restricoes
# c = np.array([3, 2], dtype=float)
# A = np.array([[1, 1]], dtype=float)  # Uma única restrição
# b = np.array([5], dtype=float)



optimal_solution, shadow_prices, objective_value = solve_simplex(c, A, b)

# Formatar saída para 2 casas decimais
optimal_solution_rounded = np.round(optimal_solution, decimals=2)
shadow_prices_rounded = np.round(shadow_prices, decimals=2)
objective_value_rounded = np.round(objective_value, decimals=2)

# Imprimir resultados
print("Ponto ótimo:", optimal_solution_rounded)
print("Preços sombra:", shadow_prices_rounded)
print("Valor da função objetivo:", objective_value_rounded)