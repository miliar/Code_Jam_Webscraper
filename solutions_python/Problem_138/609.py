import sys
import copy

def normal(naomi, ken):
    naomi_score = 0
    while len(naomi) > 0:
        naomi_block = naomi[0]
        naomi = naomi[1:]
        removed = False
        for i in range(len(ken)):
            if ken[i] > naomi_block:
                ken = ken[0:i] + ken[i+1:]
                removed = True
                break
        if not removed:
            naomi_score += 1
            ken = ken[1:]
    return naomi_score

def deceitful(naomi, ken):
    naomi_score = 0
    while len(ken) > 0:
        ken_block = ken[0]
        removed = False
        for i in range(len(naomi)):
            if naomi[i] > ken_block:
                naomi = naomi[0:i] + naomi[i+1:]
                ken = ken[1:]
                removed = True
                naomi_score += 1
                break
        if not removed:
            naomi = naomi[1:]
            ken = ken[:len(ken)-1]
    return naomi_score

input_file = open(sys.argv[1])
input = []
output = open("output.txt", "w")
for line in input_file:
    input.append(line)
for i in range(0, int(input[0])):
    index = i * 3
    naomi = input[index + 2].split()
    naomi = [float(n) for n in naomi]
    naomi.sort()
    ken = input[index + 3].split()
    ken = [float(n) for n in ken]
    ken.sort()
    output.write("Case #" + str(i+1) + ": " + str(deceitful(naomi, ken)) + " " + str(normal(naomi, ken)) + "\n")