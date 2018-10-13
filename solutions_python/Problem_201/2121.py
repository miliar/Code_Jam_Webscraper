import sys

def main():
    if(len(sys.argv) < 2):
        print("Not enough arguments. Exiting.")
        exit()
    file = open(sys.argv[1], 'r')

    totalCases = int(file.readline().strip())
    testCases = 0

    line = file.readline().strip()
    while(line != ""):
        size, people = [int(value) for value in line.split(" ")]
        stalls = [None for i in range(size)]
        testCases += 1
        left = 0
        right = 0

        while people > 0:
            gaps = []
            start = -1
            for i in range(size):
                if(stalls[i] == None):
                    if(start == -1):
                        start = i
                elif(stalls[i] != None):
                    if(start != -1):
                        gaps.append([start, i - 1])
                        start = -1
            if(start != -1):
                gaps.append([start, size - 1])

            largest = 0
            for i, gap in list(enumerate(gaps)):
                if(gap[1] - gap[0] > gaps[largest][1] - gaps[largest][0]):
                    largest = i

            length = gaps[largest][1] - gaps[largest][0]
            left = (length // 2)
            right = length - left

            stalls[gaps[largest][0] + left] = 1
            people -= 1

        print("Case #" + str(testCases) + ": " + str(right) + " " + str(left))

        line = file.readline().strip()

    file.close()

if(__name__ == "__main__"):
    main()
