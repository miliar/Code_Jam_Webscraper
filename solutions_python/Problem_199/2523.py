def main():
    with open("A-large.in", 'r') as file, open("output.txt", 'w') as out:
        cases = file.readline()

        for case in range(int(cases)):
            line = file.readline()
            s = list(line.split(' ')[0])
            k = int(line.split(' ')[1])
            flips = 0

            for i in range(len(s)-k+1):
                if s[i] == '-':
                    for j in range(k):
                        if s[i+j] == '-':
                            s[i+j] = '+'
                        else:
                            s[i+j] = '-'
                    flips = flips + 1

            result = str(flips)

            for i in s[-k:]:
                if i != '+':
                    result = 'IMPOSSIBLE'

            out.write("Case #" + str(case+1) + ": " + result + "\n")

if __name__ == "__main__":
    main()
