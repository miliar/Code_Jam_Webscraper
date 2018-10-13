file = open("A-large.in","r")
batches = []
for line in file:
    line = line.strip()
    batches.append(line)
batches = batches[1:]
file.close()

def panflip(value):
    pancake = []
    k = []
    count = 0
    for letter in value:
        if letter == ' ':
            pass
        elif letter.isdigit() == False:
            pancake.append(letter)
        else:
            k.append(letter)
    k = ''.join(k)
    k = int(k)
    for i in range(len(pancake) - (k - 1)):
        if pancake[i] == "-":
            for j in range(0,k):
                if pancake[i + j] == "-":
                    pancake[i + j] = "+"
                else:
                    pancake[i + j] = "-"
            count = count + 1
        else:
            pass
    for side in pancake:
        if side == "+":
            pass
        else:
            count = "IMPOSSIBLE"
    return count

result = []
for batch in batches:
    flips = panflip(batch)
    result.append(flips)


file = open("finale2.txt","w")
for i in range(len(result)):
    file.write("Case #{0}: {1}\n".format(i + 1,result[i]))
file.close()
    
    
            

