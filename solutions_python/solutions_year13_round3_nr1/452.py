import sys
sys.stdin = open("input.txt")
sys.stdout = open("output.txt", "w+")

T = input()


def is_consonant(word):
    for c in word:
        if c in "aeiou":
            return False
    return True


for t_case in range(1, T+1):
    word, N = raw_input().split(); N = int(N)

    answer = 0
    prev = -1
    length = len(word)

    for i in range(len(word) - N + 1):
        if is_consonant(word[i:i+N]):
            answer += (length - (i + N) + 1) * (i + 1)
            answer -= (prev + 1) * (length - (i + N) + 1)
            prev = i
    print "Case #%s: %s" % (t_case, answer)
