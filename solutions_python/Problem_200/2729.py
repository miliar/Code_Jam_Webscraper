def tidyArray(array):
    if len(array) == 1:
        return array
    minimum = min(array)
    for index, value in enumerate( reversed(array) ):
        if value == minimum:
            last = len(array) - index - 1
            break
    while last:
        if array[last] != array[last-1]:
            break
        last -= 1
    if last == 0:
        return array[0:1] + tidyArray(array[1:])
    else:
        array[last-1] -= 1
        for i in range(last, len(array) ):
            array[i] = 9
        return tidyArray( array[:last] ) + array[last:]

def tidyNum(n):
    num = [ int(i) for i in n.strip() ]
    tidy = tidyArray(num)
    tidynum = "".join([str(t) for t in tidy])
    while tidynum[0] == '0':
        tidynum = tidynum[1:]
    return tidynum

sample = int(input() )
for case in range(1, sample+1):
    n = input()
    print("Case #{}: {}".format(case, tidyNum(n)) )