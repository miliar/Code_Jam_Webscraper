def calc(n):
    if len(n) == 1:
        return n[0]
    for i in range(len(n)-1, 0, -1):
        if n[i] >= n[i-1]:
            continue
        ii = i
        while ii < len(n) and n[ii] != 9:
            n[ii] = '9'
            ii += 1
        n[i-1] = decr(n[i-1])

    # print n
    if n[0] == '0':
        return "".join(n[1:])

    return "".join(n)

def decr(ni):
    if ni == '0':
        return '9'
    return chr(ord(ni) - 1)

def main():
    inpfile = open("B-large.in", 'r')
    outfile = open('output', 'w')
    casenum = int(inpfile.readline().strip())
    for case in range(1, casenum + 1):
        line = inpfile.readline().strip()
        # linelst = line.split()
        
        n = [''] * len(line)
        i = 0
        for c in line:
            n[i] = c
            i += 1
        ret = calc(n)
        
        result = "Case #" + str(case) + ": " + str(ret)+"\n"
        print result
        outfile.write(result)
    inpfile.close()
    outfile.close()




if __name__ == "__main__":
    
    main()
    
