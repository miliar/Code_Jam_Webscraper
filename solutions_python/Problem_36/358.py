import sys

filename = sys.argv[1]
#print "Using file", filename
input = open(filename, 'r')
outputname = filename[:-2] + "out"
output = open(outputname, 'w')

phrase = "welcome to code jam"

cases = int(input.readline())
#print cases, "test cases"
for case in range(1, cases + 1):
    output.write("Case #" + str(case) + ": ")
    #print "Case", case
    
    line = input.readline()
    
    def findfrom(x, pos):
        if (pos == len(phrase)):
            return 1
            
        total = 0
        idx = x
        count = 1
        while count != 0:
            idx = line.find(phrase[pos:pos+1], idx)
            if idx != -1:    
                idx += 1
                count = findfrom(idx, pos + 1)
                total = total + count
            else:
                return total
        return total
        
    num = findfrom(0, 0)
    print num
    outstr = str(num)[-4:].zfill(4)
    
    output.write(outstr + "\n")
            
    
input.close()
output.close()
