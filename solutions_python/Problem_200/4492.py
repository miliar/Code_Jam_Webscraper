def isTidy(x):
    last = 0
    for i,ch in enumerate(str(x)):
        curr = int(ch)
        if curr<last:
            return False,i
        last = curr
    return True,-1

assert isTidy(123456789)[0]
assert not isTidy(90)[0]
assert not isTidy(12321)[0]
assert isTidy(124799)[0]
assert isTidy(11124799)[0]
assert not isTidy(1024799)[0]
assert not isTidy(11243799)[0]

def tidyNumber(x):

    ret = isTidy(x)
    if ret[0] == True:
        return x
    untidyAt = ret[1]
    strNum = str(x)

    newStrNum = ''
    for i,char in enumerate(strNum):
        if i>= untidyAt:
            newStrNum += '0'
        else:
            newStrNum += strNum[i]

    num = int(newStrNum)
    num -=1
    if isTidy(num)[0]:
        return num
    else:
        return tidyNumber(num)

assert tidyNumber(11243799) == 11239999
assert tidyNumber(111) == 111
assert tidyNumber(9876) == 8999
assert tidyNumber(1234) == 1234
assert tidyNumber(1023) == 999
assert tidyNumber(111111111111111110) == 99999999999999999

def solveTidy(xs):
    return tidyNumber(xs[0])

if __name__ == "__main__":
    from codejam import CodeJam, parsers
    CodeJam(parsers.ints, solveTidy).main()