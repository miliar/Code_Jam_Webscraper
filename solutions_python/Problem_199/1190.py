from codejam import CodeJam

def testcase(f):
    (S, K) = f.readline().split()
    K = int(K)
    stack = [0] * (K-1)
    flips = 0
    for pancake in S[:1-K]:
        state = (stack.pop(0) + (pancake == '-')) % 2
        if state:
            stack = [s+1 for s in stack]
            stack.append(1)
            flips += 1
        else:
            stack.append(0)
    for pancake in S[1-K:]:
        if (stack.pop(0) + (pancake == '-')) % 2:
            return 'IMPOSSIBLE'
    return flips

cj = CodeJam(testcase)

# After importing cj into an interactive terminal, I test the code by
# running:
# >>> cj.processtext("""examples""")
#
# Then after downloading the problem set, I solve it with:
# >>> cj.processfile('filename')
