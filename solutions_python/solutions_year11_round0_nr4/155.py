def main():
    inpfile = open("D-large.in", 'r')
    outfile = open('outfile', 'w')
    casenum = int(inpfile.readline().strip())
    for case in range(1, casenum + 1):
        line = inpfile.readline().strip()
        line2 = inpfile.readline().strip().split()
        numelem = int(line)
        x = 0
        l = line2[:]
        while x < len(line2):
            l[x] = int(line2[x])
            x += 1
        print numelem
        print l
        
        sortedl = l[:]
        sortedl.sort()
        i = 0
        counter = 0
        while i < numelem:
            if l[i] != sortedl[i]:
                counter += 1
            i += 1
        
        
        result = "Case #" + str(case) + ": " + str(counter) + ".000000\n"
        outfile.write(result)
    inpfile.close()
    outfile.close()

    
if __name__ == "__main__":
    main()
    
