def Intersect(w1,w2):
    if (w1[0] < w2[0] and w1[1] > w2[1]):
        return 1
    if (w1[0] > w2[0] and w1[1] < w2[1]):
        return 1  
    return 0

if __name__ == '__main__':
    #in_file = 'testA.txt'
    #in_file = 'A-small-attempt0.in'
    in_file = 'A-large.in'
    out_file = 'res'
    

    lines = open(in_file).readlines()
    lines = lines[1:]
    case = 0

    wfile = open(out_file, 'w')

    while lines:
        case += 1
        n = lines[0].strip()
        n = int(n)

        lines = lines[1:]
        wires = list()
        s = 0
        
        for line in lines[:n]:
            l = line.strip().split()
            l = [ int(x) for x in l]
            wires.append(l)
        
        
        for i in range(len(wires)-1):
            for j in range((i+1),len(wires)):
                s = s + Intersect(wires[i],wires[j])

        

        wfile.write('Case #' + str(case) + ': ')
        wfile.write(str(s) + '\n')
        
        lines = lines[n:]

        
    wfile.close()