__author__ = 'student'
A = input().split()
t=int(input())
for n in range(t):
    x=int(A[-1])
    i=len(A)-x-1
    A.insert(i, x)
    A.pop()
print(A)