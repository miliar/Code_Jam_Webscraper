import sys,time
#import ...

start_time = time.time()
try:
    if len(sys.argv) > 1:
        inname = sys.argv[1]
    else:
        inname = input("Enter input filename: ")

    assert inname.endswith('.in')
    outname = inname.replace('.in', '.out')

    with open(inname) as fin:
        with open(outname, 'w') as fout:
            num_cases = int(fin.readline())
            for case_idx in range(1,1+num_cases):
                if time.time() >= start_time + 5:
                    print ("[== Case %d of %d ==]" % (case_idx, num_cases))
                line = fin.readline().split()
                N = int(line[0])
                R = line[1::2]
                P = [int(x) for x in line[2::2]]
               
                assert len(R) == len(P) == N
                assert all(1 <= x <= 100 for x in P)
                assert all(x in 'OB' for x in R)

                last_p = {'O':1, 'B':1}
                last_t = {'O':0, 'B':0}
                t = 0
                for i in range(N):
                    r,p = R[i],P[i]
                    distance = max(0, abs(p-last_p[r]) - (t-last_t[r]))
                    t += 1 + distance
                    last_t[r] = t
                    last_p[r] = p
                answer = t
                print("Case #%d: %d" % (case_idx, answer), file=fout)

except:
    import traceback
    print("Exception caught:", file=sys.stderr)
    print('-'*60, file=sys.stderr)
    traceback.print_exc(file=sys.stderr)
    print('-'*60, file=sys.stderr)
    input("Press Enter to close")
else:
    total_time = time.time() - start_time
    print("Completed in %.1f seconds" % total_time, file=sys.stderr)
    time.sleep(3)
