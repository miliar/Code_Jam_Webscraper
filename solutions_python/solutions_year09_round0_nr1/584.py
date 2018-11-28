import re,string,sys

file = open('A-large.in')
line = file.readline().rstrip("\r\n")
data = line.split(' ')
dict = []
for i in range(int(data[1])):
    line = file.readline().rstrip("\r\n")
    dict.append(line)
    #print (dict[i])

for i in range(int(data[2])):
    regex = file.readline().rstrip("\r\n")
    mystring = ''.join(regex)
    list = re.split('(\\([a-z]*\))|(\D{1})',mystring)
    for j in range(len(list)-1,-1,-1):
        if ((list[j] is None) | (list[j]=='')):
            del list[j]
    for j in range(len(list)):        
        if(re.match("^\(.*",list[j])):
            list[j]=re.split('\(|\)',list[j])[1]
    
    match=0
    for k in range(len(dict)):
        flag=0
        for pattern in range(len(list)):
            for letter in range(len(list[pattern])):
                if (list[pattern][letter]==dict[k][pattern]):
                    flag+=1
                    #print(flag)
        if(flag==len(list)):
                match+=1
    #text= "Case #"+i,":",match
    sys.stdout.write("Case #"+str(i+1)+":"+" "+str(match))
    print()
            
            
file.close()
