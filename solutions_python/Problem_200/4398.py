def check_if_tidy(an_int):

    int1 = an_int
    array1 = [int(x) for x in str(int1)]
    for k in range(0, len(array1) - 1):
        if array1[k] > array1[k + 1]:
            array1[k] -= 1
            for z in range(k + 1, len(array1)):
                array1[z] = 9
            str1 = ''.join(str(e) for e in array1)
            int1 = int(str1)
            return [int1, False]
    return [int1, True]


cases = int(input())
for i in range(1, cases + 1):
    m = [int(s) for s in input().split(" ")]
    my_int = int(m[0])
    is_found = False

    while not is_found:
        array2 = check_if_tidy(my_int)
        my_int = array2[0]
        if array2[1]:
            is_found = True


    print("Case #{}: {}".format(i, array2[0]))


