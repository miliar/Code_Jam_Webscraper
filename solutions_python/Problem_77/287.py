def f(l):
    sort=list(sorted(l))
    k=len([i for i,j in zip(l,sort) if i!=j])
    return str(k)+'.000000'
def main():
    s=input()
    T=int(s)
    for i in range(T):
        s=input()
        s=input()
        L=[int(i) for i in s.split(' ')]
        print('Case #{0}: {1}'.format(i+1,f(L)))
main()
