__author__ = 'student'
f = open('split3', 'r')
A=f.read().rstrip()
for i in range(0, len(A)//2):
    print(A[i]+' '+A[-1-i], end=" ")
if len(A)/2!=0:
    print(A[len(A)//2])