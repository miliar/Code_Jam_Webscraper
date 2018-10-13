n = int(input())

i = 0
while i < n:
    i += 1

    num = input()

    a = [int(x) for x in list(num)]

    for j in reversed(range(len(num) - 1)):

        if a[j + 1] < a[j]:
            a[j] -= 1

            for k in range(j+1, len(a)):
                a[k] = 9

    a = int(''.join([str(x) for x in a]))

    print("Case #" + str(i) + ": " + str(a))
