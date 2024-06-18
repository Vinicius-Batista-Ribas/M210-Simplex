import numpy as np

def initialize_table(c, A, b):
    m, n = A.shape
    table = np.zeros((m + 1, n + m + 1))
    
    table[0, :n] = -c
    table[0, -1] = 0
    
    table[1:, :n] = A
    table[1:, n:n + m] = np.eye(m)
    table[1:, -1] = b
    
    return table

def is_optimal(table):
    return np.allclose(table[0, :-1], np.maximum(table[0, :-1], 0))

def get_pivot_column(table):
    return np.argmin(table[0, :-1])

def get_pivot_line(table, entering_col):
    rhs = table[1:, -1]
    column = table[1:, entering_col]
    
    mask = column > 0
    ratios = rhs[mask] / column[mask]
    
    return np.argmin(ratios) + 1

def update_table(table, pivot_row, pivot_col):
    pivot_element = table[pivot_row, pivot_col]
    table[pivot_row] /= pivot_element
    
    for row in range(table.shape[0]):
        if row == pivot_row:
            continue
        
        multiplier = table[row, pivot_col]
        table[row] -= multiplier * table[pivot_row]

def solve_simplex(c, A, b, verbose=True):
    table = initialize_table(c, A, b)
    
    iteration = 0
    
    while not is_optimal(table):
        if verbose:
            print(f"Iteração {iteration}:")
            print(np.round(table, 2)) 
            print()
        
        pivot_col = get_pivot_column(table)
        pivot_row = get_pivot_line(table, pivot_col)
        update_table(table, pivot_row, pivot_col)
        
        iteration += 1
    
    if verbose:
        print(f"Iteração {iteration}:")
        print(np.round(table, 2)) 
        print()

    optimal_point = table[1:, -1]
    preco_sombra = table[0, :-1]
    z = table[0,-1]

    optimal_point[np.abs(optimal_point) < 1e-8] = 0.0
    preco_sombra[np.abs(preco_sombra) < 1e-8] = 0.0
    
    return optimal_point, preco_sombra, z

