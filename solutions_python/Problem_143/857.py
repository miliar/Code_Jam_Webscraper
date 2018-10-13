import sys


def QB(A, B, K):
    pairs = []
    for element in range(A):
        pairs += [(element, x) for x in range(B) if (int(x) & int(element)) < K]
    return len(pairs)


if __name__ == '__main__':
    text = open(sys.argv[1], "r").readlines()


    cases = int(text[0])

    solution = open("QBoutput.txt", "w")

    text = text[1:]
    for index, i in enumerate(range(cases)):
        a, b, k = text[0].replace("\n", "").split(" ")
        text = text[1:]
        result = QB(int(a), int(b), int(k))
        solution.write("Case #%s: %s\n" % (index+1, result))