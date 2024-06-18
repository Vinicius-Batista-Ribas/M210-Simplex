import numpy as np
from simplex import solve_simplex
# Exemplo 1:  4 variaveis
# c = np.array([80, 70, 100, 16], dtype=float)
# A = np.array([[1, 1, 1, 4], [0, 1, 1, 2], [3, 2, 4, 0]], dtype=float)
# b = np.array([250, 600, 500], dtype=float)

# # Exemplo 2: 2 variaveis
# c = np.array([20, 40], dtype=float)
# A = np.array([[4, 15], [6, 30], [8, 16]], dtype=float)
# b = np.array([60,30,32], dtype=float)

# # Exemplo 3: 3 variaveis
# c = np.array([5, 4, 3], dtype=float)
# A = np.array([[1, 1, 1], [2, 2, 1]], dtype=float)
# b = np.array([4, 10], dtype=float)

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