# Multiplying two matrix in Python

# Create two matrix using list
A = [[1,2],[3,4],[5,6],[7,8],[9,10]]
B = [[3,5,4],[6,7,1]]
# print(A)
# print(type(A))
# To print any elements we can use the command print(A[1][1])
# It is evident that the dimension of C =A*B would be (5x2) times (2x3) hence C is of (5x3)
# Let us first initialize a matrix
C = [[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0]]
C[0][0] = A[0][0]*B[0][0]+A[0][1]*B[1][0]
C[0][1] = A[0][0]*B[0][1]+A[0][1]*B[1][1]
C[1][0] = A[1][0]*B[0][0]+A[1][1]*B[1][0]
C[1][1] = A[1][0]*B[0][1]+A[1][1]*B[1][1]
print(C)
# Now we have to write this in for loop
# One can find the dimension of row and column using the following two commands
# print(len(A))
# print(len(A[0]))
# A is of dimension nxm
nA = len(A)
mA = len(A[0])
print("The values of nA is {} and mA is {}".format({nA},{mA}))
# B is of dimension nxm
nB = len(B)
mB = len(B[0])
print("The values of nB is {} and mB is {}".format({nB},{mB}))

# Using list comprehension we create a result of dimension nAxmB
result = [[0 for i in range(0,mB)] for j in range(0,nA)]
print("The values of nresult is {} and mresult is {}".format({len(result)},{len(result[0])}))
print(result)
for i in range(0,len(A)):
    for j in range(0,len(B[0])):
        # print("The value of i is {} and j is {}".format({i},{j}))
        for k in range(0,len(A[0])):
            result[i][j] += A[i][k]*B[k][j]

print(result)

# Let us create a function that would do the multiplication
def listMultiply(A,B):
    result = [[0 for i in range(0, len(B[0]))] for j in range(0, len(A))]
    for i in range(0, len(A)):
        for j in range(0, len(B[0])):
            # print("The value of i is {} and j is {}".format({i},{j}))
            for k in range(0, len(A[0])):
                result[i][j] += A[i][k] * B[k][j]
    return result

C1 = listMultiply(A,B)
print(C1)