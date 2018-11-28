import sys, os

t = int(sys.stdin.readline())
for i in range(t):
    combo = {}
    opposed = []
    s = sys.stdin.readline().split()
    for j in range(int(s.pop(0))):
        scombo = s.pop(j)
        combo[scombo[0:2]] = scombo[2]
        combo[scombo[1] + scombo[0]] = scombo[2]
    for k in range(int(s.pop(0))):
        opposed.append(s.pop(j))
    command = ""
    N = int(s.pop(0))
    spell = s[0]
    for l in range(int(N)):
        command += spell[l]
        if len(command) > 1:
            combotest = command[len(command)-2:len(command)]
            if combotest in combo:
                command = command.replace(combotest, combo[combotest])
            for first in command:
                for second in command:
                    if first+second in opposed:
                        command = ""
                        break
    output = []
    for l in command:
        output.append(l)
    print ("Case #%d:" % (i+1), "[" + ", ".join(output) + "]")