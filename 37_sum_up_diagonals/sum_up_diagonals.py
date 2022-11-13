def sum_up_diagonals(matrix):
    """Given a matrix [square list of lists], return sum of diagonals.

    Sum of TL-to-BR diagonal along with BL-to-TR diagonal:

        >>> m1 = [
        ...     [1,   2],
        ...     [30, 40],
        ... ]
        >>> sum_up_diagonals(m1)
        73

        >>> m2 = [
        ...    [1, 2, 3],
        ...    [4, 5, 6],
        ...    [7, 8, 9],
        ... ]
        >>> sum_up_diagonals(m2)
        30
    """
    matrix_length = len(matrix)

    downward_slope = 0
    upward_slope = 0

    for list in range(0, matrix_length):
        for integer in range(0, matrix_length):
            if (i==j):
                downward_slope += matrix[list][range]
            
            if ((i+j)==(matrix_length-1)):
                upward_slope += matrix[list][range]
                
    return upward_slope + downward_slope