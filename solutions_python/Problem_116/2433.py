from functools import reduce

def check_hor(table):
    tablex = table.replace('T', 'X')
    tableo = table.replace('T', 'O')
    for i in (0, 4, 8, 12):
        if tablex[i:i+4] == "XXXX":
            return "X won"
        elif tableo[i:i+4] == "OOOO":
            return "O won"

def check_ver(table):
    tablex = table.replace('T', 'X')
    tableo = table.replace('T', 'O')
    for i in (0, 1, 2, 3):
        if tablex[i]+tablex[4+i]+tablex[8+i]+tablex[12+i] == "XXXX":
            return "X won"
        if tableo[i]+tableo[4+i]+tableo[8+i]+tableo[12+i] == "OOOO":
            return "O won"

def check_diag(table):
    tablex = table.replace('T', 'X')
    tableo = table.replace('T', 'O')
    if tablex[0]+tablex[5]+tablex[10]+tablex[15] == "XXXX":
        return "X won"
    if tablex[3]+tablex[6]+tablex[9]+tablex[12] == "XXXX":
        return "X won"
    if tableo[0]+tableo[5]+tableo[10]+tableo[15] == "OOOO":
        return "O won"
    if tableo[3]+tableo[6]+tableo[9]+tableo[12] == "OOOO":
        return "O won"

def check(table):
    checks = (check_hor(table), check_ver(table), check_diag(table))
    ends = ("X won", "O won")
    for end in ends:
        if end in checks:
            return end
    if "." in table:
        return "Game has not completed"
    return"Draw"
        
with open('A-large.in') as f:
    number = int(f.readline())
    for game in range(number):
        one = f.readline()
        two = f.readline()
        three = f.readline()
        four = f.readline()
        table = reduce(lambda x, y: x.strip()+y.strip(), (one, two, three, four))
        print("Case #{}: {}".format(game+1, check(table)))
        f.readline()
