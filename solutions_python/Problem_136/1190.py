##Google Code Jam 2014
#Input File
file = open('B-large.in','r')       
#Output File
output = open('output.out','w')
print(output)

def val(line):
    vals = []
    l = ''
    for i in line:
        if i == ' ':
            vals.append(l)
            l = ''
        else:
            l += i
    vals.append(l)
    #print('vals of ',line, ' = ',vals)
    return vals
def solve():
    farms = 0
    max_t = X/2
    new_t = C/2 + X/(f+2)
    a_better_time = new_t<max_t
    old_t = max_t
    res_t = C/2
    while a_better_time:
        old_t = new_t
        farms += 1
        c_rate = farms*f + 2
        new_t = res_t + C/c_rate + X/(c_rate +f)
        res_t += C/c_rate
        a_better_time = new_t<old_t
    return min(new_t,old_t)

a = 1
t = int(file.readline())
while True:
    while a <= t:
        line = file.readline().strip('\n')
        line = val(line)
        C = float(line[0])
        f = float(line[1])
        X = float(line[2])
        #print('Case #%i:'%a+' '+str(solve())+'\n')
        output.write('Case #%i:'%a+' '+str(solve())+'\n')
        a+=1
    break
output.close()
#file.close()
