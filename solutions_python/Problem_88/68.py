import sys,time

def cumsum(L):
    res = [0]
    s = 0
    for x in L:
        s += x
        res.append(s)
    return res

def do_it(R,C,W):
    # calculate row cumulative sums
    RS = [cumsum(row) for row in W]
    # calculate square cumulative sums
    S = list(zip(*[cumsum(col) for col in zip(*RS)]))

    #print (W)
    #print (RS)
    #print (S)
    for k in range(min(R,C), 2, -1):
        #print("Trying k={}".format(k))
        for r in range(R-k+1):
            for c in range(C-k+1):
                #print("r={}, c={}".format(r,c))
                # left vs. right
                sl  = S[r+k//2][c+k]+S[r][c]
                sl -= S[r+k//2][c]  +S[r][c+k]
                sl -= W[r][c] + W[r][c+k-1]
                
                sr  = S[r+k][c+k]+S[r+(k+1)//2][c]
                sr -= S[r+k][c]  +S[r+(k+1)//2][c+k]
                sr -= W[r+k-1][c]+W[r+k-1][c+k-1]
                
                # top vs. bottom
                st  = S[r+k][c+k//2]+S[r  ][c]
                st -= S[r  ][c+k//2]+S[r+k][c]
                st -= W[r][c] + W[r+k-1][c]
                
                sb  = S[r+k][c+k]+S[r  ][c+(k+1)//2]
                sb -= S[r  ][c+k]+S[r+k][c+(k+1)//2]
                sb -= W[r][c+k-1]+W[r+k-1][c+k-1]

                #print("delta LR={}, delta TB={}".format(sl-sr, st-sb))
                if sl == sr and st == sb:
                    return k
    return "IMPOSSIBLE"
    
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
                R,C,D = [int(x) for x in fin.readline().split()]
                W = []
                for r in range(R):
                    W.append([int(x) for x in fin.readline().strip()])

                answer = do_it(R,C,W)
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
