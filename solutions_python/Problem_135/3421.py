import os

f = open('a.in', 'r')
fw = open('a.out', 'w')

def answer(testCase):
    ans1 = int(testCase[0])
    testCase = testCase[1:]

    sqr1 = set(map(int, testCase[ans1-1].split()))
    testCase = testCase[4:]

    ans2 = int(testCase[0])
    testCase = testCase[1:]

    sqr2 = set(map(int, testCase[ans2-1].split()))
    testCase = testCase[4:]

    ans = sqr2.intersection(sqr1)
    length = len(ans)

    if length == 1:
        return str(ans.pop())
    elif length > 1:
        return "Bad magician!"
    else:
        return "Volunteer cheated!"

if __name__ == "__main__":
    i = 1
    n = int(f.readline()[:-1])
    testCase = f.read().split('\n')
    for i in range(1,n+1):
        fw.write("Case #%d: %s\n" % (i,answer(testCase[:10])))
        testCase = testCase[10:]
        i += 1

f.close()
fw.close()


