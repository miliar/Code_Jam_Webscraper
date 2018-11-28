import fileinput

def fuckMagician(A,B):
    A = sorted(A)
    B = sorted(B)
    i = 0
    j = 0
    val = -1
    while i < 4 and j < 4:
        if A[i] == B[j]:
            if val != -1:
                return "Bad magician!"
            else:
                val = A[i]
                i+=1
                j+=1
        elif A[i] > B[j]:
            j += 1
        else:
            i += 1
    if val == -1:
        return "Volunteer cheated!"
    else:
        return str(val)


def main():
    fin = fileinput.input()
    T = int(next(fin)) # number of test cases
    for case in range(1, T+1):
        selected = int(next(fin))
        for i in range(1,5):
            if i == selected:
                A = [int(x) for x in next(fin).split(" ")]
            else:
                next(fin)
        selected = int(next(fin))
        for i in range(1,5):
            if i == selected:
                B = [int(x) for x in next(fin).split(" ")]
            else:
                next(fin)
        print("Case #{}: {}".format(case, fuckMagician(A,B)))
    fin.close()

if __name__ == '__main__':
    main()
