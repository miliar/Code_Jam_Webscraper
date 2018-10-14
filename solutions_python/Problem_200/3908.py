def tidy_number(n):
    digits = [int(i) for i in str(n)]
    digits_ = digits[::-1]

    for index, item in enumerate(digits_):
        if index == len(digits_)-1:
            break
        if item < digits_[index+1] or digits_[index+1] == 0:
            digits_[index+1] = digits_[index+1]-1
            digits_[index] = 9
            for i in range(index+1):
                digits_[i] = 9

    tidy = digits_[::-1]
    tidy = map(str, tidy)
    tidy = ''.join(tidy)
    tidy = int(tidy)

    return tidy

cases = []
for i in range(1,input()+1):
    cases.append(input())

for index, item in enumerate(cases):
    print("Case #%d: %d" % (index+1, tidy_number(item)))
