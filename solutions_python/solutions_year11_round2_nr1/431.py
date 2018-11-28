def main():

    inputfile = file('A-large.in', 'r')
    outputfile = file('output', 'w')
    currentcase = 1
    totalcase = int(inputfile.readline().strip())
    while currentcase <= totalcase:
        totalteam = int(inputfile.readline().strip())
        currentteam = 0
        l = []
        lowp = []
        lwp = []
        while currentteam < totalteam:
            l.append(inputfile.readline().strip())
            currentteam += 1
        output = "Case #%d:\n"%currentcase
        for i in range(0, totalteam):
            wp = l[i].count('1')/float(l[i].count('0')+l[i].count('1'))
            lwp.append(wp)
            owp = fowp(l, i)
            lowp.append(owp)
        for i in range(0, totalteam):
            wp = lwp[i]
            owp = lowp[i]
            index = 0
            soowp = 0
            t = 0
            while index < len(lowp):
                if l[i][index] != '.':
                    soowp += lowp[index]
                    t += 1
                index += 1
            oowp = soowp/float(t)
            output += "%f\n"%(0.25 * wp + 0.50 * owp + 0.25 * oowp)
        outputfile.write(output)
        currentcase += 1
    inputfile.close()
    outputfile.close()
    
def fowp(l, tnumber):
    current = 0
    wp = 0
    totalteam = 0
    while current < len(l):
        if current != tnumber and l[current][tnumber] != '.':
            totalteam += 1
            i = 0
            w = 0
            total = 0
            while i < len(l[current]):
                if i != current and i != tnumber:
                    if l[current][i] != '.':
                        if l[current][i] == '1':
                            w += 1
                        total += 1
                i += 1
            if total != 0:
                wp += float(w)/total
        current += 1
    return float(wp)/totalteam
            
            
            

if __name__ == '__main__':
    main()