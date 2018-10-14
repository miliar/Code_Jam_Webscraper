#codejam 4/10/15
#dijkstra
import math as m
import time

filename = r'c:\g\Q\C-test.in.txt'
#filename = r'c:\g\Q\C-small-attempt0.in'
filename = r'c:\g\Q\C-large.in'
foutname = r'c:\g\Q\C-out.txt'
foutname = r'c:\g\Q\C-out-large.txt'

FILE = open(filename)
FOUT = open(foutname,"w")
T = int(FILE.readline())

multbl=[["-1","k","-j"],["-k","-1","i"],["j","-i","-1"]]
multbl2=[[("1",1),("k",0),("j",1)],[("k",1),("1",1),("i",0)],[("j",0),("i",1),("1",1)]]
if 0:#check multbl2 by showing table
    print "    i   j   k"
    for r1 in "ijk":
        d1=r1+": "
        for c1 in "ijk":
            e1,e2 = multbl2[ord(r1)-ord("i")][ord(c1)-ord("i")]
            d1 += ("-" if e2 else " ") + e1 + "  "
        print d1
if 0:
  def mul0(aa): #two strings with 1 letter each like ijk, no minus, no 1
    if len(aa)<>2: raise "aa="+aa
    return multbl[ord(aa[0])-ord("i")][ord(aa[1])-ord("i")]

  def mul1(aa): #strings like above but may contain 1
    if len(aa)<>2: raise aa
    if aa[0]=="-": return aa #-1, -i, -j, -k
    if aa[0]=="1": return aa[1]
    if aa[2]=="1": return aa[0]
    return mul0(aa)

def mul2(aa): #string that can start with - and be of any length, but must have only ijk
    if len(aa)<=1: return aa
    if aa[0]=="-":
        t = mul2(aa[1:])
        if t[0]=="-": return t[1:] #minus x minus = plus
        return "-"+t
    #aa is not minus:
    cum,isneg="1",0
    for ch in aa:
        if cum=="1":
            cum = ch #same sign
        else:
            cum,isneg2 = multbl2[ord(cum)-ord("i")][ord(ch)-ord("i")]
            isneg = isneg ^ isneg2
    return ("-" if isneg else "") + cum
#print mul2("iiiii")


#find all positions at which stuff to left reduces to i
def findi(s,dbg):
    """Returns list of positions r where r[m] means s[0:m+1] reduces to i"""
    if dbg: print "input: ",s
    ret=[]
    cum,isneg = "1",0 #isneg = sign of the cumulative so far, 0 or 1
    for pch,ch in enumerate(s):
        if dbg: print "pch,ch=",(pch,ch)," cum,isneg=",(cum,isneg)
        if cum=="1":
            cum = ch #1*x = x, -1*x = -x (preserve sign: isneg unchanged)
        else:
            cum,isneg2 = multbl2[ord(cum)-ord("i")][ord(ch)-ord("i")]
            isneg = isneg ^ isneg2 #multiply signs (with xor)
        if dbg: print " cum2,isneg2=",(cum,isneg),"="+(" -"[isneg])+cum
        if isneg==0 and cum=="i": ret += [pch]
    return ret
#print findi("iiiii",0),"expect 0,4"
#print findi("jjjjjjjjjjjjjjjjjjjjjjjj",0)

#find all positions at which stuff to right reduces to k
def find_right_k(s,dbg):
    """returns list of positions (numbering 0 as rightmost character) where all characters to the right reduce to k"""
    if dbg: print "input: ",s
    ret=[]
    cum,isneg = "1",0 #isneg = sign of the cumulative so far, 0 or 1 -- this is kind of the output of the null string on right end
    for pch,ch in enumerate(s[::-1]): #pch here is 0 for right-most character
        if dbg: print "pch,ch=",(pch,ch)," cum,isneg=",(cum,isneg)
        if cum=="1":
            cum = ch #1*x = x, -1*x = -x (preserve sign: isneg unchanged)
        else:
            cum,isneg2 = multbl2[ord(ch)-ord("i")][ord(cum)-ord("i")]
            isneg = isneg ^ isneg2 #multiply signs (with xor)
        if dbg: print " cum2,isneg2=",(cum,isneg),"="+(" -"[isneg])+cum
        if isneg==0 and cum=="k": ret += [pch]
    return ret
#print findk("k",1)
#print findk("kkkkkkkkkkkkkkkkkkkk",0)

#find all positions at which stuff to right reduces to jk=i
def find_right_jk(s,dbg):
    """returns list of positions (numbering 0 as rightmost character) where all characters to the right reduce to jk = i"""
    #will use this to test if middle section is OK and reduces to j (where we know right side reduces to k)
    if dbg: print "input: ",s
    ret=[]
    cum,isneg = "1",0 #isneg = sign of the cumulative so far, 0 or 1 -- this is kind of the output of the null string on right end
    for pch,ch in enumerate(s[::-1]): #pch here is 0 for right-most character
        if dbg: print "pch,ch=",(pch,ch)," cum,isneg=",(cum,isneg)
        if cum=="1":
            cum = ch #1*x = x, -1*x = -x (preserve sign: isneg unchanged)
        else:
            cum,isneg2 = multbl2[ord(ch)-ord("i")][ord(cum)-ord("i")]
            isneg = isneg ^ isneg2 #multiply signs (with xor)
        if dbg: print " cum2,isneg2=",(cum,isneg),"="+(" -"[isneg])+cum
        if isneg==0 and cum=="i": ret += [pch]
    return ret
#print find_right_jk("ijijijijijijij",0)

def sol1(s,dbg):
    """Return 1 if has solution"""
    if dbg: print "sol1 input=",s,len(s)
    ipos = findi(s,0)
    kpos = find_right_k(s,0)
    jkpos = find_right_jk(s,0)
    jkdic = {}
    if dbg: print "ipos=",ipos
    if dbg: print "kpos=",kpos
    if dbg: print "jkpos=",jkpos,jkdic
    for jk in jkpos: jkdic[jk]=1
    for ai in ipos:
        for ak in kpos:
            if (ai+1) + (ak+1) + 1 > len(s): break #no more ak
            #i substring is s[:ai+1]
            #j substring s[ai+1 : - (ak+1)]
            #k substring is s[-(ak+1):]
            lenjk = len(s) - (ai+1)
            if dbg: print s[:ai+1], s[ai+1 : -(ak+1)], s[-(ak+1):], "lenjk=",lenjk
            if (lenjk-1) in jkdic: #if (len(s) - lenjk) in jkdic:
                if dbg: print "solution ai,ak=",ai,ak
                return 1
    if dbg: print "no solution"
    return 0

#sol1("ijijijijijijijijijk",1)

def mpower(aa, N):
    if aa[0]=='-':
        return ('-' if (N%2)==1 else '') + mul2(aa[1:] * (N%4))
    else:
        return mul2(aa * (N%4))
    
def sol2(s, X, dbg):
    """s is string, X is repetitions of s.  Return if any solution.  dbg=1 to show work.
    len(s) can be up to 10,000
    X can be up to 10^12
    Didn't do this part.
    """
    if dbg: print "sol2 input len(s)=",len(s),"X=",X,"s = ",s
    start_time = time.time()
    s_red = mul2(s) # reduced s -- might have minus sign
    s_power = mpower(s_red, X) #this handles X%4
    if dbg: print len(s_power),"=len(s_power)"
    r_s_power = mul2(s_power)
    end_time = time.time()
    if dbg and (end_time-start_time > .1): print("Mul2 time: %.4g s" % (end_time - start_time))
    if r_s_power<>"-1": #whole thing can't be ijk if it doesn't equal -1
        if dbg: print "s_red = ",s_red, "check total, should be ijk = -1:", mul2(s_power),"=-1?"
        return 0
    #the left string (reducing to i) might be many whole copies of s followed by left side of s
    #the right string (reducing to k) might be many whole copies of s on the right, and then (on its left) the right side of s
    #since s itself can be reduced to +/- 1,i,j,k,
    #and s^n is the same as s^(n mod 4),
    #we should be able to find all possible left sides as only 4 times as complex as in sol1 above
    if X<=16: return sol1(s*X, 0) #as-given, do it the old way
    useX = (X%4) + 12 #assert this is enough since any other multiple of 4 must live in i,j,k section and =1
    return sol1(s * useX,0)

def sol2t(s, X, dbg): #same but show timing
    start_time = time.time()
    v = sol2(s, X, 1 if dbg>1 else 0)
    end_time = time.time()
    dt = round(end_time - start_time,3)
    if dbg and dt>.1: print "sol2 time: %.3g s" % dt
    return v

#sol2("jk" * 100,1,1)

def shows(s):
    if len(s)<=100: return s
    return s[:97]+"..."+s[-3:]

dbg=1
if 1:
  t0 = time.time()
  sumz = 0
  for i in range(1,T+1):
    rawline = FILE.readline().split(' ')
    L,X = int(rawline[0]), int(rawline[1]) #ok if newline after X
    if dbg: print "Case #" + str(i)+": L=",L," X=",X
    s = FILE.readline()
    if s[-1]<'0': s=s[:-1]#strip newline
    if dbg: print "  s="+shows(s)+" * "+str(X)+" len(s)=",len(s)

    #z0 = sol1(s * X, 0)
    z = sol2t(s, X, 1)
    if dbg: print "  ==> ",z
    sumz += z
    #if z<>z0: raise "mismatch",z,z0
    msg = 'Case #' + str(i) + ': ' + ("YES" if z else "NO")
    if dbg: print msg
    if not dbg and i%10==1: print msg
    FOUT.write(msg + "\n")
  print "finished",T,"cases,", round(time.time() - t0,3),"s, YESs:",sumz
FOUT.close()
FILE.close()
