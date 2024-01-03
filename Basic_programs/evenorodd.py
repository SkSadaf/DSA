def fun1(n):
    if n%2==0:
        return True
    return False
for i in range(11):
    print(i,fun1(i),sep='\t')