def run(a):
        f = file(a,"rb").read()
        o = []
        i = 0
        fs = f.split("\n")
        for l in fs[1:-1]:
                i += 1
        	ls = l.split(" ")
        	o.append("Case #" + str(i) + ": " + ison(int(ls[0]),int(ls[1])))
        f2 = file(a+".out","wb")
        f2.write("\n".join(o))
        f2.close()
