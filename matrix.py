"""
A matrix will be an N sized list of 4 element lists.
Each individual list will represent an [x, y, z, 1] point.
For multiplication purposes, consider the lists like so:
x0  x1      xn
y0  y1      yn
z0  z1  ... zn
1  1        1
"""
import math

#print the matrix such that it looks like
#the template in the top comment
def print_matrix( matrix ):
    cols = len(matrix)
    rows = len(matrix[0])
    for row in range(rows):
        line = ""
        for col in range(cols):
            line += str(matrix[col][row]) + '  '
        print (line)

#turn the paramter matrix into an identity matrix
#you may assume matrix is square
def ident( matrix ):
    nm = new_matrix()
    index = 0
    while index < 4:
        nm[index][index] = 1
        index+=1
    matrix = nm
    return matrix

#multiply m1 by m2, modifying m2 to be the product
#m1 * m2 -> m2
def matrix_mult( m1, m2 ):
    nm = new_matrix(4,len(m2))
    row = 0
    while row < 4:
        for col in range(len(m2)):
            prod = 0
            for n in range(len(m1)):
                prod += (m1[n][row] * m2[col][n])
            nm[col][row] = prod
        row += 1
    m2 = nm
    return m2


def new_matrix(rows = 4, cols = 4):
    m = []
    for c in range( cols ):
        m.append( [] )
        for r in range( rows ):
            m[c].append( 0 )
    return m
