# -*- coding: utf-8 -*-
from utils.matrix import (elements_sum, diagonal_sum)

A = [[1, 4, 7, 8, -2], [5, 7, -5, -7, 3], [-8, 1, 0, 4, 0], [1, 5, 6, -3, 7], [2, 4, -7, 9, 0]]

print "\nDada la matriz:\n"
print "\n".join(["\t".join([str(elmnt) for elmnt in row]) for row in A])
print "\n+ La suma de sus elementos es %s" % elements_sum(A)
print "+ La suma de los elementos de su diagonal principal es %s\n" % diagonal_sum(A)
