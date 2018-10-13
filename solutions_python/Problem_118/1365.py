import math
def isPalindrome(a):
    strNum = str(a)
    for i in range(len(strNum)/2):
        if strNum[i] != strNum[-(i+1)]:
            return False
    return True

def isPerfectSquare(a):
    floor = int(math.floor(math.sqrt(a)))
    while (floor * floor < a):
        floor += 1
    if floor * floor == a:
        return (True, floor)
    return (False, None)

def find(A, B):
    count = 0
    for i in range(A, B + 1):
        if isPalindrome(i):
            (result, root) = isPerfectSquare(i)
            if result and isPalindrome(root):
                count += 1
    return count

def main():
    output = open('3.out', 'w')
    with open('C-small-attempt0.in', 'r') as input:
        cases = int(input.readline().split('\n')[0])

        for case in range(1, cases + 1):
            ls = filter(None, input.readline().split(' '))
            result = find(int(ls[0]), int(ls[1]))
            output.write('Case #{0}: {1}\n'.format(case, result))
    output.close()

if __name__ == "__main__":
    main()

