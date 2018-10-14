nums = range(2000000 + 1)
def reset():
    for i in range(2000000):
        nums[i] = 0


def n_recycled(line):
    reset()
    s = line.split()
    A = int(s[0])
    B = int(s[1])
    count = 0
    for i in range(A, B+1):
        if (nums[i] == 0):
            s_i = str(i)
            lnth = len(s_i)
            lst = []            
            nums[int(i)] = 1
            local_count = 0
            for k in range(1,lnth):
                t = s_i[lnth-k:] + s_i[:lnth-k]
                if (nums[int(t)] ==0 and int(t) != i and int(t) <= B and int(t) >= A and int(s_i[:lnth-k])!=0):
                    local_count +=1
                    nums[int(t)] = 1
                    
                    lst.append(int(t))
            count += sum(range(1,local_count+1))
    return count
            
        

f = open('C:\\C-small-attempt0.in')
f_out = open('C:\\res.txt','r+')
j = 0
n = 0
for line in f:
    if (j == 0):
        n = int(line)
        j = j + 1
        continue
    f_out.write("Case #"+str(j)+": "+str(n_recycled(line))+'\n')
    j = j + 1

f.close()
f_out.close()
