def main():
    input1 = open('input1.txt', 'r')
    output1 = open('output1.txt', 'w')

    T = int(input1.readline())      #number of test cases
    
    for casenum in xrange(1, T + 1):
        line = input1.readline().strip().split(' ')
        max_shyness = int(line[0])
        shyness = line[1];      #histogram of shyness. size = Smax+1
        shyness = [int(c) for c in shyness]
        to_add = 0
        
        standing_now = 0
        for i in xrange(max_shyness+1):
            if(shyness[i] == 0):
                continue
            elif(i <= standing_now):
                standing_now += shyness[i]
            else:
                to_add += (i - standing_now)
                standing_now = i + shyness[i]
        
        outstr = 'Case #' + str(casenum) + ': '
        outstr += str(to_add)
        outstr += '\n'
        output1.write(outstr)

    input1.close()
    output1.close()
  
    
    
main()