def det_key(d,item):
    return d.keys()[d.values().index(item)]

def det_prev(l,end):
    count =0
    for i in xrange(end,-1,-1):
        if l[i]=="0":
            return count-1
        count+=1
def det_next(l,start):
    count = 0
    for i in xrange(start,len(l)):
        if l[i]=="0":
            #print l,i
            return count-1
        count+=1

def second_part(d,indexes):
    l = []
    for i in indexes:
        l.append(d[i])
    maxi = []
    maxi_val = 0
    index = 0
    for j in l:
        if max(j)==maxi_val:
            maxi.append(d.keys()[index])
        elif max(j)>maxi_val:
            maxi_val = max(j)
            maxi = [index]
        index+=1
    result = []
    ans = []
    for k in maxi:
        result.append(l[k])
    for m in result:
        ans.append(det_key(d,m))
    #print ans,"NS"
    return ans

def calc_pos(l):
    d = {i:[] for i in xrange(len(l))}
    ind = 0
    for k in l:
        if k=="0":
            d[ind] = [0,0]
        else:
            d[ind] = [det_prev(l,ind),det_next(l,ind)]
        ind+=1
    s = d.values()
    maxi = []
    maxi_val = 0
    index = 0
    for j in s:
        if min(j)==maxi_val:
            maxi.append(d.keys()[index])
        elif min(j)>maxi_val:
            maxi_val = min(j)
            maxi = [index]
        index+=1
    #print maxi
    if len(maxi)>1:
        second = second_part(d,maxi)
        #print second,"SEcond"
    else:
        return maxi[0]

    if len(second)>1:
        second.sort()
        return second[0]
    else:
        return second[0]


f = file("stalls-output-small.txt","w")
t = int(raw_input())
for case in xrange(1,t+1):
    n,k = map(int,raw_input().split())
    l = ["0"]
    for _ in xrange(n):
        l.append(".")
    l.append("0")
    for i in xrange(k-1):
        #print calc_pos(l)
        temp = calc_pos(l)
        l[temp]="0"
        if temp==0:
            break
        #print l
    if max(det_next(l,calc_pos(l)),det_prev(l,calc_pos(l)))+min(det_next(l,calc_pos(l)),det_prev(l,calc_pos(l))) == -2:
        print 0,0
        f.write("Case" + " #" + str(case) + ": " + str("0 0"))
    else:
        print str(max(det_next(l,calc_pos(l)),det_prev(l,calc_pos(l))))+" "+str(min(det_next(l,calc_pos(l)),det_prev(l,calc_pos(l))))
        f.write("Case" + " #" + str(case) + ": " + str(max(det_next(l,calc_pos(l)),det_prev(l,calc_pos(l))))+" "+str(min(det_next(l,calc_pos(l)),det_prev(l,calc_pos(l)))))
    f.write("\n")

f.close()
