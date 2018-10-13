def count(maxShy, occurrences):
    currentStanding = 0
    friends = 0
    for i in range(0, int(maxShy)+1):

        currentShy = int(occurrences[i])
        if currentStanding < i and currentShy > 0:
            friends += (i - currentStanding)
            currentStanding += (i - currentStanding)

        currentStanding += currentShy

    return friends

def main():
    f = open('/Users/alex/Downloads/A-large.in.txt')
    nTests = int(f.readline().replace("\n",""))
    for i in range(nTests):
        line = f.readline().replace("\n","")
        (maxShy, occurrences) = line.split(" ")
        print "Case #" + str(i+1) + ": " + str(count(maxShy, occurrences))

if __name__ == "__main__":
    main()
