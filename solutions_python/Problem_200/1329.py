import numpy

tc = int(input())

for i in range(tc):
    arr = input()
    while True:
        answer = numpy.array(list(arr))
        size = len(answer)
        flag = False
        for j in range(1, size):
            if not answer[j - 1] <= answer[j]:
                answer[j - 1] = int(answer[j - 1]) - 1
                answer[j:] = 9
                flag = True
                arr = list(answer)
                break
        if flag is False:
            break
    print('Case #{}: {}'.format(i + 1, int(''.join(answer))))
