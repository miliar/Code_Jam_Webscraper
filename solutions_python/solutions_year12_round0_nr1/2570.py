#Googlerese

#mapping = {'a':'y', 'b':'n','c':'f','d':'i','e':'c','f':'w','g':'l','h':'b','i':'k','j':'u','k':'o','l':'m','m':'x','n':'s','o':'e','p':'v','q':'','r':'p','s':'d','t':'r','u':'j','v':'g','w':'t','x':'n','y':'a','z':'q',' ':' ','\n':'\n'}
mapping = {'h':'x', 'y':'a', 'n':'b','f':'c','i':'d','c':'e','w':'f','l':'g','b':'h','k':'i','u':'j','o':'k','m':'l','x':'m','s':'n','e':'o','v':'p','z':'q','p':'r','d':'s','r':'t','j':'u','g':'v','t':'w','a':'y','q':'z',' ':' ','\n':'\n'}

#print sorted(mapping.keys())
#print sorted(mapping.values())
#print mapping

#Read input
f_in = open("C:\\Users\\Sumit Chopra\\Desktop\\code_jam\\A-small-attempt0.in","r")
f_out = open("C:\\Users\\Sumit Chopra\\Desktop\\code_jam\\A-small-attempt0.out","w")

#number of test cases
numTestCases = int(f_in.readline())

i = 1
while i <= numTestCases:
    line = f_in.readline()
    f_out.write("Case #"+str(i)+": ")
    for e in line:
        f_out.write(mapping[e])
    i+=1

f_in.close()
f_out.close()