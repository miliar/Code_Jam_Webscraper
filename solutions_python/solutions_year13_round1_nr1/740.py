import sys
f=open(sys.argv[1],"r").read()
f_split=f.split("\n")

for i in range(1, int(f_split[0])+1):
    r_l=f_split[i].split(" ")
    radius=long(r_l[0])
    ml=long(r_l[1])
    count=0
    index=1
    while ml>0:
        vol_req = (2*radius + index)
        if vol_req<=ml:
            count+=1
            ml=ml-vol_req
            index+=4
        else:
            break
    print "Case #"+str(i)+": "+str(count)
