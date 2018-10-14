#!/usr/bin/python

t = int(raw_input())
for i in xrange(t):
    l = raw_input().split()

    n_combine = int(l[0])
    combine = l[1 : 1+n_combine]
    n_oppose = int(l[1+n_combine])
    oppose = l[2+n_combine : 2+n_combine+n_oppose]
    string = l[-1]

    c = {chr(x): {} for x in range(ord('A'), ord('Z')+1)}
    o = {chr(x): {} for x in range(ord('A'), ord('Z')+1)}

    for x in combine:
        c[x[0]][x[1]] = x[2]
        c[x[1]][x[0]] = x[2]

    for x in oppose:
        o[x[0]][x[1]] = True
        o[x[1]][x[0]] = True

    gc = {chr(x): 0 for x in range(ord('A'), ord('Z')+1)}

    stack = []
    for x in string:
        stack.append(x)
        gc[x] += 1

        while (len(stack) > 1):
            if stack[-1] in c[stack[-2]]:
                a = stack.pop()
                b = stack.pop()
                new = c[a][b]
                stack.append(new)

                gc[a] -= 1
                gc[b] -= 1
                gc[new] += 1
            else:
                break
        for y in o[stack[-1]].keys():
            if gc[y] > 0:
                stack = []
                gc = {chr(x): 0 for x in range(ord('A'), ord('Z')+1)}

    print("Case #%d: [%s]" % (i+1, ', '.join(stack)))



