import sys

def read_dataset(filename):
    data = open(filename)
    T = int(data.readline().strip())
    cases = []
    for i in range(0,T):
        N = int(data.readline().strip())
        cases.append(N)
        
    return T, cases

def resolve_set(dataset):
    T, cases = dataset
    numbers = []
    for i in range(0,T):
        N = cases[i]
        numbers.append(resolve(N))
    return numbers

def resolve(N):
    # import ipdb;ipdb.set_trace()
    tidy = False
    i = N
    while not tidy:
        tidy = isTidy(i)
        if tidy:
            return i
        else:
            i = nextNumber(i)
            
    return 0

def nextNumber(n):
    # import ipdb;ipdb.set_trace()
    number = map(int,list(str(n)))
    for i in range(0, len(number)):
        if number[i] > number[i+1]:
            number[i] -= 1
            for j in range(i+1, len(number)):
                number[j] = 9
            break
        else:
            i += 1

    n = ''.join(map(str, number))
    return int(n)


def isTidy(n):
    number = str(n)
    for i in range(0, len(number)-1):
        if int(number[i]) > int(number[i+1]):
            return False
    return True

def output(numbers, name):
    out = name[:-3] + '.out'
    file = open(out, "w")
    for i, n in enumerate(numbers):
        file.write("Case #" + str(i+1) +": " + str(n) + "\n")

def solution():
    name = sys.argv[1]
    dataset = read_dataset(name)
    numbers = resolve_set(dataset)
    output(numbers, name)

solution()