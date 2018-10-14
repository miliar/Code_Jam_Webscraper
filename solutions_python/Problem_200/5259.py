solutionList = []

def main():
    checker = False
    with open('B-small-attempt0.in') as f:
        for line in f:
            line = (line.strip())
            if not checker:
                checker = True
                continue
            answer = tidy(line)
            solutionList.append(answer)
        with open("Big-tidy-numbers.out", "w") as text_file:
            i = 1
            for n in solutionList:
                text_file.write("Case #" + str(i) + ": " + str(n) + "\n")
                i += 1


def tidy(s):
    test = 0
    if len(s) == 1:
        return s
    if len(s) < 5:
        intTidy = int(s)
        j = 0
        for i in range(0, len(s)):
            j = i + 1
            nowInt = s[i]
            try:
                nextInt = s[ i +1]
            except:
                return
            if (nowInt <= nextInt):
                if j+ 1 == len(s) and nowInt <= nextInt:
                    test += 1
                    return s
                continue
            else:
                s = str(intTidy - 1)
                return tidy(s)

main()
