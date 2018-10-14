of = open("output.txt",'w')
with open("A-large.in") as f:
    data = f.readlines()
    nb_Tc = int(data[0])
    for c in xrange(1,nb_Tc+1):
        d = data[c].split(' ')
        sl = int(d[0])
        snddd = 0
        sntv = 0
        for lv in xrange(sl+1):
            snoln = int(d[1][lv])
            if snoln:
                if snddd>=lv:
                    snddd+= snoln
                else:
                    sntv += lv - snddd
                    snddd = lv + snoln
        of.write('Case #'+str(c) + ': ' + str(sntv)+ '\n')

f.close()
of.close()
        
