from math import ceil as ceil

file = open("b_input.txt")
out = open("b_output.txt", 'w')
T = int(file.readline().strip())
case = 1
for cases in range(T):
    diners = file.readline().strip()
    pancake = [int(i) for i in file.readline().strip().split()]
    pancake.sort(key=int, reverse=True)
    maximum = pancake[0]
    minute = 10

    for plate in range(1, maximum+1):
        movement = 0
        for p in pancake:
            if p <= plate:
                break
            movement += ceil(p/plate) - 1
        if minute > movement + plate:
            minute = movement + plate

    out.write("Case #%i: %i\n" % (case, minute))
    case += 1
