def timeSave(num,count):
    return num - count-(num+1)/2
def solver(instr):
    dic,top={},0
    for item in map(int,instr.split(' ')):
        if item not in dic:
            dic[item] = 0
        dic[item] += 1
    top = max(dic.keys())
    res = [top]
    adtime =0
    while top>0:
        count  = dic.pop(top)
        if top ==9 and count<2 and 5 not in dic and 7 not in dic:
            adtime += count * 2
            next = max(3,max(dic.keys()+[0]))
            res.append(adtime + next)
            dic[3]=dic.get(3,0)+3*count
            top = next
            continue
        next = max((top+1)/2,max(dic.keys()+[0]))
        if timeSave(top,count)<0:
            return min(res)
        else:
            adtime+=count
            res.append( adtime+next )
            dic[(top+1)/2] = dic.get((top+1)/2,0) + count
            dic[top/2] = dic.get(top/2,0)+ count
        top = next
    return min(res)

with open('3.in','r') as infile:
    n = int(infile.readline().strip())
    with open('1,out','w') as outfile:
        for i in range(n):
            infile.readline()
            outfile.write("Case #%d: %d\n" %(i+1,solver(infile.readline().strip())))

