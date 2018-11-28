def works(size, rows, cols):
    if size == 1:
        return True
    if (rows * cols) % size != 0:
        return False
    if size == 2:
        return True
    if size == 3:
        if rows * cols == 3:
            return False
        if rows * cols == 6:
            return True
        if rows * cols == 9:
            return True
        if rows * cols == 12:
            return True
    if size == 4:
        if (rows < 4) & (cols < 4):
            return False
        if rows * cols == 4:
            return False
        if rows * cols == 8:
            return False
        if rows * cols == 12:
            return True
        if rows * cols == 16:
            return True



with open('D-small-attempt1.in') as f:
    stuff = f.readlines()

cases = 1

while cases < len(stuff):
    string = list(map(int, stuff[cases].split()))
    if works(string[0], string[1], string[2]):
        print("Case #"+str(cases)+": GABRIEL")
    else:
        print("Case #"+str(cases)+": RICHARD")
    cases += 1