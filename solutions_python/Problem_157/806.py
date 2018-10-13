import sys

sys.stdin = open("input.txt", "r")
sys.stdout = open("output.txt", "w")

matrix = {"1": {"1": "1", "i": "i", "j": "j", "k": "k"},
          "i": {"1": "i", "i": "-1", "j": "k", "k": "-j"},
          "j": {"1": "j", "i": "-k", "j": "-1", "k": "i"},
          "k": {"1": "k", "i": "j", "j": "-i", "k": "-1"},
          "-1": {"1": "-1", "i": "-i", "j": "-j", "k": "-k"},
          "-i": {"1": "-i", "i": "1", "j": "-k", "k": "j"},
          "-j": {"1": "-j", "i": "k", "j": "1", "k": "-i"},
          "-k": {"1": "-k", "i": "-j", "j": "i", "k": "1"}}
goals = ['i', 'j', 'last']

n = int(raw_input())

for c in range(n):
    answ = "NO"

    l, x = map(int, raw_input().split())
    s = raw_input()
    current = '1'
    goal = 0
    for v in range(x*l):
        current = matrix[current][s[v % l]]
        if goal != 2:
            if current == goals[goal]:
                goal += 1
                current = '1'
    if goal == 2 and current == 'k':
        answ = "YES"
    print "Case #"+str(c+1)+": "+answ