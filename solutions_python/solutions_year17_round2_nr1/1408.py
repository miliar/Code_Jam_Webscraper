
def main(file):

    f = open(file)
    text = f.read().split("\n")
    f.close()

    f = open("solution.txt", 'w')

    i = 1
    it = 0
    while it < int(text[0]):
        horses = []
        line = text[i].split()
        #print line
        d = int(line[0])
        horsesTot = int(line[1])
        #print horses
        for j in range(horsesTot):
            lineHorse = text[i+j+1].split()
            k = int(lineHorse[0])
            s = int(lineHorse[1])
            horses.append((k,s))

        #print horses
        maxVelocity = calculateMaxSpeed(horses, d)

        if (it == int(text[0])-1): f.write("Case #"+(str(it+1))+": "+str(maxVelocity))
        else: f.write("Case #"+(str(it+1))+": "+str(maxVelocity)+"\n")

        i = i + horsesTot + 1
        it += 1

    f.close()

def calculateMaxSpeed(horses, d):
    velocity = []

    for horse in horses:
        pos = horse[0]
        speed = horse[1]
        distanceLeft = d-pos
        timeLeft = distanceLeft/float(speed)
        maxVelocity = d/timeLeft
        velocity.append(maxVelocity)

    velocity.sort()

    return velocity[0]

main("A-large.in")