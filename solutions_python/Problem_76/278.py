from functools import reduce
def f(l):
    result=reduce(lambda x,y:x^y,l)
    if result!=0:
        return 'NO'
    else:
        return sum(l)-min(l)
def main():
    s=input()
    T=int(s)
    for i in range(T):
        s=input()
        s=input()
        l=[int(i) for i in s.split(' ')]
        print('Case #{0}: {1}'.format(i+1,f(l)))
main()
