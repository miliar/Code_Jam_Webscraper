finput= open('C-small-attempt0.in')
fout= open('C-small-attempt0.out', 'w')

ntc= int(finput.readline())

lookup= {'11':'1',
         'i1':'i',
         'j1':'j',
         'k1':'k',
         '1i':'i',
         'ii':'-1',
         'ji':'-k',
         'ki':'j',
         '1j':'j',
         'ij':'k',
         'jj':'-1',
         'kj':'-i',
         '1k':'k',
         'ik':'-j',
         'jk':'i',
         'kk':'-1'}

def quap(f, s):
    f= str(f).strip()
    s= str(s).strip()
    use = f[len(f)-1]+ s[len(s)-1]

    if (((f[0] == "-") and (s[0] == "-")) or ((f[0]!= "-") and (s[0] != "-"))):
        #print "normal"
        #tpl= f,s
        hold=lookup[use]
        #print hold
        return hold
    else:
        #print "neg"
        #print use
        temp =lookup[use]

        if (temp[0] == "-"):
            #print "yeah"
            hold= temp
            #print hold[-1]
            return hold[-1]
        else:
            #print "-"+temp
            return "-"+temp
        
##        if (str(lookup[use])[0] =="-"):
##            hold= lookup[use]
##        else:
##            hold ="-"+ lookup[use]
        

for y in xrange(0, ntc):
    #entry= raw_input()
    entry = finput.readline()

    enel= [int(x) for x in entry.split(" ")]
    #letters= raw_input()
    letters = finput.readline().strip()
    first= enel[0]
    second= enel[1]
    
    print letters
    if (letters == letters[::-1]):
        #print "sr"
        fout.write("Case #" + str(y+1) + ": " + "NO"+"\n")
        #print "NO"
    else:
        flet= letters*second
        #print flet

        prod= first * second
        qp=1
        hold=""
        status= 0
        #print str(prod)

        if (prod<3):
            fout.write("Case #" + str(y+1) + ": " + "NO"+"\n")
            #print "NO"
        else:
            for i in xrange(0, len(flet)):
                qp= quap(qp,flet[i])
                #print str(i) + "  " + str(flet[i])
                #print qp
                #print str(status)
                if (status==0):
                    if (qp == "i"):
                        qp="1"
                        status=1
                elif (status==1):
                    if (qp == "j"):
                        qp="1"
                        status=2
                #print qp

            if ((status ==2) and (qp=="k")):
                fout.write("Case #" + str(y+1) + ": " + "YES"+"\n")
                #print "YES"
            else:
                fout.write("Case #" + str(y+1) + ": " + "NO"+"\n")
                #print "NO"

fout.close()
##2 1
##ik
##3 1
##ijk
##3 1
##kji
##2 6
##ji
##1 10000
##i
    
