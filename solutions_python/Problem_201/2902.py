from eulerlib import *

def next_right(stalls, index):
    for i in range(index + 1, len(stalls)):
        if stalls[i]:
            return i

    print("Error")

def solve(n, k):
    stalls = n + 2 #Stalls
    occupied = [False] * stalls #True if occupied
    occupied[0] = True #The first is always
    occupied[stalls - 1] = True #The last is always

    left_most = 0 #The left most stall which is occupied

    last_selection = 0

    for user in range(0, k): #Loop over 0...k (for each bathroom user)
        #print(last_selection)
        stall_close = []
        
        for stall_index in range(0, len(occupied)):
            stall = occupied[stall_index]

            if stall == True:
                stall_close.append(False) #To ensure it is the smallest
                left_most = stall_index #Since it is occupied, it is the left most stall which is occupied.
                continue

            ls = stall_index - left_most - 1 #Calculate the value of ls as the current stall minus the left occupied stall minus 1 to ensure that the value is correct.
            #For example, (0)[True](1)[False]... and they choose 1. 1 - 0 = 1 - 1 = 0 stalls between them.
            rs = next_right(occupied, stall_index) - stall_index - 1
            #(0)[True](1)[False](2)[False](3)[True] Pick stall 1. Right most = 3 (1 stall between) 3 - 1 = 2 - 1 = 1 stall
            stall_close.append((ls, rs))

        #Now decide which is the best
        #print(stall_close)

        #Choose the farthest closest neighbour

        farthest_closest_index = 0
        farthest_closest_maximal = -1
        clash = []

        for i in range(0, len(stall_close)):
            if stall_close[i] == False:
                continue
            
            m = min(stall_close[i])
            
            if m == farthest_closest_maximal:
                clash.append(i)

            if m > farthest_closest_maximal:
                farthest_closest_maximal = m
                farthest_closest_index = i
                clash = [farthest_closest_index]

        if len(clash) == 1:
            #print("Selected through first", farthest_closest_index)
            occupied[farthest_closest_index] = True
            last_selection = stall_close[farthest_closest_index]
            continue

        farthest_max_index = 0
        fartest_max_maximal = -1
        clash_t = []

        for i in clash:
            if stall_close[i] == False:
                continue
            
            m = max(stall_close[i])

            if m == fartest_max_maximal:
                clash_t.append(i)

            if m > fartest_max_maximal:
                fartest_max_maximal = m
                farthest_max_index = i
                clash_t = [farthest_max_index]

        if len(clash_t) == 1:
            #print("Selected through second", farthest_closest_index)
            occupied[farthest_max_index] = True
            last_selection = stall_close[farthest_max_index]
            continue

        #print("Selected through third", clash[0])
        occupied[clash_t[0]] = True
        last_selection = stall_close[clash_t[0]]

    return (max(last_selection), min(last_selection))

#time_algorithm(solve, (1000, 1000))

solutions = []

with open("C-small-1-attempt0.in") as file:
    case = 1
    for line in file.readlines()[1:]:
        spl = line.split(" ")
        a = int(spl[0])
        b = int(spl[1].strip())

        answer = solve(a, b)
        sol = "Case #" + str(case) + ": " + str(answer[0]) + " " + str(answer[1]) + "\n"

        solutions.append(sol)

        case += 1

with open("C-small-1-answers.txt", "w") as file:
    file.writelines(solutions)

print("Finished")
