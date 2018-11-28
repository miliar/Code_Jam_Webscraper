from math import pi

#  def best(i, last, c=0):
#      if c == k: return 0
#      if last == -1:
#          opt1 = pi*p[i][0]**2 + best(i+1, i, c+1)
#          opt2 = best(i+1, -1, 0)
#
#      if p[last][0] >= p[i][0]:
#          opt1 = best(

def open(x):
    return 2*pi*x[0]*x[1] + pi*x[0]*x[0]

t = int(input())
for q in range(t):
    n, k = map(int, input().split())

    p = [list(map(int, input().split())) for i in range(n)]
    p.sort(key=lambda x: x[0]*x[1], reverse=True)

    using = p[:k] # k highest
    bestr = max(x[0] for x in using)

    best = -1
    besti = -1
    for i in range(k, len(p)):
        if p[i][0] >= bestr and open(p[i]) > best:
            best = open(p[i])
            besti = i

#      print("besti", besti)
    worst = min(x[0]*x[1] for x in using)
    update = pi*(p[besti][0]**2 - bestr**2) + 2*pi * p[besti][0] * p[besti][1] - 2*pi*worst

    if besti != -1 and update > 0:
        r = best
        for x in using:
            r += 2 * pi * x[0] * x[1]
        r -= 2*pi*worst
    else:
        r = 0
        for x in using:
            r += 2 * pi * x[0] * x[1]
        r += pi * bestr**2

    print("Case #{}: {:.9f}".format(q+1, r))
