import copy

def solve(matrix):
    rpi = []
    wp = {}
    wp_other = {}
    owp = {}
    oowp = {}
    #wp
    for j, line in enumerate(matrix):
        wp_other[j] = {}
        temp_count = {}
        temp_total = {}
        count = total = 0.0
        for i, s in enumerate(line):
            if s == '1':
                count += 1
            if s != '.':
                total += 1
        wp[j] = count/total
        for i, s in enumerate(line):
            if s != '.':
                #print s, count, total
                wp_other[j][i] = (count-int(s))/(total-1)
        
        #print line, w, total
    #owp
    for j, line in enumerate(matrix):
        count = total = 0.0
        for i, s in enumerate(line):
            if s != '.':
                total += wp_other[i][j]
                count += 1
        #print "t, c:", total, count
        owp[j] = total/count
    #oowp
    for j, line in enumerate(matrix):
        count = total = 0.0
        for i, s in enumerate(line):
            if s != '.':
                total += owp[i]
                count += 1
        #print "t, c:", total, count
        oowp[j] = total/count
        
        #print copyowp
    '''
    print "wp", wp
    print "wp_other", wp_other
    print "owp", owp
    print "oowp", oowp
    '''
    #rpi
    for i in range(len(matrix)):
        rpi.append(str(wp[i]*0.25+owp[i]*0.5+oowp[i]*0.25))
    
    return rpi
                
input = open('A-large.in', 'r')
output = open('a.out', 'w')

t = int(input.readline())
for case in range(1, t+1):
   
    n = int(input.readline())

    matrix = []
    for n in range(n):
        line = input.readline().strip()
        matrix.append(line)

    #print matrix
    
    result = solve(matrix)

    print 'Case #'+str(case)+':', result
    #print
    output.write("Case #%s:\n" %(case))
    for line in result:
        output.write(line+"\n")
