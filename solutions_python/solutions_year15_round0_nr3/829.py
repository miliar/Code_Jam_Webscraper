import sys


def inverse(a, total, is_plus):
    if a == '1' and total == '1' and is_plus:
        return '1'
    elif a == 'i' and total == 'i' and is_plus:
        return 'i'
    elif a == 'j' and total == 'j' and is_plus:
        return 'j'
    elif a == 'k' and total == 'k' and is_plus:
        return 'k'
    elif a == '1' and total == 'i' and is_plus:
        return '1'
    elif a == 'i' and total == '1' and not is_plus:
        return 'i'
    elif a == 'j' and total == 'k' and is_plus:
        return 'j'
    elif a == 'k' and total == 'j' and not is_plus:
        return 'k'

    elif a == '1' and total == 'j' and is_plus:
        return '1'
    elif a == 'i' and total == 'k' and not is_plus:
        return 'i'
    elif a == 'j' and total == '1' and not is_plus:
        return 'j'
    elif a == 'k' and total == 'i' and is_plus:
        return 'k'

    elif a == '1' and total == 'k' and is_plus:
        return '1'
    elif a == 'i' and total == 'j' and is_plus:
        return 'i'
    elif a == 'j' and total == 'i' and not is_plus:
        return 'j'
    elif a == 'k' and total == '1' and not is_plus:
        return 'k'
    return '1'


def getChar(a, b, is_plus):
    if a == '1' and b == '1':
        return '1', is_plus
    elif a == '1' and b == 'i':
        return 'i', is_plus
    elif a == '1' and b == 'j':
        return 'j', is_plus
    elif a == '1' and b == 'k':
        return 'k', is_plus
    elif a == 'i' and b == '1':
        return 'i', is_plus
    elif a == 'i' and b == 'i':
        return '1', not is_plus
    elif a == 'i' and b == 'j':
        return 'k', is_plus
    elif a == 'i' and b == 'k':
        return 'j', not is_plus
    elif a == 'j' and b == '1':
        return 'j', is_plus
    elif a == 'j' and b == 'i':
        return 'k', not is_plus
    elif a == 'j' and b == 'j':
        return '1', not is_plus
    elif a == 'j' and b == 'k':
        return 'i', is_plus
    elif a == 'k' and b == '1':
        return 'k', is_plus
    elif a == 'k' and b == 'i':
        return 'j', is_plus
    elif a == 'k' and b == 'j':
        return 'i', not is_plus
    elif a == 'k' and b == 'k':
        return '1', not is_plus
    return '1', is_plus
# rule = \
# {
# '1':{'1': ('1', True), 'i': ('i', True), 'j': ('j', True), 'k': ('k', True)},
# 'i':{'1': ('i', True), 'i': ('1', False), 'j': ('k', True), 'k': ('j', False)},
# 'j':{'1': ('j', True), 'i': ('k', False), 'j': ('1', False), 'k': ('i', True)},
# 'k':{'1': ('k', True), 'i': ('j', True), 'j': ('i', False), 'k': ('1', False)},
# }
# def getChar(a, b, is_plus):
#     char, sign = rule[a][b]
#     return char, sign == is_plus

# def makeK(string):
#     # print("@ makeK string: " + string)
#     curChar = '1'
#     is_plus = True
#     for i in range(len(string)):
#         curChar, is_plus = getChar(curChar, string[i], is_plus)
#     if curChar == 'k' and is_plus:
#         # print("in makeK: " + str(i))
#         return True
#     return False

def makeK(string):
    # print("@ makeK string: " + string)
    curChar = '1'
    is_plus = True
    for i in range(len(string)):
        curChar, is_plus = getChar(curChar, string[i], is_plus)
    if curChar == 'k' and is_plus:
        # print("in makeK: " + str(i))
        return True
    return False

def makeJ(string):
    # print("@ makeJ string: " + string)
    curChar = '1'
    is_plus = True
    for i in range(len(string)):
        curChar, is_plus = getChar(curChar, string[i], is_plus)
        if curChar == 'j' and is_plus:
            # print("in makeJ: " + str(i))
            if makeK(string[i+1:]):
                return True
            else:
                return False
    return False

def makeI(string):
    # print("@ makeI string: " + string)
    curChar = '1'
    is_plus = True
    for i in range(len(string)):
        curChar, is_plus = getChar(curChar, string[i], is_plus)
        # print("!!!makeI: i: " + str(i) + ", string[i]: " + string[i] + ", curChar: " + curChar)
        if curChar == 'i' and is_plus:
            # print("in makeI: " + str(i))
            if makeJ(string[i+1:]):
                return True
            else:
                continue
    return False


def getString(repeat, string):
    out_str = ''.join([string for n in range(repeat)])
    return out_str

def solve(charLen, repeat, string):
    totalString = getString(repeat, string)
    if makeI(totalString):
        return "YES"
    else:
        return "NO"

def start():
    f = sys.stdin
    # f = open('C-small-attempt1.in', 'r')
    # f = open('input.in', 'r')
    of = open('output.out', 'w')
    tn = int(f.readline())
    for t in range(1, tn+1):
        firstLine = list(map(int, f.readline().rstrip().split()))
        charLen = firstLine[0]
        repeat = firstLine[1]
        string = f.readline().rstrip()
        # print("Case #{0}: {1}\n".format(t, solve(charLen, repeat, string)))
        of.write("Case #{0}: {1}\n".format(t, solve(charLen, repeat, string)))
    f.close()
    of.close()

start()
# print(getChar('k', 'j', False))