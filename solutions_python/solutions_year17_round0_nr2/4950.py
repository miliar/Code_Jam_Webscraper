import itertools

TC = int(input())
case = 1
for tc in range(TC):
    number= input()
    notFound = True
    while notFound:
        sort = sorted(number)
        flatten = ''.join(sort)
        if number != flatten:
            number = str(int(number)-1)
        else:
            notFound = False
    print("Case #%s: %s" %(case, number))
    case += 1
