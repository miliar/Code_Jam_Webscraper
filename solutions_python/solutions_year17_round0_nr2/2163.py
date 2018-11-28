def listToInt(numList):
    return int(''.join(map(str,numList)))

def correct(n):
    if (n < 10):
        return n

    ant = 0
    numArray = [int(j) for j in str(n)]
    resp = []
    for i in range(len(numArray)):
        if (numArray[i] < ant):
            if (i == len(numArray) -1):
                resp.append(0)
                resp = listToInt(resp)
                return correct(resp - 1)
            else:
                resp[len(resp) - 1] = ant - 1
                ant = 9
                for j in range(len(numArray) - i):
                    resp.append(ant)

                return correct(listToInt(resp))

        else:
            ant = numArray[i]

        resp.append(ant)

    return listToInt(resp)


t = int(input())  # read a line with a single integer
for i in range(1, t + 1):
  n = int(input())  # read a list of integers

  n = correct(n)

  print("Case #" + str(i) + ": " + str(n))
