import sys,time
import operator,functools

def xor_sum(L):
    return functools.reduce(operator.xor, L)

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
                N, = [int(x) for x in fin.readline().split()]
                C = [int(x) for x in fin.readline().split()]

                answer = 'NO' if xor_sum(C) else sum(C)-min(C)
                print("Case #{}: {}".format(case_idx, answer), file=fout)

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
