__author__ = 'student'
A=input().split()
m=0
for x in A:
    k=A.count(x)
    if k>m:
        m=k
        s=x
print(s)