##Google Code Jam 2015
#Input File
file = open('A-large.in','r')       
#Output File
output = open('output.out','w')

#Functions
def val(line):
    vals = []
    l = ''
    for i in range(0,len(line)):
        if line[i] == ' ':
            vals.append(l)
            l = line[i+1:]
            break
        else:
            l += line[i]
    vals.append(l)
    return vals

#test cases
t = int(file.readline())
for i in range(0,t):
    case = val(file.readline().strip('\n'))
    s_max = int(case[0])
    aud = case[1]
    y = 0
    s = 0
    for j in range(0,s_max+1):
        s += int(aud[j])
        if s>=s_max:
            break
        else:
            if s>j:
                j+=1
            else:
                y+=1
                s+=1
                j+=1
    c = i +1
    output.write('Case #%i:'%c +' '+str(y)+'\n')

output.close()
file.close()
