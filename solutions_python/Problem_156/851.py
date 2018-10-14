def optimize(inp):
#    print inp
    best = max(inp)
    for top in range(1, max(inp)):
        moves = 0
        for val in inp:
            if val > top:
                if val % top == 0:
                    moves += (val / top) - 1
                else:
                    moves += val / top
#        print "top={}, moves={}".format(str(top), str(moves))
        best = min(best, moves + top)
    return best



def run(testN):
    nums = input()
    vals = map(int, raw_input().split())
    best = optimize(vals)
    print "Case #" + str(testN) + ": " + str(best)
    return


testCases = input()
for case in range(testCases):
    run(case + 1)
