FILE = 'C-small-1-attempt1.in'

def stall(k, n):
    lst = [n]

    while k > 1:
        big = max(lst)
        lst.remove(big)

        if big%2 == 0:
            lst += [int(big/2), int(big/2-1)]

        else:
            lst += [int(big//2), int(big//2)]

        k -= 1
        #print(lst)

    return lst
    
def main():
    file = open(FILE).readlines()

    for i in range(1, len(file)):
        line = file[i].strip().split()

        stalls = int(line[0])
        people = int(line[1])

        bathroom = stall(people, stalls)
        big = max(bathroom)

        final = []

        if big%2 == 0:
            final = [str(int(big/2)), str(int(big/2-1))]

        else:
            final = [str(int(big//2)), str(int(big//2))]

        print('Case #{}: {}'.format(i, ' '.join(final)))

main()
