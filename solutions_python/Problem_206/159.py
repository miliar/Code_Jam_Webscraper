
input = open("A-large.in", "r")
output = open("A-large.out", "w")


T = int(input.readline().strip())

for j in range(1, T+1):
    output.write("case #{}: ".format(j))
    line = input.readline().strip()
    D = float(line.split()[0])
    N = int(line.split()[1])
    horses = []
    for i in range(N):
    	line = input.readline().strip()
    	pos = float(line.split()[0])
    	speed = float(line.split()[1]) 
    	horses.append((pos, speed))

    max_time = max([((D - horse[0])/ horse[1]) for horse in horses])
    
    speed = D / max_time
    output.write("{0:.6f}".format(speed))
    output.write("\n")


input.close()
output.close()

