def func(S):
    string = list(S)

    queue = [[string, 0, ""]]

    while queue is not []:
        current = queue.pop(0)
        currentString = current[0]
        currentStart = current[1]
        currentNumber = current[2]

        if currentString is []:
            return currentNumber

        for i in range(currentStart, 10):
            try:
                res = removeNumber(currentString, currentNumber, i)

                if res[0] == []:
                    return res[2]

                queue.append(removeNumber(currentString, currentNumber, i))
            except ValueError:
                pass


def removeNumber(string, number, i):
    texts = ["ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"]
    text = texts[i]

    string = list(string)

    for c in text:
        string.remove(c)

    newNumber = number + str(i)

    return [string, i, newNumber]

T = int(input())

for t in range(T):
    S = input()
    print('Case #' + str(t+1) + ': ' + str(func(S)))

