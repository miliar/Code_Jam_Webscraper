mini = None
def read():
    with open('A-small-attempt0.in', 'r') as content_file:
        content = content_file.read()
        return content.split('\n')

a=read()

def flip(s,start,n):  
    for i in range(start,start+n):
        if len(s)<start+n:
            return
        if s[i]=='+':
            s[i]='-'
        else:
            s[i]='+'

def fun(s,n,counter=0):
    global mini
    if s[0]=='+' and len(set(s))==1:
        return counter
    for i in range(counter,len(s)):
        if len(s)>=i+n:
            #print s
            flip(s,i,n)
            #print s,n,counter+1,i
            result=fun(s,n,counter+1)
            if result:
                if mini == None:
                    mini=result
                elif result<mini:
                    mini=result
                
            flip(s,i,n)
with open("test2.out", "w") as myfile:
    T=int(a[0])
    counter=0
    for case in range(1,T+1):
        mini= None
        counter+=1
        
        input_i=a[case].split(' ')
        s=list(input_i[0])
        n=int(input_i[1])
        
        if s[0]=='+' and len(set(s))==1:
                myfile.write("Case #{}: 0".format(counter))
        else:
            fun(s,n)
            if mini == None:
                myfile.write("Case #{}: IMPOSSIBLE".format(counter))
            else:
                myfile.write("Case #{}: {}".format(counter,mini))
        if counter<T:
            myfile.write("\n")
            