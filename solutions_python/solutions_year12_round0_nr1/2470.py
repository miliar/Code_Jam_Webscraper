translate = {'e' : 'o', 'j' : 'u', 'p' : 'r', 'm' : 'l', 'y' : 'a', 's' : 'n', 'l' : 'g', 'c' : 'e',
             'k' : 'i', 'd' : 's', 'x' : 'm', 'v' : 'p', 'n' : 'b', 'r' : 't', 'i' : 'd', 'a' : 'y',
             'b' : 'h', 'f' : 'c', 'g' : 'v', 'h' : 'x', 'o' : 'k', 't' : 'w', 'u' : 'j', 'q' : 'z',
             'w' : 'f', ' ' : ' ', 'z' : 'q', '\n' : '\n'}

f = open ('A-small.IN')
new = open ('A-small Solution.OUT', 'w')
cases = int (f.readline())

for i, case in enumerate (range (cases)):
    current = f.readline ()
    n_line = ''
    new.write ('Case #' + str (i+1) + ': ')
    for l in current:
        n_line += translate [l]
    new.write (n_line)

new.close()
