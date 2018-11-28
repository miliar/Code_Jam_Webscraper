def main():
    with open("B-large.in", 'r') as file, open("output.txt", 'w') as out:
        cases = file.readline()

        for case in range(int(cases)):
            n = list(file.readline().strip())

            done = False
            i = 0
            j = 0

            while not done and i < len(n):
                while j < len(n) and int(n[j]) == int(n[i]):
                    j = j+1
                if j >= len(n):
                    done = True
                else:
                    if int(n[j]) > int(n[i]):
                        i = j
                    else:
                        n[i] = str(int(n[i])-1)
                        for k in range(i+1, len(n)):
                            n[k] = '9'
                        done = True

            out.write("Case #" + str(case+1) + ": " + str(int(''.join(n))) + "\n")

if __name__ == "__main__":
    main()
