# File input
#input = open('H:/winprofile/desktop/a.in','r')
input = open('C:/Users/Asus/Desktop/a.in','r')
outputString = ""

#Define function

            
# Calculation
import math
numCase = int(input.readline().replace('\n',''))
for i in range(1,numCase+1):
    line = input.readline().replace('\n','').split(' ')
    radius = long(line[0])
    paint = long(line[1])
    b = float(2 * radius - 1)
    n = (-b + math.sqrt(b*b+8*paint))/4
    ans = long(math.floor(n))
    if b * ans >= paint:
        ans = ans - 1
    outputString = outputString + 'Case #' + str(i) + ': ' + str(ans) + '\n'


#File output
#output = open('H:/winprofile/desktop/a.out','w')
output = open('C:/Users/Asus/Desktop/a.out','w')
output.write(outputString)
input.close()
output.close()
