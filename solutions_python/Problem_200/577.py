def maxTidy(s):
    stack = list(s)
    stack = [int(i) for i in stack]
    num_digits = len(stack)
    result = []
    while len(stack) != 0:
        if len(stack) == 1:
            result.append(stack.pop())
            break
        last = stack.pop()
        first = stack.pop()
        if last < first:
            result = [9 for i in result]
            result.append(9)
            stack.append(first - 1)
        else:
            result.append(last)
            stack.append(first)
    if result[-1] == 0:
        ret = 1
        for j in range(num_digits - 1):
            ret *= 10
        return ret - 1
    else:
        ret, factor = 0, 1
        while len(result) != 0:
            ret += factor * result.pop(0)
            factor *= 10
        return ret


def __main__():
    l = int(input())
    for i in range(l):
        max = maxTidy(input())
        print("Case #{}: {}".format(i + 1, max))

__main__()