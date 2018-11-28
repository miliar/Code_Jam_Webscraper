INPUT  = "A-large.in"
OUTPUT = "A-large.out"

def rem_no(dc,oc,ind,s,val,no,l):
    for i in xrange(l):
        if val[i]==1 and s[i]==dc:
            no[ind]+=1
            val[i]=0

    if no[ind]:
        for x in oc:
            tmp=0
            for i in xrange(l):
                if val[i]==1 and s[i]==x:
                    tmp+=1
                    val[i]=0
                    if tmp==no[ind]: break

def solve(s):
    l=len(s);
    val=[1]*l
    no=[0]*10

    rem_no('Z',['E','R','O'],0,s,val,no,l)
    rem_no('X',['S','I'],6,s,val,no,l)
    rem_no('S',['E','V','E','N'],7,s,val,no,l)
    rem_no('G',['E','I','H','T'],8,s,val,no,l)
    rem_no('V',['F','I','E'],5,s,val,no,l)
    rem_no('U',['F','O','R'],4,s,val,no,l)
    rem_no('W',['T','O'],2,s,val,no,l)
    rem_no('I',['N','N','E'],9,s,val,no,l)
    rem_no('T',['H','R','E','E'],3,s,val,no,l)
    rem_no('O',['N','E'],1,s,val,no,l)

    ans=''
    for i in xrange(10):
        while no[i]!=0:
            ans+=str(i)
            no[i]-=1

    return ans

with open(INPUT) as infile:
    with open(OUTPUT, 'w') as outfile:
        t = int(infile.readline())

        for i in xrange(t):
            #n = int(infile.readline())
            #line = infile.readline()
            inputVal = infile.readline().strip()
            #inputVal = [int(x) for x in line.strip().split()]
            #print "Case #%d: %s" % (i + 1, solve(inputVal))
            outfile.write("Case #%d: %s\n" % (i + 1, solve(inputVal)))
