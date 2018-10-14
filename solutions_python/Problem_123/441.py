
Motes = []

def operations(size,i,th,c = 0):
    if size == 1: # nothing we can do but remove all
        return th
    if N <= i:
        return c # no cost to absorb nothing
    if th <= c:
        return th # threshold met, no need to consider more options

    if size > Motes[i]: # can absorb for free
        return operations(size + Motes[i], i+1, th, c)
    else: 
        # add the largest we can absorb and update th to the cost of
        # removing the rest
        newth = min(c + len(Motes[i:]), th)
        return operations(2 * size - 1, i, newth, c+1)

if __name__ == '__main__':
    T = int(input())
    case = 1
    while case <= T:
        A, N = [int(x) for x in input().split()]
        Motes = sorted([int(x) for x in input().split()])
        print('Case #{}: {}'.format(case, operations(A,0,N,0)))
        case += 1
        
