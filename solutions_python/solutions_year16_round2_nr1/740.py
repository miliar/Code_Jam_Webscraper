def x(s):
    return ord(s) - 64

def digits(s):
    letters = [0]*27
    nums = [0]*10
    for letter in s:
        letters[x(letter)] += 1

    word = 'ZERO'
    key = 'Z'
    val = letters[x(key)]
    nums[0] += val
    for letter in word:
        letters[x(letter)] -= val

    word = 'SIX'
    key = 'X'
    val = letters[x(key)]
    nums[6] += val
    for letter in word:
        letters[x(letter)] -= val

    word = 'EIGHT'
    key = 'G'
    val = letters[x(key)]
    nums[8] += val
    for letter in word:
        letters[x(letter)] -= val

    word = 'TWO'
    key = 'W'
    val = letters[x(key)]
    nums[2] += val
    for letter in word:
        letters[x(letter)] -= val

    word = 'THREE'
    key = 'T'
    val = letters[x(key)]
    nums[3] += val
    for letter in word:
        letters[x(letter)] -= val

    word = 'SEVEN'
    key = 'S'
    val = letters[x(key)]
    nums[7] += val
    for letter in word:
        letters[x(letter)] -= val    

    word = 'FIVE'
    key = 'V'
    val = letters[x(key)]
    nums[5] += val
    for letter in word:
        letters[x(letter)] -= val

    word = 'FOUR'
    key = 'F'
    val = letters[x(key)]
    nums[4] += val
    for letter in word:
        letters[x(letter)] -= val
        
    word = 'NINE'
    key = 'I'
    val = letters[x(key)]
    nums[9] += val
    for letter in word:
        letters[x(letter)] -= val

    word = 'ONE'
    key = 'O'
    val = letters[x(key)]
    nums[1] += val
    for letter in word:
        letters[x(letter)] -= val

    ans = ''
    for i in range(0,10):
        ans += str(i)*nums[i]

    return ans

def main():
    n = int(input())
    ans = []
    for case in range(0,n):
        s = input()
        ans += [digits(s)]

    for i in range(0,n):
        print("Case #" + str(i+1) + ": " + ans[i])
