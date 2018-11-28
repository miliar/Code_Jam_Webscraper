import tkFileDialog
import sys

def calc(played, won, results, i, j):
    p = played[i]
    w = won[i]
    if j is not None:
        if results[i][j] == '1':
            p -= 1
            w -= 1
        if results[i][j] == '0':
            p -= 1
    if (p == 0):
        return float(0.0)
    else: 
        return float(w) / p

def main():
    infile = (len(sys.argv) > 1 and sys.argv[1]) or tkFileDialog.askopenfilename(title="Select input file", initialdir='.', filetypes = [('Input','.in')])
    outfile = infile.replace(".in", ".out", 1);
    print "Output file will be: %s" % outfile
    of = open(outfile, "w")
    with open(infile, "r") as f:
        line = f.readline()
        noCases = int(line)
        print "Number of test cases: %d" % noCases 
        caseNo = 1
        while caseNo <= noCases:
            line = f.readline()
            N = int(line)
            print("N: %d" % N)
            won = []
            played = []
            opposition = []
            wp = []
            results = []
            for i in range(N):
                won.append(0)
                played.append(0)
                opposition.append([])
                line = f.readline()
                for j in range(N):
                    if line[j] == '0':
                        played[i] += 1
                        opposition[i].append(j)
                    else:
                        if line[j] == '1':
                            played[i] += 1
                            won[i] += 1
                            opposition[i].append(j)
                if (played[i] == 0):
                    wp.append(float(0.0))
                else: 
                    wp.append(float(won[i]) / played[i])
                results.append(line)
            output = ""
            lnwp = []
            lowp = []
            for i in range(N):
                nwp =calc(played, won, results, i, None)
                lnwp.append(nwp)
                owp = float(0.0)
                print opposition[i]
                for j in opposition[i]:
                    owp += calc(played, won, results, j, i)
                print owp
                if (len(opposition[i]) > 0):
                    owp /= len(opposition[i])
                print owp
                lowp.append(owp)
#                oo = []
#                for j in opposition[i]:
#                    oo.extend(opposition[j])
#                ooset = set(oo)
#                ooset.remove(i)
#                oowp = float(0.0)
#                print "ooset: %s" % ooset
#                for j in ooset:
#                    oowp += calc(played, won, results, j, i)
#                if (len(ooset) > 0):
#                    oowp /= len(ooset)
#                rpi = (0.25 * nwp) + (0.5 * owp) + (0.25 * oowp) 
#                output += "%0.12f\n" % rpi
#                print "wp: %f, owp: %f, oowp: %f" % (nwp, owp, oowp)
            for i in range(N):

                oowp = float(0.0)
                for j in opposition[i]:
                    oowp += lowp[j]
                if (len(opposition[i]) > 0):
                    oowp /= len(opposition[i])
                rpi = (0.25 * lnwp[i]) + (0.5 * lowp[i]) + (0.25 * oowp) 
                output += "\n%0.12f" % rpi
                print "wp: %f, owp: %f, oowp: %f" % (nwp, owp, oowp)
        
            print "Output: %s" % output
            of.write("Case #%d:%s\n" % (caseNo, output))
            caseNo += 1
    of.close()
    
        
if __name__ == '__main__':
    main()