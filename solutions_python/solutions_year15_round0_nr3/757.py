#!/usr/bin/python3

T = int(input())

table = {
    '1': { '1': '1', 'i': 'i', 'j': 'j', 'k': 'k' },
    'i': { '1': 'i', 'i': '-1', 'j': 'k', 'k': '-j'},
    'j': { '1': 'j', 'i': '-k', 'j': '-1', 'k': 'i'},
    'k': { '1': 'k', 'i': 'j', 'j': '-i', 'k': '-1'},
}

def solve(base_S, X):
    S = base_S * X
    positive = True

    accu = '1'
    while not (accu == 'i' and positive):
        if not S:
            return "NO"
        accu = table[accu][S[0]]
        if accu[0] == '-':
            positive = not positive
            accu = accu[1]
        S = S[1:]

    accu = '1'
    while not (accu == 'j' and positive):
        if not S:
            return "NO"
        accu = table[accu][S[0]]
        if accu[0] == '-':
            positive = not positive
            accu = accu[1]
        S = S[1:]

    accu = '1'
    while not (accu == 'k' and positive and not S):
        if not S:
            return "NO"
        accu = table[accu][S[0]]
        if accu[0] == '-':
            positive = not positive
            accu = accu[1]
        S = S[1:]

    return "YES"
    
    

for t in range(T):
    L, X = [int(c) for c in input().strip().split()]
    base_S = input().strip()

    print("Case #%d: %s" % (t+1, solve(base_S, X)))
