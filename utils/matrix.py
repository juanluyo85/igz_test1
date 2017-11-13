# -*- coding: utf-8 -*-

def elements_sum(matrix):
    """
    Esta función debe devolver la suma de todos los elementos de la matriz cuadrada dada
    :param matrix: matriz cuadrada
    :return: La suma de todos los elementos de la matriz
    """
    return sum([sum(line) for line in matrix])


def diagonal_sum(matrix):
    """
    Esta función debe devolver la suma de los elementos de la diagonal principal
    de la matriz cuadrada dada
    :param matrix: matriz cuadrada
    :return: La suma de los elementos de la diagonal principal de la matriz
    """
    size = len(matrix)
    sum = 0
    for i in range(size):
        sum += matrix[i][i]
    return sum