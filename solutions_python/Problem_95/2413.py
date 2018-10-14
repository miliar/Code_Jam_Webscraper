translist = [[0]*2]*27
translist[0]= [' ', ' ']
translist[1]= ['a', 'y']
translist[2]= ['b', 'n']
translist[3]= ['c', 'f']
translist[4]= ['d', 'i']
translist[5]= ['e', 'c']
translist[6]= ['f', 'w']
translist[7]= ['g', 'l']
translist[8]= ['h', 'b']
translist[9]= ['i', 'k']
translist[10]= ['j', 'u']
translist[11]= ['k', 'o']
translist[12]= ['l', 'm']
translist[13]= ['m', 'x']
translist[14]= ['n', 's']
translist[15]= ['o', 'e']
translist[16]= ['p', 'v']
translist[17]= ['q', 'z']
translist[18]= ['r', 'p']
translist[19]= ['s', 'd']
translist[20]= ['t', 'r']
translist[21]= ['u', 'j']
translist[22]= ['v', 'g']
translist[23]= ['w', 't']
translist[24]= ['x', 'h']
translist[25]= ['y', 'a']
translist[26]= ['z', 'q']
def transl(str):
    list1 = []
    lst = list(str)
    for l in range(len(lst)):
        for m in range(27):
            if lst[l] == translist[m][1]:
                list1.append(translist[m][0])
    return list1
t = open('A.in', 'r')
first = t.readline()
print(first)
w = int(first)
filer = open('test.txt', 'w')
for i in range(w):
    q = t.readline()
    m = transl(q)
    z = str(m)
    line = "Case #"+str((i+1))+": "+"".join(m)
    
    print(line)
