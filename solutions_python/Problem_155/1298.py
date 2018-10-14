"""
1<T<100
0<S<6

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

words = read_words("A-large.in")
count = 0
output = []
wrdnum = 0

for wrd in words:
    num = 0
    
    if (count % 2 == 0):
        sumnum=0
        if wrdnum ==0:
            wrdnum+=1
            continue
        cur = wrd.split()[1]
        for i in range(len( cur )):
           
            if i > sumnum:
                num += 1
                sumnum+=1 
            sumnum += int(cur[i])

                    
        output.append("Case #"+str(wrdnum)+": "+str(num))
        wrdnum+=1
        
for line in output:
    print line
            