# Input is positive integer n
# Output is list A with digits of n in its entries
def List(n):
    m=n
    A=[]
    while m!=0:
        A.append(m%10)
        m=m//10
    A=A[::-1]
    return A
'''
# Sample test
n=1234567890
A=List(n)
print(A)
'''
# Input is list A of digits
# Output is original integer n
def Int(A):
    sum=0
    for i in range(len(A)):
        sum=10*sum+A[i]
    return sum
'''
# Sample test
n=12345678901234567890
A=List(n)
print(A)
m=Int(A)
print(m)
'''

# Input is list A
# Output is smallest integer m where A[i]=A[k] for all i in [m,k] and 
# k is the smallest integer such that a descent occurs at k, that is
# where A[k]>A[k+1] or -1 if no such descent occurs for all k
def Descent(A):
    for k in range(len(A)-1):
        if A[k]>A[k+1]:
            for i in range(k):
                if A[k-i-1]<A[k]:
                    return k-i
            return 0
    return -1
'''
# Sample test
n1=22220863
A1=List(n1)
print(A1)
print(Descent(A1))
n2=134777757
A2=List(n2)
print(A2)
print(Descent(A2))
n3=123455
A3=List(n3)
print(A3)
print(Descent(A3))
'''
# Input is positive integer n
# Output is integer m that is the largest tidy number not exceeding n
def Last_Tidy(n):
    A=List(n)
    k=Descent(A)
    if k==-1:
        return n
    else:
        B=A[0:k]
        B.append(A[k]-1)
        for i in range(k+1,len(A) ):
            B.append(9)
        return Int(B)
'''
# Sample test
print(List(132))
print(Descent(List(132) ) )    
print(Last_Tidy(132))
for n in range(1111,2222):
    print(Last_Tidy(n)," ")
'''

f=open('B-large.in','r')
g=open('Tidy_large_output.txt','w')
t=int(f.readline())
for i in range(t):
    a1=f.readline()
    n=int(a1)
    g.write('Case #{0}: {1}\n'.format(i+1,Last_Tidy(n) ) )
g.close()

