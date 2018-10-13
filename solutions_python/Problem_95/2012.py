# Problem A. Speaking in toungues #

l='abcdefghijklmnopqrstuvwxyz'
t='ynficwlbkuomxsevzpdrjgthaq'
File = open('Aout.txt', 'w')
T = int(raw_input())
for case in range(1,T+1):
    File.write("Case #"+str(case)+': ')
    G = str(raw_input())
    for letter in G:
        if letter==' ':
            File.write(letter)
        else:
            File.write(l[t.index(letter)])
    if case==T:
        break
    File.write('\n')
File.close()
