__author__ = 'yurychebiryak'

# Input
#
# 4
# 1
# 0.5
# 0.6
# 2
# 0.7 0.2
# 0.8 0.3
# 3
# 0.5 0.1 0.9
# 0.6 0.4 0.3
# 9
# 0.186 0.389 0.907 0.832 0.959 0.557 0.300 0.992 0.899
# 0.916 0.728 0.271 0.520 0.700 0.521 0.215 0.341 0.458
#
#
#
# Output
#
# Case #1: 0 0
# Case #2: 1 0
# Case #3: 2 1
#Case #4: 8 4

def solve(n, Naomi, Ken):
    N = Naomi.copy()
    K = Ken.copy()
    fair = 0
    while len(N):
        m = max(N)
        higher = { x for x in K if x > m}
        if len(higher):
            K.remove(min(higher))
            fair+=1
        N.remove(m)
    deceitful = 0
    N = Naomi.copy()
    K = Ken.copy()
    while len(N):
        if min(N) < min(K): #need to trade up the smallest block for his heaviest
            N.remove(min(N))
            K.remove(max(K))
            deceitful+=1
        else: #can score by declaring a too high weight and trading min(N) for min(K)
            N.remove(min(N))
            K.remove(min(K))
    return n-fair, n-deceitful


def run(input, output):
    file = open(input, 'r')
    out = open(output, 'w')
    lines = file.readlines()
    for i in range(int(lines[0].strip())):
        n = int(lines[i * 3 + 1].strip())
        Naomi   = { float(x) for x in lines[i*3 + 2].split(" ") }
        Ken     = { float(x) for x in lines[i*3 + 3].split(" ") }
        fair, deceitful = solve(n, Naomi, Ken)
        out.write("Case #%d: %d %d\n" % (i+1, deceitful, fair))
        print("Case #%d: %d %d\n" % (i+1, deceitful, fair))

run("example.txt", "exampleOut.txt")
run("smallD.txt", "smallOut.txt")
run("largeD.txt", "largeOut.txt")
