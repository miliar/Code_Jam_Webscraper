with open("input.txt","r") as f:
    with open("output.txt","wt") as output:
        cases = int(f.readline())
        for c in range(cases):
            target = int(f.readline())
            target = [int(n) for n in str(target)]
            length = len(target)
            case = c + 1
            while True:
                flag = 1
                for l in range(length - 1):
                    if target[l] > target[l + 1]:
                        flag = 0
                        target[l] -= 1
                        for inner in range(l+1,length):
                            target[inner] = 9
                if flag:
                    break
            answer = str(int("".join([str(n) for n in target])))
            print("case #{0}: {1}".format(str(case),answer),file = output)
