#!/usr/bin/python

def magika(st, result, clist, rlist):
    if st == '':
        return result
    result.append(st[0])
    combine(result, clist)
    repel(result, rlist)
    return magika(st[1:], result, clist, rlist)

def combine(result, clist):
    if len(result) < 2:
        return

    for c in clist:
        if result[-1] == c[0] and result[-2] == c[1]:
            result.pop()
            result.pop()
            result.append(c[2])
        else:
            if result[-1] == c[1] and result[-2] == c[0]:
                result.pop()
                result.pop()
                result.append(c[2])

def repel(result, rlist):
    if len(result) < 2:
        return

    for r in rlist:
        if r[0] in result and r[1] in result:
            while len(result):
                result.pop()

if __name__ == '__main__':
    test_cases = int(raw_input())
    for case in range(1, test_cases + 1):
        parts = raw_input().split()
        clist_len = int(parts[0])
        clist = []
        for i in range(1, clist_len + 1):
            clist.append(parts[i])
        rlist_len = int(parts[clist_len + 1])
        rlist = []
        for i in range(clist_len + 1 + 1, clist_len + 1 + rlist_len + 1):
            rlist.append(parts[i])
        st = parts[clist_len + 1 + rlist_len + 1 + 1]
        result = []
        print 'Case #' + str(case) + ': [' + ', '.join(magika(st, result, clist, rlist)) + ']'

