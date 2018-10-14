T = int(input())
for case in range(1, T+1):
    liczby = input().split()
    liczby = [int(a) for a in liczby]
    N = liczby[0]
    S = liczby[1]
    s = 0
    w = 0
    p = liczby[2]
    t = []
    for i in range(3,len(liczby)):
        t = liczby[i]
        if t%3==0:
            if t/3 >= p:
                w+=1
            elif t/3 == p-1:
                if s < S and t>0:
                    w+=1
                    s+=1
        else:
            if t//3 >= p-1:
                w+=1
            elif t//3 == p-2 and t%3 == 2:
                if s < S and t>1:
                    w+=1
                    s+=1
    print("Case #{0}: {1}".format(case, w))
