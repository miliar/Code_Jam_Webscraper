def f(N):
    def d(n:int):#Number of digits of 1's that can fit into the n. For example, 245 -> 111 and 1500 -> 1111 and 1000 -> 111 and 1024 -> 111
        n= int(n)
        o= 0#Number of 1's that can fit
        while True:
            if int('1' * (o+1))>n:
                return int('0'+'1'*o)
            o+=1
    addable=str(d(N))
    n0=0
    def isGood(n):
        if n>N:
            return False
        n=list(str(n))
        return n==sorted(n)

    while addable:
        guess=n0+int(addable)
        if isGood(guess):
            n0=guess
        else:
            addable=addable[1:]
    return n0
for i in range(int(input())):
    print(f(int(input())))
