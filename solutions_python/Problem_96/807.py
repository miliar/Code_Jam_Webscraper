with open("2.output","w") as op:
    with open("B-small-attempt0.in") as ip:
        whole=int(ip.readline().strip())
        case=0
        for line_at in range(whole):
            ele=ip.readline().strip().split(" ")
            dancers=int(ele[0])
            surp=int(ele[1])
            cut=int(ele[2])
            scores=map(int,ele[3:])
            maxim_num=0
            for i in scores:
                if i-3*cut+2>=0:
                    maxim_num+=1
                elif i-cut>0 and i-3*cut+4>=0 and surp>0:
                    maxim_num+=1
                    surp-=1
            print "Case #%s: "%(line_at+1)+str(maxim_num)
            op.write("Case #%s: "%(line_at+1)+str(maxim_num)+"\n")
