def gcd(a,b):
    while b:
        a,b = b,a%b
    return a

P2 = tuple(2**i for i in range(41))

for TC in range(1,int(input())+1):

    P, Q = tuple(map(int, input().split('/')))

    P, Q = P//gcd(P,Q), Q//gcd(P,Q)
    P = max(x for x in P2 if x<=P)
    P, Q = P//gcd(P,Q), Q//gcd(P,Q)

    try:
        ans  = P2.index(Q)
    except:
        ans = 'impossible'
    
    print('Case #%d:' % TC, ans)
