glist = []
def parse (raw):
    for tc in range (0, int (raw.readline()[:-1])):
        tcdata = raw.readline()
        glist.append ( map(int, tcdata.split()[1]))
f=open ('friendlarge.in', 'rb')
parse(f)
count = 1

for list_ in glist:
    shyness_level = 0
    req =0
    total_count =0
    for elem in list_:
        sub=0
        if shyness_level == 0 or elem ==0:
            pass
        elif shyness_level > total_count:
            req += shyness_level-total_count
            sub = shyness_level-total_count
        total_count +=(elem + sub)
        shyness_level +=1
        
     
    print "Case #" + str(count) + ": " + str(req)
    count +=1
    
