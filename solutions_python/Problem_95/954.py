import sys
filename=sys.argv[1]
infile=open(filename,"r")
outfile=open("google.out","w")
dict={'a':'y','b':'h','c':'e',' ':' ','\n':'\n','d':'s','e':'o','f':'c','g':'v','h':'x','i':'d','j':'u','k':'i','l':'g','m':'l','n':'b','o':'k','p':'r','q':'z','r':'t','s':'n','t':'w','u':'j','v':'p','w':'f','x':'m','y':'a','z':'q'}
count=0
list=[]
line=''
for line in infile:
    if count==0:
        count+=1
        continue
    else:

        count+=1
        out=''
        for i in line:
            out+=dict[i]
        outfile.write ("Case #"+str(count-1)+": "+str(out))
print "Done"
outfile.close()
