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
                # read combinations
                C, line = int(line[0]), line[1:]
                comb = {}
                for i in range(C):
                    xyz, line = line[0],line[1:]
                    x,y,z = xyz
                    comb[x+y] = comb[y+x] = z
                # read opposite
                D, line = int(line[0]), line[1:]
                opp = {}
                for i in range(D):
                    xy, line = line[0],line[1:]
                    x,y = xy
                    opp.setdefault(x, set())
                    opp.setdefault(y, set())
                    opp[x].add(y)
                    opp[y].add(x)
                # read N
                N, line = int(line[0]), line[1:]
                inv, = line

                BASE = 'QWERASDF'
                assert all(x in BASE for x in inv)

                el = ""
                for x in inv:
                    el += x
                    while el[-2:] in comb:
                        el = el[:-2] + comb[el[-2:]]
                    if el[-1] in opp and opp[el[-1]] & set(el):
                        el = ""
                
                answer = '['+", ".join(el)+']'
                print("Case #%d: %s" % (case_idx, answer), file=fout)

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
