def main():
    strings = open(input(prompt='input')).readlines()
    strings = strings[1:]

    with open(input(prompt='output'), 'a') as outputFile:
        for i in range(len(strings)):
            totals = strings[i].split()
            s = int(totals[1])
            p = int(totals[2])
            totals = [int(t) for t in totals[3:]]
            y = 0
            unsurp = 0
            surp = 0

            for t in totals:
                d = t % 3
                if d == 0:
                    unsurp = t//3
                    surp = t//3 + 1
                elif d == 1:
                    unsurp = t//3 + 1
                    surp = t//3 + 1
                elif d == 2:
                    unsurp = t//3 + 1
                    surp = t//3 + 2
                if unsurp >= p:
                    y += 1
                elif surp >= p and s > 0 and t > 1:
                    s -= 1
                    y += 1
            outputFile.write('Case #'+str(i+1)+': '+str(y)+'\n')

if __name__ == '__main__':
    main()