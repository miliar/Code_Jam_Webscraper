import itertools

f = open("A-small.txt")

o = open("a-small.out", "w+")


line = f.readline()
T = int(line[:-1])

for rep in range(T):
    line = f.readline()
    line = line[:-1] if line[-1] == '\n' else line
    line = line.split(" ")
    
    R = int(line[0])
    C = int(line[1])
    W = int(line[2])

#    print(R, C, W)
    win = False
    guess = 0
    shots = 0
    while not win:
        if C - guess <= W:
            shots += W
            win = True
        else:
            shots += 1
            guess += W
#        print(guess)
        
        
        
#    print(shots * R)
    
    
    print("Case #%d: %.6f\n"%(rep+1, shots * R))
    o.write("Case #%d: %.6f\n"%(rep+1, shots * R))
o.close()
f.close()
