def main():
    file = open("A-small-attempt1.in")
    lines = file.read().split()
    file.close()
    number = int(lines[0])
    lines = lines[1:]
    result = ""
    for i in range(number):
        a = float(lines[2*i])
        b = float(lines[2*i+1])
        result += "Case #" + str(i + 1) + ": " + str(numRings(a, b)) + "\n"
    file = open("Asmall1.txt", 'w')
    file.write(result)
    file.close()

def area(r):
    return 2*r + 1


def numRings(r, t):
    c = 0
    while True:
        a = area(r)
        t = t - a
        if t < 0:
            break
        r += 2
        c += 1
    return c
