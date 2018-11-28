# Enter your code here. Read input from STDIN. Print output to STDOUT
t = int(raw_input())  # read a line with a single integer
for i in xrange(1, t + 1):
    row = raw_input().split(' ')  # read a list of integers, 2 in this case
    s, k = list(row[0]), int(row[1])
    flips = 0
    for j in xrange(0, len(s) - k + 1):
        el = s[j]
        if el == '-':
            flips += 1
            el = '+'
            for n in xrange(0, k):
                if s[n + j] == '-':
                    s[n + j] = '+'
                else:
                    s[n + j] = '-'
    if ''.join(s) == '+'*len(s):
        ans = flips
    else:
        ans = "IMPOSSIBLE"
               
    print "Case #{}: {}".format(i, ans)
