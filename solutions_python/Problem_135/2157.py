def main():
    cases = int(input())
    line = ''
    f = open('output.txt', 'w')
    for columbia in range(cases):
        case = columbia + 1
        row = int(input())
        line += 'Case #{:d}: '.format(case)
        for i in range(1, 5):
            if i == row:
                x = input().split(" ")
            else:
                y = input()
        for i in range(len(x)):
            x[i] = int(x[i])
        row = int(input())
        sets = set(x)
        for i in range(1, 5):
            if i == row:
                d = input().split(" ")
            else:
                y = input()
        for i in range(len(d)):
            d[i] = int(d[i])

        z =set(x).intersection(set(d))
        print(z)
        if len(z) == 0:
            line += 'Volunteer cheated!'
        elif len(z) == 1:
            line += str(list(z)[0])
        else:
            line += 'Bad magician!'
        line += '\n'
        f.write(line)
main()
