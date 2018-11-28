import sys
import time
import collections

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
            T = int(fin.readline())
            for t in range(1,1+T):
                N,K = map(int,fin.readline().split())

                answer = ((K+1) % (1 << N)) == 0
                print >> fout, "Case #%d: %s" % (t, 'ON' if answer else 'OFF')

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
