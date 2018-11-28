import sys

g={'a':'y','b':'h','c':'e','d':'s','e':'o','f':'c','g':'v','h':'x','i':'d',\
   'j':'u','k':'i','l':'g','j':'u','k':'i','l':'g','m':'l','n':'b','o':'k',\
   'p':'r','q':'z','r':'t','s':'n','t':'w','u':'j','v':'p','w':'f','x':'m',\
   'y':'a','z':'q'}

control = True
f=open("test.in")
user_input = f.readlines()
lines=int(user_input[0])
user_input=user_input[1:]
i=0
while i<len(user_input):
    user_input[i]=user_input[i][:-1]
    i+=1

#print(user_input);
f=open('output.out',mode='w')
i=1
x=[]
for line in user_input:
    output=[]
    a=list(line)
    j=0
    while j<len(a):
        if(a[j]!=" "):
            output.append(g[a[j]])
            j+=1
        else:
            output.append(" ")
            j+=1
    output=''.join(output)
    output="Case #{0}: ".format(i) + output
    i+=1
    x.append(output)
    print(output)
x='\n'.join(x)
f.write(x)
f.close()
