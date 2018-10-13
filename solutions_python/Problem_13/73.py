import inspect
import os
import sys

def debug(*args, **kwargs):
    frame = sys._getframe(1)
    info = inspect.getframeinfo(frame)
    line = info[1]
    func = info[2]

    print('%s(%d):' % (func, line), file=sys.stderr, *args, **kwargs)

inf = 999999999999999999999999999

def trav(tree, n, exp):
    node = tree[n]

    # if leaf
    if isinstance(node, int):
        if node == exp:
            return 0
        else:
            return inf

    # if non leaf
    left = n * 2
    right = n * 2 + 1

    gate = 'and' if node[0] else 'or'
    exch = node[1]


    left0 = trav(tree, left, 0)
    left1 = trav(tree, left, 1)
    right0 = trav(tree, right, 0)
    right1 = trav(tree, right, 1)

    res = []
    if gate == 'and' and exp == 1:
        res.append(left1 + right1)
    elif gate == 'and' and exp == 0:
        res.append(left1 + right0)
        res.append(left0 + right1)
        res.append(left0 + right0)
    elif gate == 'or' and exp == 1:
        res.append(left1 + right0)
        res.append(left0 + right1)
        res.append(left1 + right1)
    elif gate == 'or' and exp == 0:
        res.append(left0 + right0)


    savegate = gate
    if exch:
        gate = ('and','or')[gate == 'and']
        if gate == 'and' and exp == 1:
            res.append(left1 + right1 + 1)
        elif gate == 'and' and exp == 0:
            res.append(left1 + right0 + 1)
            res.append(left0 + right1 + 1)
            res.append(left0 + right0 + 1)
        elif gate == 'or' and exp == 1:
            res.append(left1 + right0 + 1)
            res.append(left0 + right1 + 1)
            res.append(left1 + right1 + 1)
        elif gate == 'or' and exp == 0:
            res.append(left0 + right0 + 1)

    debug(n, savegate, min(res))

    return min(res)



    

def run_case():
    M, V = map(int, input().split())

    tree = []
    tree.append(V)
    for _ in range((M-1)//2):
        tree.append(list(map(int, input().split())))

    for _ in range((M+1)//2):
        tree.append(int(input()))

    debug(tree)
    debug(trav(tree, 1, V))

    res = trav(tree, 1, V)
    if res >= inf:
        return 'IMPOSSIBLE'
    else:
        return res

def main():
    
    N = int(input())
    for i in range(N):
        r = run_case()
        print('Case #%d: %s' % (i+1, r))


if __name__ == "__main__":
    main()
