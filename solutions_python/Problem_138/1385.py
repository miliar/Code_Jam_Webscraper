def main():
    T = int(input())

    for T in range(T):
        N = int(input())
        print("Case #{}: {}".format(T+1, "%d %d" % solve(N)))
        
def solve(N):
    naiomi_1 = [float(x) for x in input().split()]
    ken_1 = [float(x) for x in input().split()]

    naiomi_1.sort()
    ken_1.sort()

    naiomi_2 = list(naiomi_1)
    ken_2 = list(ken_1)

    dect_war = 0
    for i in range(N):
        if (len(naiomi_1) == 1):
            dect_war += 1 if naiomi_1[0] > ken_1[0] else 0
            del(naiomi_1[0])
            del(ken_1[0])
        else:
            if naiomi_1[0] < ken_1[0]:
                del(naiomi_1[0])
                del(ken_1[len(ken_1) - 1])
            else:
                del(naiomi_1[0])
                del(ken_1[0])
                dect_war += 1
                
    shitty_war = 0
    for i in range(N):
        ken_next = findGreater(ken_2, naiomi_2[0])
        if (naiomi_2[0] > ken_2[ken_next]):
            shitty_war += 1
        
        del(naiomi_2[0])
        del(ken_2[ken_next])

    assert(len(naiomi_1) == 0)
    assert(len(naiomi_2) == 0)
    assert(len(ken_1) == 0)
    assert(len(ken_2) == 0)

    return (dect_war, shitty_war)

def findGreater(l, n):
    if l[len(l) - 1] < n:
        return 0
    for i, val in enumerate(l):
        if val > n:
            return i
    return 0
if __name__ == '__main__':
    main()
