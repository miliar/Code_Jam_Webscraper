def invert(pancakeline, number):
    if pancakeline[number] == "+":
        pancakeline = pancake_line[0:number] + "-" + pancake_line[number+1:]
    else:
        pancakeline = pancake_line[0:number] + "+" + pancake_line[number+1:]
    return pancakeline





t = int(input())

for i in range(1, t + 1):
    input_line = input()
    input_line = input_line.split(" ")
    flips = 0
    pancake_line = input_line[0]
    k = int(input_line[1])

    for j in range(0, len(pancake_line)):
        if pancake_line[j] == "-":
            #print(pancake_line)
            flips += 1
            if len(pancake_line) < j + k:
                flips = "IMPOSSIBLE"
                break
            else:
                for ii in range(0,k):
                    pancake_line = invert(pancake_line, j+ii)

    #print(pancake_line)
    print("Case #{}: {}".format(i, flips))



'''
            pancake_line = pancake_line[0:j] + "+" + pancake_line[j:]

            if pancake_line[j+1] == "-":
                pancake_line = pancake_line[0:j+1] + "+" + pancake_line[j+1:]
            else:
                pancake_line = pancake_line[0:j + 1] + "-" + pancake_line[j + 1:]

            if pancake_line[j + 2] == "-":
                pancake_line = pancake_line[0:j + 2] + "+" + pancake_line[j + 2:]
            else:
                pancake_line = pancake_line[0:j + 2] + "-" + pancake_line[j + 2:]




    num_minus = pancake_line.count("-")

    if num_minus == 0:
        flips = 0

    elif num_minus < int(input_line[1]):
        flips = "IMPOSSIBLE"

    else:





        flips = num_minus #just for test
'''



