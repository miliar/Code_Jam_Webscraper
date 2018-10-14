import sys

def solve(infilename, outfilename):
    infile, outfile = open(infilename), open(outfilename, 'w')
    cases = int(infile.next().strip())
    for case in range(cases):
        P, K, L = [int(x) for x in infile.next().strip().split(' ')]
        howoften = [int(x) for x in infile.next().strip().split(' ')]
        howoften.sort(reverse=True)
        if P*K<L:
            outfile.write('Case #'+str(case+1)+': impossible\n')
            continue
        presses_all = 0
        presses_for_curr = 1
        count = 0
        while(len(howoften)>0):

            if count>=K:

                presses_for_curr += 1
                count = 0
            count +=1
            presses_all += howoften.pop(0)*presses_for_curr


        outfile.write('Case #'+str(case+1)+': '+str(presses_all)+'\n')

if __name__ == '__main__':
    solve(sys.argv[1], sys.argv[2])
