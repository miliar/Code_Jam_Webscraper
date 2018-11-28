import math

def solveThirds(plates, minutes):
    if (max(plates) == 0):
        return minutes
    original_max = max(plates)
    plates_copy = [x - 1 for x in plates]

    optimal_minutes = 999

    # split stacks in (as close to half as possible) and record
    # the lowest (# movements) + (max stack after)

    solution = list(plates)

    while (minutes <= 10):
        if (minutes + max(plates) < optimal_minutes):
            optimal_minutes = minutes + max(plates)
            solution = list(plates)
        print(plates)
        minutes += 1
        most = max(plates)
        i = plates.index(most)
        if (most == 9):
            plates[i] = 6
            plates.append(3)
        else:
            plates[i] = int(math.floor(most / 2))
            plates.append(int(math.floor(most- (most / 2))))
        if (minutes + max(plates) < optimal_minutes):
            print("Found new best")
            optimal_minutes = minutes + max(plates)
            solution = list(plates)

    #optimal_if_wait = solve(plates_copy, minutes + 1)
    optimal_if_wait = 999

    return min(optimal_if_wait, optimal_minutes)

def solve(plates, minutes):
    if (max(plates) == 0):
        return minutes
    original_max = max(plates)
    plates_copy = [x - 1 for x in plates]

    optimal_minutes = 999

    # split stacks in (as close to half as possible) and record
    # the lowest (# movements) + (max stack after)

    solution = list(plates)

    while (minutes <= 10):
        if (minutes + max(plates) < optimal_minutes):
            optimal_minutes = minutes + max(plates)
            solution = list(plates)
        print(plates)
        minutes += 1
        most = max(plates)
        i = plates.index(most)
        plates[i] = int(math.floor(most / 2))
        plates.append(int(math.floor(most- (most / 2))))
        if (minutes + max(plates) < optimal_minutes):
            print("Found new best")
            optimal_minutes = minutes + max(plates)
            solution = list(plates)

    #optimal_if_wait = solve(plates_copy, minutes + 1)
    optimal_if_wait = 999

    return min(optimal_if_wait, optimal_minutes)

def main():

    infile = open("input.txt")
    outfile = open("output.txt", 'w')

    one = infile.readline()
    testCases = int(one)
    print(str(testCases) + " test cases")


    case = 1

    while (case <= testCases):
        diners = int(infile.readline().strip())
        plates = map(int, infile.readline().strip().split())

        if (diners != len(plates)):
            print("ERROR")
            exit()
        plates_copy1 = list(plates)
        plates_copy2 = list(plates)
        optimal_minutes = solve(plates_copy1, 0)
        alternate = solveThirds(plates_copy2, 0)
        if (alternate != optimal_minutes):
            print("ALERT! with thirds, got " + str(alternate) + " versus regular got " + str(optimal_minutes))


        print("Best was " + str(min(optimal_minutes, alternate)) + " minutes.")
        print("")
        outfile.write("Case #" + str(case) + ": " + str(min(optimal_minutes, alternate)) + "\n")
        case += 1

    outfile.close()
    infile.close()


main()
