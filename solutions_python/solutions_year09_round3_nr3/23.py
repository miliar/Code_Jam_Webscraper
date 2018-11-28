f=open('1.txt','r')
inp = f.readlines()
t = inp[0].strip()
dic = {}
def find_min(cells,rel):
    cells = int(cells)
    rel = [int(elem) for elem in rel]
    if dic.has_key(str(cells)+str(rel)):
        return dic[str(cells)+str(rel)]
    elif rel == []:
        return 0
    else:
        o_min = min(
            [int(cells)-1+
             find_min(elem-1,rel[:rel.index(elem)])+
             find_min(cells-elem,[
                 e-elem for e in rel[rel.index(elem)+1:]])
            for elem in rel])
        dic[str(cells)+str(rel)]=o_min
        return o_min
        pass
for i in range(0,int(t)):
    [cells, releases] = [int(elem) for elem in inp[2*i+1].strip().split(' ')]
    rel = [int(elem) for elem in inp[2*i+2].strip().split(' ')]
    print "Case #%d: %d" % (i+1,find_min(cells,rel))
f.close()
