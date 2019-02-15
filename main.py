from display import *
from draw import *
from matrix import *

screen = new_screen()
color = [ 10, 12, 100 ]
matrix = new_matrix(4,10)
m1 = [[1, 2, 3, 1], [4, 5, 6, 1]]
m2 = [[2, 4], [4, 6], [6, 8]]

print_matrix(matrix)
print ('\n')
print_matrix(ident(matrix))
print ('\n')
print("Matrix 1")
print_matrix(m1)
print ('\n')
print("Matrix 2")
print_matrix(m2)
print ('\n')
print("m1 * m2")
print_matrix(matrix_mult(m1, m2))

edgeMat = new_matrix()

add_point(edgeMat, 250, 450)
add_point(edgeMat, 50, 250)

angle = 90
x = 50
y = 250
while angle > -90:
    newX = rotate(x, y, 250, 250, angle)[0]
    newY = rotate(x, y, 250, 250, angle)[1]
    add_edge(edgeMat, x, y, 0, newX, newY, 0)
    x = newX
    y = newY
    angle -= .01


draw_lines(edgeMat, screen, color)
display(screen)
save_extension(screen, 'matrixIMG.png')
