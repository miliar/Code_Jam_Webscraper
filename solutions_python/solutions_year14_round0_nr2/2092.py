def main():
    cases = int(input())
    line = ''
    file = open('output.txt', 'w')
    for columbia in range(cases):
        case = columbia + 1
        line += 'Case #{:d}: '.format(case)
        ln = input().split(" ")
        t = 0
        C = float(ln[0])
        F = float(ln[1])
        f = 2
        X = float(ln[2])
        while (X/f > (C/f + (X)/(F+f))):
            t += C/f
            f = f+F
        line += "{:.7f}".format(t+X/f)
        line += '\n'
    file.write(line)
main()
