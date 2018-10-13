import sys

def f(case, a, b):
    count = 0
    for n in range(a, b + 1):
        n = str(n)
        k = len(n)
        for i in range(0, k):
            head = n[0 : i + 1]
            tail = n[i + 1 : k + 1]
            m = tail + head
            if int(n) < int(m) and a <= int(m) <= b:
                count += 1
    print "Case #" + str(case) + ": " + str(count)

def run():
    lines = sys.stdin.readlines()
    lines_of_input = int(lines[0])
    case = 1
    for line in lines[1:]:
        parts = line.split(" ")
        f(case, int(parts[0]), int(parts[1]))
        case += 1

run()
