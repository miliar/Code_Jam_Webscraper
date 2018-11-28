f = open('2.in')
out = open('1-out', 'w')
t = int(f.readline())
case = 1
for i in range(t):
    (r, c, w) = [int(x) for x in f.readline().strip().split()]
    res = 0
    res = res + c//w
    res = res + w - 1
    if c%w > 0:
        res = res + 1
    res = res*r
    out.write('Case #' + str(case) + ': ' + str(res) + '\n')
    case = case + 1
out.close()
