from codejam import CodeJam

def testcase(f):
    (D, N) = [int(i) for i in f.readline().split()]
    slowest = 0
    for _ in range(N):
        (K, S) = [int(i) for i in f.readline().split()]
        t = (D - K) / S
        slowest = max(slowest, t)
    return '{:0.7f}'.format(D / slowest)


    

    


cj = CodeJam(testcase)

# After importing cj into an interactive terminal, I test the code by
# running:
# >>> cj.processtext("""examples""")
#
# Then after downloading the problem set, I solve it with:
# >>> cj.processfile('filename')
