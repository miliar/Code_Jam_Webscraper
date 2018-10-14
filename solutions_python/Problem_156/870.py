
def readFile(filename):
    with open(filename, 'r') as myfile:
        # First line is the smax
        line = myfile.readline()
        #print(line)
        i = 1
        for line in myfile:
            # Read the line in a list
            line = line[:-1]
            #print(line)
            plates_line = myfile.readline()[:-1]
            #print(plates_line)
            plates = [int(e) for e in plates_line.split(' ')]
            #print(plates_line, plates)
            # Give the line without \n
            temp = list(plates)
            minutes = recSolvePancakes(temp)
            #print(plates)
            print("Case #{}: {}".format(i, minutes))
            i += 1


def solvePancakes(plates):
    minutes = 0
    nb_pancakes = sum(plates)
    #print(nb_pancakes)
    while(nb_pancakes > 0):
        minutes += 1
        # Get the maxiimum of the plates
        M = max(plates)
        if M>len(plates): #We need to move pancakes
            max_i = plates.index(M)
            plates.append(M//2)
            plates[max_i] -= M//2
        else:
            plates = [e-1 for e in plates]
            plates = [e for e in plates if e != 0]
        nb_pancakes = sum(plates)
    return minutes

def recSolvePancakes(input_plates):
    # Try to divide the biggest element
    M = max(input_plates)
    if M<=3:
        return M
    minutes = []
    for i in range(2, M//2 +1):
        plates = list(input_plates)
        max_i = plates.index(M)
        # Create the new plates
        plates.append(i)
        plates[max_i] -= i
        # Is it worth it ?
        minutes.append(1 + recSolvePancakes(plates))
    # It's cool
    if(min(minutes) < M):
        return min(minutes)
    else: # Not worth it
        return M


if __name__ == "__main__":
    #L = [4] * 8
    #print(solvePancakes(L))
    filename = "B-small-attempt5.in"
    #filename = "pancaketest.txt"
    readFile(filename)
