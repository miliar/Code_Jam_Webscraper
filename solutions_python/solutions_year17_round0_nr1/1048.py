def inp():
    result = []
    t = int(input())
    for i in range(t):
        s, k = input().split()
        result.append((input_to_array(s), int(k)))
    return result


def input_to_array(s):
    return [c == "+" for c in s]


def process(a, k):
    count = 0
    for i in range(len(a) - k + 1):
        if not a[i]:
            count += 1
            for j in range(k):
                a[i+j] = not a[i+j]
    for sign in a[len(a)-k:][::-1]:
        if not sign:
            return "IMPOSSIBLE"
    return count


def main():
    cases = inp()
    # print(cases)
    for i in range(len(cases)):
        print("Case #{}: {}".format(i+1, process(*cases[i])))

if __name__ == '__main__':
    main()
