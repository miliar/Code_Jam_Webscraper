import sys
def main():
    lauda = newts()
    #file=open('output.txt','w')
    for i, Naruto, Kabadi in lauda:
        r = jytoi(Naruto, Kabadi)
        r = ' '.join(str(x) for x in r)
        #file.write(f'Case #{i}: {r}\n')
        print(f'Case #{i}: {r}')
def jytoi(Naruto, Kabadi):
    if Kabadi == Naruto:
        return 0, 0
    naasta = Naruto - 1
    andhe = naasta // 2
    bakland = naasta - andhe
    kidhar = Kabadi - 1
    ka = kidhar // 2
    kb = kidhar - ka
    if Kabadi == 1:
        return bakland, andhe
    if Kabadi == 2:
        return jytoi(bakland, 1)
    if naasta % 2 == 0:
        return jytoi(bakland, kb)
    else:
        if kidhar % 2 == 0:
            return jytoi(andhe, ka)
        else:
            return jytoi(bakland, kb)
def newts():
    Totla = int(input())
    for i in range(1, Totla + 1):
        Naruto, Kabadi = [int(x) for x in input().split()]
        yield i, Naruto, Kabadi
if __name__ == '__main__':
    main()
