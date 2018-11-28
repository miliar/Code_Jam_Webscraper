s=[]

f = open('A-small-attempt2.in', 'r')
s.append(int(f.readline()))
for i in range(s[0]):
    s.append(f.readline().strip())        

dict={'y':'a','e':'o','j':'u','p':'r','m':'l','s':'n','l':'g','k':'i','d':'s','x':'m','v':'p','n':'b','r':'t','i':'d','b':'h','t':'w','c':'e','a':'y','h':'x','w':'f','u':'j','g':'v','f':'c','o':'k','q':'z','z':'q',' ':' '}
#s=list("ejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc jv")
for k in range(1,int(s[0])+1):
    case=list(s[k])
    for i in range(len(case)):
        case[i]=dict[case[i]]
    case="".join(case)
    thefile=open("lang4.txt",'a')
    thefile.write("Case #" + str(k) + ": %s\n" % case)
    thefile.close()



