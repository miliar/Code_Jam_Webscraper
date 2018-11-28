
file_input = open("large-input.txt","r") 
file = open("large-output.txt", "w+") 

num_cases = int(file_input.readline().rstrip())

for case in range(num_cases):
    line = file_input.readline().rstrip()
    
    pancakes, k = [s for s in line.split(" ")]
    k = int(k)
    pancakes = list(pancakes)

    num_flips = 0
    for i in range(len(pancakes) - k + 1):
        pancake = pancakes[i]

        if pancake == '-':
            num_flips += 1

            for flipping in range(i, i + k):
                if pancakes[flipping] == '-':
                    pancakes[flipping] = '+'
                else:
                    pancakes[flipping] = '-'


    valid = True
    for pancake in pancakes:
        if pancake == '-':
            valid = False

    if valid:
        file.write("Case #" + str(case + 1) + ": " + str(num_flips) + "\n")
    else:
        file.write("Case #" + str(case + 1) + ": IMPOSSIBLE\n")

file_input.close()
file.close()