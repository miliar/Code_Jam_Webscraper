#### Problem A. Standing Ovation ####

# from math import sqrt, ceil, floor


# input
filename = "input"
lines = (line.rstrip('\n') for line in open(filename))
T = int(lines.__next__())

# output
output = open('output', 'w+')

# test case loop
for caseIdx in range(T):
    [smax, lvls] = lines.__next__().split(' ')
    smax = int(smax)
    lvls = list(map(int, list(lvls)))

    y = 0 # nr or friends necessary
    n = 0 # nr of people standing
    for i in range(smax+1):
      dy = max(0, i-n)
      y += dy
      n += dy + lvls[i]


    # print output
    msg = str(y)
    out = 'Case #' + str(caseIdx + 1) + ': ' + msg + '\n'
    output.write(out)
    # print(out)

output.close()
print(open('output', 'r').read())
