"""
Dijkstra
"""
def read_words(filename):
    """
    takes a file and creates a list of strings, one word per index
    """
    file=open(filename,"r")
    words = []
    word = ''
    for line in file:
        word = line.rstrip()
        words.append(word)
    file.close()
    return words

table =[]
table.append(["1","i","j","k"])
table.append(["i","-1","k","-j"])
table.append(["j","-k","-1","i"])
table.append(["k","j","-i","-1"])


lines = read_words("small_dijkstra.txt")
count = 1
output= []

i = 1
j = 2
k = 3

def char_to_int(char):
    if char[0] =="-":
        if char[1]=="i":
            return 1
        if char[1] == "j":
            return 2
        if char[1] == "k":
            return 3
        else:
            return 0
    else:
        if char[0]=="i":
            return 1
        if char[0] == "j":
            return 2
        if char[0] == "k":
            return 3        
        else:
            return 0

for z in range(len(lines)) : 
    yi_ni = "no"
    if (z == 0):
        continue
    elif  z % 2 == 1:

        vals = lines[z].split()
        string_in = lines[z+1]*int(vals[1])
        

        cur = 0
        anscount = 0
        non_neg = True
        
        for q in range(len(string_in)):
            char = string_in[q]
            char_int = char_to_int(char)
        
            if anscount == 0:
                # find i
               
                cur = table[cur][char_int]
                #print cur
                if(cur[0]=="-"):
                    non_neg= not non_neg
                    
                cur = char_to_int(cur)
                
                if cur == 1:
                    anscount = 1
                    cur = 0 
                    continue

                
                
            elif (anscount==1):
                #find j
                
                cur = table[cur][char_int]
                #print cur
                if(cur[0]=="-"):
                    non_neg= not non_neg
                    
                cur = char_to_int(cur)                
                if cur == 2:
                    anscount =2
                    cur = 0 
                    continue                    
           
            else:
                #rest must be k
               
                cur = table[cur][char_int]
                #print cur
                if(cur[0]=="-"):
                    non_neg= not non_neg
                cur = char_to_int(cur)
        
        if (non_neg and anscount ==2 and cur == 3):
            yi_ni="yes"
        output.append("Case #"+str(count)+": "+str(yi_ni))
        count += 1
for i in range(len(output)):
    print output[i]