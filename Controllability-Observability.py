# Obtain Controllability and observability of a matrix

import numpy as np
import control as ct
A = [[-1,-2],[-3, -4]]
B = [[5],[7]]
C = [[6,8]]
D = [[9]]
print("---Manual Way------")
Ctrb = np.hstack((B,np.matmul(A,B)))
print("The value of Controllability matrix is")
print(Ctrb)
dets = np.linalg.det(Ctrb)
print("The determinant of Controllability matrix is {:.2f}".format(dets))

Obsv = np.vstack((C,np.matmul(C,A)))
print("The value of Observability matrix is")
print(Obsv)
dets1 = np.linalg.det(Obsv)
print("The determinant of Observability matrix is {:.2f}".format(dets1))

print("---Direct Way------")

sys_ss = ct.ss(A,B,C,D)
print("The Controllability matrix is")
print(ct.ctrb(A,B))
print("The determinant of Controllability matrix is {:.2f}".format(np.linalg.det(ct.ctrb(A,B))))
print("The Observability matrix is")
print(ct.obsv(A,C))
print("The determinant of Observability matrix is {:.2f}".format(np.linalg.det(ct.obsv(A,C))))