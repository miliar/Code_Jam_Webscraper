import logging
import sys

bound = 1000
#logging.basicConfig(level=logging.DEBUG)

def children(plates):
    pmax = max(plates)
    idx = plates.index(pmax)
    # put half of the largest pile on an empty plate
    child = plates[:]
    child[idx] = pmax//2
    child.append(pmax-child[idx])
    yield child
    # consider taking 3 from the top of pmax if pmax is odd
    if pmax % 2:
        child = plates[:]
        child[idx] = pmax-3
        child.append(3)
        yield child
    # consider just eating instead of using a special minute
    eat = [max(0, x-1) for x in plates]
    yield eat

def dfbnb(plates, depth):
    'implements depth first branch and bound to find the shortest breakfast possible.'
    global bound
    logging.debug('dfbnb({})'.format({'plates':plates, 'depth':depth, 'bound':bound}))
    # ignore branches that won't lead to better solutions.
    if depth >= bound:
        return depth
    # no point using special minutes whenever the largest pile has 3 pancakges or less
    pmax = max(plates)
    if pmax <= 3:
        bound = min(bound, depth+pmax)
        return depth+pmax
    # consider different strategies and return the min
    ans = bound
    for child in children(plates):
        ans = min(ans, dfbnb(child, depth+1))
    return ans

def minutes(plates):
    global bound
    bound = max(plates)
    return dfbnb(plates, 0)

def main():
    case = 1
    data = open(sys.argv[1])
    T = int(data.readline())
    while T:
        D = int(data.readline())
        plates = [int(p) for p in data.readline().split()]
        print('Case #{}: {}'.format(case, minutes(plates)))
        case +=1
        T -= 1

main()
