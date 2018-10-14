#! /usr/bin/env python3.0

def harmony(n1, n2):
    return ((n1%n2 == 0) or (n2%n1 == 0))

fic = input()

f = open(fic, "r")
lines = [li.replace("\n", "") for li in f.readlines()]
f.close()

lines = lines[1:]

f = open("output.txt", "w")

for i in range(0, len(lines), 2):
    
    min = int(lines[i].split(" ")[1])
    max = int(lines[i].split(" ")[2])
    
    tab = [int(k) for k in lines[i+1].split(" ")]
    
    note = 0
    
    for n in range(min, max+1):
        for n2 in tab:
            if (not harmony(n, n2)):
                break
        else:
            if (note == 0):
                note = n
    
    if (note == 0):
        note = "NO"
    else:
        note = str(note)
    
    
    out = "Case #"+str(int(i/2)+1)+": "+note
    print(out)
    f.write(out+"\n")

f.close()