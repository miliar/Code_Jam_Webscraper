import math as m


filename = r'c:\g\Q\A-test.in.txt'
filename = r'c:\g\Q\A-small-attempt0.in'
filename = r'c:\g\Q\A-large.in'
foutname=r'c:\g\Q\A-out.txt'

FILE = open(filename)
FOUT = open(foutname,"w")
T = int(FILE.readline())

def numguests(s,dbg):
    cum = 0
    invite = 0
    if dbg: print "numguests( s=",s,")", "len(s)=",len(s)
    #print [(x,y) for x,y in enumerate(s)]
    for pch,ch in enumerate(s):
        ich = int(ch) #0-9
        if dbg: print pch,ch,"cum,invite=",(cum,invite)
        if ich==0:  #nobody in this group
            if dbg: print "  skip"  
        elif cum>=pch:
                cum += ich # already enough standing for ich stand up
                if dbg: print "  add ",ich, "now cum=",cum
        else:
            addl = pch-cum #how many these people invite to be standing - how many already up
            invite += addl #invited guests
            cum += ich + addl
            if dbg: print "  invite ",addl," more, now cum,invite=",(cum,invite)
    return invite
#print numguests("1100120001",0),"needed"
dbg=0
if 1:
  for i in range(1,T+1):
    rawline = FILE.readline().split(' ')
    SMAX,s = int(rawline[0]), rawline[1]
    if s[-1]<'0': s=s[:-1] #strip lf on end
    if dbg: print "Case #" + str(i)+": SMAX=",SMAX,"len(s)=",len(s),s if len(s)<=100 else ""
    if dbg and len(s)>100: print "   s=",s[:100]+("..."+s[-3:] if len(s)>100 else "")

    msg = 'Case #' + str(i) + ': ' + str(numguests(s,0))
    if dbg: print msg
    if i%10==1: print msg
    FOUT.write(msg + "\n")
  print "finished",T,"cases."
FOUT.close()
