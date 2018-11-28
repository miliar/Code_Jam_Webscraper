import copy

fileHandle = open('in.txt', 'r')
outputHandle = open('out.txt', 'w')


def war(array_a, array_b):
    n = len(array_a)
    war_result = 0
    array_a.sort()
    array_b.sort()

    for i in reversed(range(n)):
        not_found_flag = True
        for j in reversed(array_a):
            if array_b[i] > j:
                not_found_flag = False
                war_result += 1
                array_a.remove(j)
                break
        if not_found_flag:
            return n - war_result

    return n - war_result


def deceitful_war(array_a, array_b):
    n = len(array_a)
    deceitful_war_result = 0
    array_a.sort()
    array_b.sort()
    for i in range(n):
        for j in array_b:
            if array_a[i] > j:
                deceitful_war_result += 1
                array_b.remove(j)
                break
    return deceitful_war_result


caseNumber = int(fileHandle.readline())

for i in range(caseNumber):
    dump = fileHandle.readline()

    array_a = [float(j) for j in fileHandle.readline().split(" ")]
    array_b = [float(j) for j in fileHandle.readline().split(" ")]

    outputHandle.write("Case #" + str(i+1) + ": " + str(deceitful_war(copy.copy(array_a), copy.copy(array_b))) + " " + str(war(copy.copy(array_a), copy.copy(array_b))) + "\n")

fileHandle.close()
outputHandle.close()