word = "welcome to code jam"
data = ""
count = 0

def calc2(index,current):
    global data,word,memo
    if current == len(word):
        return 1
    if index >= len(data):
        return 0
    try:
        x = data.index(word[current],index+1)
        return calc2(x,current) + calc2(x,current+1)
    except :
        return 0
        
    
fin = open("w0.in","r")
fout = open("w0.out","w")
num = int(fin.readline()[:-1])
for i in range(0,num):
    data = fin.readline()[:-1]
    c = str(calc2(-1,0))
    while len(c) < 4:
        c = '0' + c
    fout.write("Case #" + str(i+1) + ": " + c + "\n")

    
fin.close()
fout.close()

