def cal(string):
    
    num=[0,0,0,0,0,0,0,0,0,0]
    
    count=string.count("Z")
    num[0]=count
    string=string.replace("Z", "_", count)
    string=string.replace("E", "_", count)
    string=string.replace("R", "_", count)
    string=string.replace("O", "_", count)
    
    count=string.count("W")
    num[2]=count
    string=string.replace("T", "_", count)
    string=string.replace("W", "_", count)
    string=string.replace("O", "_", count)
    
    count=string.count("G")
    num[8]=count
    string=string.replace("E", "_", count)
    string=string.replace("I", "_", count)
    string=string.replace("G", "_", count)
    string=string.replace("H", "_", count)
    string=string.replace("T", "_", count)
    
    count=string.count("H")
    num[3]=count
    string=string.replace("T", "_", count)
    string=string.replace("H", "_", count)
    string=string.replace("R", "_", count)
    string=string.replace("E", "_", count*2)
    
    count=string.count("U")
    num[4]=count
    string=string.replace("F", "_", count)
    string=string.replace("O", "_", count)
    string=string.replace("U", "_", count)
    string=string.replace("R", "_", count)
    
    count=string.count("X")
    num[6]=count
    string=string.replace("S", "_", count)
    string=string.replace("I", "_", count)
    string=string.replace("X", "_", count)
    
    count=string.count("F")
    num[5]=count
    string=string.replace("F", "_", count)
    string=string.replace("I", "_", count)
    string=string.replace("V", "_", count)
    string=string.replace("E", "_", count)
    
    count=string.count("V")
    num[7]=count
    string=string.replace("S", "_", count)
    string=string.replace("E", "_", count*2)
    string=string.replace("V", "_", count)
    string=string.replace("N", "_", count)
    
    count=string.count("I")
    num[9]=count
    string=string.replace("N", "_", count*2)
    string=string.replace("I", "_", count)
    string=string.replace("E", "_", count)
    
    count=string.count("O")
    num[1]=count
    string=string.replace("O", "_", count)
    string=string.replace("N", "_", count)
    string=string.replace("E", "_", count)
    
    final=""
    for i in range(10):
        final=final+ str(i) *num[i]
        
    return final
    

file = open("a")
T = file.readline()
all_the_text=[]

for num in range(1,int(T)+1):
    word=file.readline().strip()
    final=cal(word)
    temstr='Case #'+str(num)+': '+final+'\n'
    all_the_text.append(temstr)
    
file_object = open('thefile.txt', 'w+')
file_object.writelines(all_the_text)
file_object.close( )