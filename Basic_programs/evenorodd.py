def fun1(n):
    if n%2==0:
        return True
    return False
def fun2(n):
    return n%2==0
def fun3(n):
    return (n&1)==0
for i in range(11):
    print(i,fun1(i),fun2(i),fun3(i),sep='\t')

    