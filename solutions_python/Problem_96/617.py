



'''3-2-1-3'''
def solve(line):
    count = 0
    (N, suprise, par) = line.split(' ')[0:3]
    scores = line.split(' ')[3:]
    par = int(par)
    suprise = int(suprise)
    
#    print 'scores' + str(scores)
#    print 'surpris' + str(suprise)
#    print 'par' + str(par)
    
    
    for s in scores:
        if int(s)>=par:
            diff = par * 3 - int(s)
            if diff <= 0:
                count += 1
            elif diff <= 2:
                    count += 1
            elif diff <= 4 and suprise > 0:
                    suprise -= 1
                    count += 1
    
    return count
            
if __name__ == '__main__':
    file = open('input.txt')
    i = 1
    lines = file.readlines()
    lines = lines[1:]
    for line in lines:
        line = line.strip('\n')
        output = solve(line)
        print "Case #" + str(i) + ": " + str(output)
        i += 1
    pass
