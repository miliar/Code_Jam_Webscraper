def last_tidy(N):
    while N >= 1:
        if is_tidy(N):
            return N
        N -= 1
    return None


def is_tidy(x):
    digits = str(x)

    last_number = None
    for n in digits:
        if last_number is None:
            last_number = n
        elif n >= last_number:
            last_number = n
        else:
            return False
    return True

input = open("input.txt")
output = open("output.txt", "w+")

T = int(input.readline())
case = 1
while case <= T:
    output.write("Case #" + str(case) + ": " + str(last_tidy(int(input.readline()))) + "\n")
    case += 1
