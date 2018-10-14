# cd F:\pythonscripts\Code_jam



def bathroom():
    from math import ceil, floor

    def stalls(n, k):
        stalls = [n]
        if n == k:
            answer = "{} {}".format(0, 0)
            return answer

        k -= 1
        for num in range(k):
            max_st = max(stalls)
            for index, item in enumerate(stalls):
                if item == max_st:
                    stalls.pop(index)
                    divd = int(item//2)
                    stalls.append(divd)
                    if item % 2 == 0:
                        stalls.append(divd-1)
                    else:
                        stalls.append(divd)
                    break
        print (stalls)

        max_st = max(stalls)
        hi = int(floor(max_st/2))
        if max_st % 2 == 0:
            low = hi - 1
        else:
            low = hi

        answer = "{} {}".format(hi, low)
        return answer
    #print (answer)
    #print("")


    lines = [tuple(map(int,i.strip().split())) for i in tuple(open("C-small-1-attempt3.in", 'r'))]
    print (lines)
    print ("")
    testcases = lines[0][0]
    lines = lines[1:]



    #lines = [(18, 4), (4,2), (5,2), (6,2), (100,100), (1000, 1)]
    #testcases = len(lines)
    for testcase in range(1, testcases+1):
        case = "Case #{}: ".format(testcase)
        pair = lines[testcase-1]
        n = pair[0]
        k = pair[1]
        answer = stalls(n, k)
        #print ("")
        #print(n, k)
        print (answer)
        print ("")


        with open("answer.txt", "a") as f:
            f.writelines("{}{}\n".format(case, answer))
            f.close()


if __name__ == '__main__':
    bathroom()
