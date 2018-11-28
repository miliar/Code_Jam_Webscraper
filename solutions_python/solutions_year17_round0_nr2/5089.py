def isListSorted(l):
    return all(a <= b for a, b in zip(l[:-1], l[1:]))


def isSorted(n):
    num = [int(i) for i in str(n)]
    return isListSorted(num)

f2 = open('myfile', 'w')
  # python will convert \n to os.linesep
  # you can omit in most cases as the destructor will call it
i = 0
with open('B-small-attempt2.in') as f:
    for line in f:
        n = int(line)
        while True:
            if ( isSorted(n) == True ):
                f2.write ("Case #")
                f2.write(str(i))
                i = i +1
                f2.write(": ")
                f2.write(str(n))
                f2.write('\n')
                break
            n = n -1
f2.close()
