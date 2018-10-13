dic={'a':'y','b':'h','c':'e','d':'s','e':'o','f':'c','g':'v','h':'x','i':'d','j':'u','k':'i','l':'g','m':'l','n':'b','o':'k','p':'r','q':'z','r':'t','s':'n','t':'w','u':'j','v':'p','w':'f','x':'m','y':'a','z':'q',' ':' '}
f1=open("in")
f2=open('out','w')
loop=int(f1.readline())
#print loop

for ii in range(1,loop+1):
    str1=f1.readline()
    #flag=0
    str2=''
    
    for i in str1:
        #print i
        if i == '\n':
            break
        str2=str2+dic[i]
        
    #print ("Case #%d: %s\n" % (ii,str2))
    f2.write("Case #%d: %s\n" % (ii,str2))