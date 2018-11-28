
def magic(grid1, row1, grid2, row2):
    num1 = set(grid1[row1])
    num2 = set(grid2[row2])
    k = num1 & num2
    if len(k) == 1:
        return str(k.pop())
    elif len(k) > 1:
        return "Bad magician!"
    else:
        return "Volunteer cheated!"
        
t = input()
for case in range(1,t+1):
    n1 = input() - 1
    grid1 = [map(int, raw_input().split()) for _ in range(4)]
    n2 = input() - 1
    grid2 = [map(int, raw_input().split()) for _ in range(4)]
    print "Case #%d: %s" % (case, magic(grid1, n1, grid2, n2))
    