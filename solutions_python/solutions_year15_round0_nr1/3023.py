import fileinput

if __name__ == "__main__":
    tc = fileinput.input()

    T = int(next(tc)) #number of test cases

    for case in range(1, T+1):
        inputString = next(tc)
        inputInts = inputString.split(" ")

        maxShy = inputInts[0]
        add = 0
        limit = 0

        stringNo = inputInts[1]
        stringNo = stringNo[:-1]

        shyLevel = 0

        for no in stringNo:
            no = int(no)
            if no > 0:
                if shyLevel > limit:
                    add += shyLevel - limit
                    limit += shyLevel - limit
                limit += no
            shyLevel += 1

        print("Case #%i: %s" % (case, add))