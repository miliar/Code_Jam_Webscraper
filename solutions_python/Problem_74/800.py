file = open("A-large.in","r")
data = [t.split(" ") for t in file.read().strip().split("\n")][1:]
file.close()
##print(data)
results = []
for line in data:
    line = line[1:]
    blue = 1
    orange = 1
    time = 0
    while len(line) > 0:
        pushed = False
##        print(line,"B:",blue,"O:",orange,"T:",time)
        time += 1
        if "B" in line:
            if blue == int(line[line.index("B")+1]) and not pushed:
                if line.index("B") == 0:
                    line = line[2:]
                    pushed = True
            elif blue < int(line[line.index("B")+1]):
                blue += 1
            elif blue > int(line[line.index("B")+1]):
                blue -= 1
        if "O" in line:
            if orange == int(line[line.index("O")+1]) and not pushed:
                if line.index("O") == 0:
                    line = line[2:]
                    pushed = True
            elif orange < int(line[line.index("O")+1]):
                orange += 1
            elif orange > int(line[line.index("O")+1]):
                orange -= 1
        
            
    results.append(time)
##print("\n".join(["Case #"+str(x+1)+": "+str(y) for x,y in enumerate(results)]))
file = open("A-small.out","w")
file.write("\n".join(["Case #"+str(x+1)+": "+str(y) for x,y in enumerate(results)]))
file.close()
