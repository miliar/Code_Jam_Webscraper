import logging

logging.basicConfig()

def war(noami, ken):
    for n in naomi:
        for k in ken:
            if n < k:
                ken.remove(k)
                break
        else:
            return len(ken)

    return 0

def deceit(naomi, ken):
    for n in reversed(naomi):
        for k in reversed(ken):
            if k < n:
                ken.remove(k)
                break
        else:
            logging.info({'naomi':naomi, 'ken':ken})
            return N-len(ken)
    return N

if __name__ == '__main__':
    T = int(input())
    for case in range(T):
        N = int(input())
        naomi = sorted([float(x) for x in input().split()])
        ken = sorted([float(x) for x in input().split()])
        print('Case #{}: {} {}'.format(case+1, deceit(naomi[:], ken[:]),
                                       war(naomi, ken)))
