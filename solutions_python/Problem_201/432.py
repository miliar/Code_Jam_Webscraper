import os

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))


def read_inputs():
    number = 0
    items = []
    with open(os.path.join(__location__, "input.txt")) as f:
        content = f.readlines()
        content = [x.strip() for x in content]
        number = int(content[0])
        for i in range(0, number):
            line = content[i+1].split()
            items.append((int(line[0]), int(line[1])))
    return number, items



def get_min_max(n, k):
    if k == 1:
        return n//2, (n-1)//2

    if (n-1)%2 == 0:
        if (k-1)%2 == 0:
            return get_min_max((n-1)//2, (k-1)//2)
        else:
            return get_min_max((n-1)//2, (k-1)//2+1)
    else:
        if (k-1)%2 == 1:
            return get_min_max((n-1)//2+1, (k-1)//2+1)
        else:
            return get_min_max((n-1)//2, (k-1)//2)


def stalls():
    number, items = read_inputs()
    for i in range(0, len(items)):
        left, right = get_min_max(items[i][0], items[i][1])
        print('Case #'+ str(i+1) + ': ' + str(left) + ' ' + str(right))

stalls()