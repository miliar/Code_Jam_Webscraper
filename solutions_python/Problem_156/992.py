#! /usr/bin/python3

def partition(n):
    for i in range(2, n//2 + 1):
        yield n - i, i

def resolve(liste):
    maxi = max(liste)
    nb_maxi = liste.count(maxi)
    if (nb_maxi >= maxi):
        return maxi
    rv = maxi
    liste = [x for x in liste if x != maxi]
    for a, b in partition(maxi):
        new_liste = liste.copy()
        new_liste.extend([a, b] * nb_maxi)
        tmp = resolve(new_liste)
        if tmp < rv:
            rv = tmp
    rv += nb_maxi
    if rv >= maxi:
        return maxi
    return rv

def main():
    T = int(input())
    for i in range(1, T + 1):
        D = int(input())
        P = list(map(int, input().split()))
        print("Case #%d: %d" % (i, resolve(P)))

if (__name__ == "__main__"):
    main()
