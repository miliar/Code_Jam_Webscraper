def owp(mp, i):
    j = 0
    z = 0.0
    m = 0
    while j < len(mp):
        if j != i and mp[j] != '.':
            if mp[j] == '1':
                z += 1
            m += 1
        j += 1
    if m == 0:
        return 0
    return z/m

def main():
    inpfile = open("A-large.in", 'r')
    outfile = open('outfile', 'w')
    casenum = int(inpfile.readline().strip())
    for case in range(1, casenum + 1):
        line1 = inpfile.readline().strip()
        n = int(line1)
        mp = []
        wplst = []
        owplst = []
        owptemp = []
        oowptemp = []
        oowplst = []
        for i in range(n):
            line = inpfile.readline().strip()
            z = 0.0
            m = 0
            for x in line:
                if x == '1':
                    z += 1
                if x != '.':
                    m += 1
            wplst.append(z/m)
            mp.append(line)
        #print mp
        #print wplst
        i = 0
        while i < n:
            j = 0
            while j < n:
                if mp[i][j] != '.':
                    owptemp.append(owp(mp[j],i))
                j += 1
            owplst.append(sum(owptemp)/len(owptemp))
            owptemp = []
            i += 1
        #print owplst
        i = 0
        while i < n:
            j = 0
            while j < n:
                if mp[i][j] != '.':
                    oowptemp.append(j)
                j += 1
            z = 0.0
            #print oowptemp
            m = len(oowptemp)
            for x in oowptemp:
                z += owplst[x]
            oowplst.append(z/m)
            i += 1
            oowptemp = []
        #print oowplst
            
        result = "Case #" + str(case) + ": " + "\n"
        outfile.write(result)
        for i in range(n):
            result = str(0.25 * wplst[i] + 0.50 * owplst[i] + 0.25 * oowplst[i]) + '\n'
            outfile.write(result)
    inpfile.close()
    outfile.close()

    
if __name__ == "__main__":
    main()
    
