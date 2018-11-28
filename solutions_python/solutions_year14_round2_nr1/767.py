import math
import time
start_time = time.time()

f = open("A.txt",'r')
ntests = int(f.readline())

g = open("output.txt",'w')

def simplify (word):
    word = word.replace("\n","") #as the end of lines keep appearring
    ln = len(word) #str length
    letters = [word[0]]
    length = [0]
    for i in range (ln):
        if word[i] != letters[-1]:
            letters.append(word[i])
            length.append(1)
        else:
            length[-1] += 1
    return [letters, length]


for i in range(ntests):
    p = int(f.readline()) #N
    words = []

    for j in range(p):
        line = f.readline()
        words.append(simplify(line)) #the N words's letters, length

    shape = words[0][0] #letters
    fail = 0
    for j in range(p):
        if words[j][0] != shape:
            fail = 1
            break


    if fail==1:
        s = "Fegla Won"

    else:
        ln = len(shape)
        count = [0]*ln

        for k in range(ln):
            for j in range(p):
                count[k]+=words[j][1][k]
            count[k]/=p

            t = int(round(count[k],0))
            count[k] = 0
            for j in range(p):
                count[k] += abs(words[j][1][k]-t)
        s =0
        for k in range(ln):
            s+=count[k]

            

    g.write("Case #{}: {}\n".format(i+1,s))
    
f.close()
g.close()

print (time.time() - start_time, "secs")
