def result(line):
    dic={'a':'y','b':'h','c':'e','d':'s','e':'o','f':'c','g':'v','h':'x','i':'d','j':'u','k':'i','l':'g','m':'l','n':'b','o':'k','p':'r','q':'z','r':'t','s':'n','o':'k','p':'r','q':'z','r':'t','s':'n','t':'w','u':'j','v':'p','w':'f','x':'m','y':'a','z':'q',' ':' ','\n':'\n'}
    nline="";
    for c in line:
        nline+=dic[c]
    return nline

testcase=int(raw_input())
li=[];
for i in range(0,testcase):
    line=str(raw_input())
    nline=result(line);
    li.append(nline);
for i in range(0,testcase):
    print "Case #"+str(i+1)+": "+li[i]

