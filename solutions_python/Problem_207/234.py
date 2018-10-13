import sys

def maxind(els):
    return els.index(max(els))

def getchoices(els, strings, nowi, dd):
    return sorted([dd[ns] for ns in CAN[strings[nowi]] if els[dd[ns]]], key=lambda x: els[x])


# def dfs(N, R, Y, B):
#     # For small input.

#     # Data
#     els = [R, Y, B]
#     strings = 'RYB'
#     s2ind = dict((s,i) for i,s in enumerate(strings))

#     # Add first horse (can be whatever).
#     ibest = maxind(els)
#     els[ibest] -= 1
#     S = strings[ibest]

#     stack = [(els, S)]
#     while stack:
#         els, S = stack.pop()

#         if len(S) == N:
#             if verify(S):
#                 return S

#         choices = getchoices(els, strings, nowi, s2ind)

#         for i in choices:
#             elss = list(els)
#             elss[i] -= 1
#             stack.append((elss, S + strings[i]))
#     return 'IMPOSSIBLE'


def is_impossible(R, O, Y, G, B, V):
    Rs = R + V + O
    Bs = B + V + G
    Ys = Y + O + G

    N = sum([R, O, Y, G, B, V])

    if max(Rs, Bs, Ys) >= (N / 2 + 2):
        return True
    return False


def dfs(N, R, O, Y, G, B, V):
    # For large input.

    # Rule out:
    Rs = R + V + O
    Bs = B + V + G
    Ys = Y + O + G
    if max(Rs, Bs, Ys) > float(N / 2):
        return 'IMPOSSIBLE'

    # Data
    els = [R, O, Y, G, B, V]
    strings = 'ROYGBV'
    s2ind = dict((s,i) for i,s in enumerate(strings))

    # Add first horse (can be whatever).
    ibest = maxind(els)
    els[ibest] -= 1
    S = strings[ibest]

    stack = [(els, S)]
    while stack:
        els, S = stack.pop()

        if len(S) == N:
            if verify(S):
                return S
        if is_impossible(*els):
            continue

        nowi = s2ind[S[-1]]
        choices = getchoices(els, strings, nowi, s2ind)

        for i in choices:
            elss = list(els)
            elss[i] -= 1
            stack.append((elss, S + strings[i]))
    return 'IMPOSSIBLE'



def solve(N, R, O, Y, G, B, V):
    return dfs(N, R, O, Y, G, B, V)

CAN = {
    'R': set(['Y', 'B', 'G']),
    'O': set(['B']),
    'Y': set(['R', 'B', 'V']),
    'G': set(['R']),
    'B': set(['R', 'Y', 'O']),
    'V': set(['Y']),
}

def verify(s):
    prev = s[0]

    if len(s) == 1:
        return True

    for i,next_ in enumerate(s[1:]):
        if next_ not in CAN[prev]:
            #print 'Fail:', prev, 'and', next_, 'at positions', i-1, i
            return False
        prev = next_

    # Test first-last.
    if s[-1] not in CAN[s[0]]:
        #print 'Fail:', s[0], 'and', s[-1], 'at positions', 0, len(s)-1
        return False

    return True


def main():
    T = int(sys.stdin.readline().strip())

    for i in xrange(T):
        N, R, O, Y, G, B, V = map(int, sys.stdin.readline().split())
        # print 'Solving:', N, R, O, Y, G, B, V
        ans = solve(N, R, O, Y, G, B, V)
        if ans != 'IMPOSSIBLE':
            assert verify(ans)
        print 'Case #%s: %s' % (i+1, ans)

if __name__ == '__main__':
    main()
