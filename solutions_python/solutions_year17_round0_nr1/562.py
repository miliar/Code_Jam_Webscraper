
inp = open("A-large.in", "r")
out = open("output", "w")
tt = int(inp.readline())
for i in xrange(tt):
    a = inp.readline()
    a = a.split(" ")
    count = int(a[1])
    a = list(a[0])
    n = len(a)
    idx = 0
    ans = 0
    while idx < n:
        if a[idx] == '-':
            next_idx = idx + count
            flag = 0
            ans += 1
            for j in xrange(count):
                if (idx + count) > n:
                    idx = n
                    ans -= 1
                    break

                if a[idx + j] == '+':
                    a[idx + j] = '-'
                    if flag == 0:
                        next_idx = idx + j
                        flag = 1

                else:
                    a[idx + j] = '+'

            idx = next_idx

        else:
            idx += 1

    ans = str(ans)
    for j in xrange(n):
        if a[j] == '-':
            ans = 'IMPOSSIBLE'
            break

    out.write("Case #%d: %s \n" % (i+1, ans))

inp.close()
out.close()