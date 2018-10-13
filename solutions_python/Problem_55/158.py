import sys
import time

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
                R,k,N = map(int,fin.readline().split())
                g = tuple(map(int,fin.readline().split()))
                assert len(g) == N
                assert all(1 <= x <= k for x in g)

                # all cyclic shifts
                G = [g[i:] + g[:i] for i in range(N)]

                history = []
                revenue = []
                H = set()
                i = 0
                while True:
                    H.add(i)
                    history.append(i)
                    j = max(j for j in range(1,1+N) if sum(G[i][:j])<=k)
                    revenue.append(sum(G[i][:j]))
                    i = (i+j)%N
                    if i in H: break
                a = history.index(i)
                b = len(history)-a
                    
                if R < a:
                    answer = sum(revenue[:R])
                else:
                    u,v = divmod(R-a, b)
                    answer = sum(revenue[:a+v]) + sum(revenue[a:]) * u

                #print history
                #print revenue
                #print a,b,answer
                print >> fout, "Case #%d: %d" % (t, answer)

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
