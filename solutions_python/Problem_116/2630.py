from pprint import pprint as pp

DEBUG = 0

f = open("code_jam_file")
data = f.readlines()
prob_size = len(data) / int(data[0])
if DEBUG:
    print "lines: ", len(data), "prob_size:", prob_size, "problems:", data[0]



def check(s, l):
    #vertical
    for x in range(4):
        h_total = 0
        v_total = 0
        for y in range(4):
            if l[x][y] == s or l[x][y] == "T":
                h_total += 1
            if l[y][x] == s or l[y][x] == "T":
                v_total += 1
        if v_total == 4 or h_total == 4:
            return True
    d1_total = 0
    d2_total = 0
    for x in range(4):
        if l[x][x] == s or l[x][x] == "T":
            d1_total += 1
        if l[x][3-x] == s or l[x][3-x] == "T":
            d2_total +=1
    if d2_total == 4 or d1_total == 4:
        return True

def check_draw(l):
    for e in l:
        for p in e:
            if p == ".":
                return "Game has not completed"
    return "Draw"

for x in range(1,len(data), 5):
    c_num = (x-1)/5 +1
    # print c_num
    l = []
    for i in range(4):
        l.append(data[x+i].strip("\n"))
    # pp(l)
    # l is initialized
    s = "Case #" + str(c_num) + ": "
    if check("X", l):
        s += "X won"
    elif check("O", l):
        s += "O won"
    else:
        s += check_draw(l)
    print s



#1-4, 6-9, 11-14

# ans = pick_two(data[x], data[x + 2])
# def pick_two(value, items):
#     value = int(value)
#     items = map(int, items.strip("\n").split(" "))
#     # print value, items
#     for i in range(len(items)):
#         for j in range(i,len(items)):
#             if items[i] + items[j] == value:
#                 if i != j:
#                     return [i + 1, j + 1]
