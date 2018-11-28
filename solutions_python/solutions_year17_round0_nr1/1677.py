
def solve():
    dicks = raw_input().split()
    num_flips = int(dicks[1])
    cakes = list(dicks[0])
    tots = 0
    for i in range(len(cakes) - num_flips + 1):
        if cakes[i] == "-":
            tots += 1
            for j in range(num_flips):
                if cakes[i + j] == "-":
                    cakes[i + j] = "+"
                else:
                    cakes[i + j] = "-"
    i += 1
    while i < len(cakes):
        if cakes[i] == "-":
            return "IMPOSSIBLE"
        i += 1
    return tots

num_tests = int(raw_input())

for K in range(num_tests):
    print "Case #" + str(K + 1) + ": " + str(solve())
