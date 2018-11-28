def main():
    infile = open("A-large (1).in", "r")
    outfile = open("A-large (1).out", "w")
    T = int(infile.readline())
    for i in range(T):
        line = infile.readline().split(" ")
        D = int(line[0])
        N = int(line[1])
        horses = [[0, 0] for j in range(N)]
        for j in range(N):
            line = infile.readline().split(" ")
            horses[j][0] = int(line[0])
            horses[j][1] = int(line[1])
        outfile.write("Case #"+str(i+1)+": "+str(findMaxSpeed(D, N, horses))+"\n")
    infile.close()
    outfile.close()

def findMaxSpeed(D, N, horses):
    maxTime = 0
    dest = 0
    speed = 0
    for i in range(N):
        time = (D-horses[i][0])/horses[i][1]
        if(time > maxTime):
            maxTime = time
            dest = horses[i][0]
            speed = horses[i][1]
    time = maxTime
    return((dest+speed*time)/time)
