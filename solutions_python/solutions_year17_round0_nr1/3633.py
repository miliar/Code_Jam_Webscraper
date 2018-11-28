num_of_loops = int(input())

def solution(case):
    case = case.split(" ")
    pancakes = case[0]
    k = int(case[1])
    total_flips = 0
    #print(pancakes, str(k), "IMPOSSIBLE")
    counter = 0
    pancakes = list(pancakes)
    while (counter < len(pancakes) - k + 1):
        if (pancakes[counter] == "-"):
            for j in range(counter, counter + k):
                if (pancakes[j] == "-"):
                    pancakes[j] = "+"
                else:
                    pancakes[j] = "-"
                #print(j)
            #print(pancakes)
            #print("flips")
            total_flips += 1
        counter += 1
    cond = True
    for i in range(len(pancakes)):
        if (pancakes[i] == "-"):
            cond = False
    #print(total_flips, cond)
    if (cond):
        return str(total_flips)
    else:
        return ("IMPOSSIBLE")
    return (" ")

for i in range(num_of_loops):
    print("Case #"+str(i+1)+": " + solution(input()))

