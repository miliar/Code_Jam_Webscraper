import io
import math

def CalculateMax(data):
    s = data.split(' ')
    out = 0
    length  = len(s[0])
    A = int(s[0])
    B = int(s[1])
    dict = {}
    for i in range(A, B + 1):
        si = str(i)  
        for j in range(1,length):
            num = int(si[j:length] + si[0:j])
            if num >= A and num <= B and num != i:
                key = ''
                if i > num:
                    key = str(i) + str(num)
                else:
                    key = str(num) + str(i)
                dict[key] = 'a'
    out = len(dict.keys())            
    return str(out)        

fin = open('in', 'r')
fout = open('out', 'w')
j = 0
for line in fin:
    if (j > 0):
        out = CalculateMax(line)         
        fout.write('Case #' + str(j) + ': ' + out + '\n')        
    j = j + 1
fin.close()    
fout.close()


