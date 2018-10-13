from codejam import CodeJam

def testcase(f):
    N = [int(digit) for digit in f.readline().strip()]
    for pos in range(len(N)-1):
        if N[pos] > N[pos+1]:
            break
    else:
        return int(''.join(str(n) for n in N))
    for pos in range(pos, 0, -1):
        if N[pos] > N[pos-1]:
            break
    else:
        pos = 0
    N[pos] -= 1
    N[pos+1:] = [9 for _ in N[pos+1:]]
    return int(''.join(str(n) for n in N))
            

cj = CodeJam(testcase)

# After importing cj into an interactive terminal, I test the code by
# running:
# >>> cj.processtext("""examples""")
#
# Then after downloading the problem set, I solve it with:
# >>> cj.processfile('filename')
