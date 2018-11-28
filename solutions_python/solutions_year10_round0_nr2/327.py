import sys
import time
import fractions

start_time = time.time()
try:
    if len(sys.argv) > 1:
        inname = sys.argv[1]
    else:
        inname = raw_input("Enter input filename: ")

    assert inname.endswith('.in')
    outname = inname.replace('.in', '.out')

    with file(inname) as fin:
        with file(outname, 'w') as fout:
            C = int(fin.readline())
            for c in range(1,1+C):
                tmp = map(int,fin.readline().split())
                N,t = tmp[0], tmp[1:]
                assert len(t) == N
                #assert len(set(t)) == N, "%d %r" % (N,t)

                y = min(t)
                T = reduce(fractions.gcd, (x-y for x in t))
                answer = (T-y)%T
                print >> fout, "Case #%d: %d" % (c, answer)

except:
    import traceback
    print >> sys.stderr, "Exception caught:"
    print >> sys.stderr, '-'*60
    traceback.print_exc(file=sys.stderr)
    print >> sys.stderr, '-'*60
    raw_input("Press Enter to close")
else:
    total_time = time.time() - start_time
    print >> sys.stderr, "Completed in %.1f seconds" % total_time
    time.sleep(3)
