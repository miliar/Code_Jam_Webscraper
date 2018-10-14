def a():
    sq1 = []
    r1 = input() - 1
    for c in range(4): sq1 += [raw_input().split()]

    sq2 = []
    r2 = input() - 1
    for c in range(4): sq2 += [raw_input().split()]

    c = set(sq1[r1]) & set(sq2[r2])

    if len(c) == 1:
       return c.pop()
    elif len(c) == 0:
       return "Volunteer cheated!"
    else:
       return "Bad magician!"


def main():
    for c in range(1,input()+1):

        print "Case #%d:"%c, a()

if __name__ == '__main__':
    main()
