import re
from decimal import *

getcontext().prec = 7

def maketree(tree):
    return eval(
        re.sub(r'(\d+(\.\d+)?)', r'Decimal("\1")',
            re.sub(r',([a-z]+),', r',"\1",',
                re.sub(r'\s+', r',',
                    tree.replace('(', '[').replace(')', ']')
                ).replace(',]', ']').replace('[,', '[')
            )
        )
    )

def weight(features, tree):
    if len(tree) == 1:
        return tree[0]
    if tree[1] in features:
        return tree[0] * weight(features, tree[2])
    return tree[0] * weight(features, tree[3])

n = int(raw_input())
for i in range(n):
    print 'Case #%d:' % (i + 1)
    tree = []
    for j in range(int(raw_input())):
        tree.append(raw_input())
    tree = maketree('\n'.join(tree))
    for k in range(int(raw_input())):
        features = raw_input().split(' ')[2:]
        #print features
        print weight(features, tree)

