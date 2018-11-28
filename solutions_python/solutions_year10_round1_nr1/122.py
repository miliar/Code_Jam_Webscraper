#!/usr/bin/python
import sys

def reduce(row, size):
    row = row.replace(".", "")
    row = "."*(size - len(row)) + row
    return row

def main():
    infile = open(sys.argv[1])
    cases = int(infile.readline())
    sides = {"R":"red", "B":"blue"}
    for case in range(cases):
        field = []
        size, rows = [int(x) for x in infile.readline().split()]
        for i in range(size):
            field.append(infile.readline().strip())
        
        #print "\n".join(field)
        
        # Rotate
        for i in range(size):
            field[i] = reduce(field[i], size)
        #print "\n".join(field)
        
        # Check for 
        win = set()
        B_rows = "B"*rows
        R_rows = "R"*rows
        for i in range(size):
            if B_rows in field[i]:
                win.add("blue")
            if R_rows in field[i]:
                win.add("red")
        for i in range(size-rows+1):
            for col in range(size):
                for side in ["R", "B"]:
                    if field[i][col] == side:
                        # Search downward, slopeing left, right, and not at all
                        left = right = middle = True
                        for j in range(rows):
                            if middle and field[i+j][col] != side:
                                middle = False
                            if right and (col+j >= size or field[i+j][col+j] != side):
                                right = False
                            if left and (col-j < 0 or field[i+j][col-j] != side):
                                left = False
                        if left or right or middle:
                            win.add(sides[side])
        if "red" in win and "blue" in win:
            win = "Both"
        elif "red" in win:
            win = "Red"
        elif "blue" in win:
            win = "Blue"
        else:
            win = "Neither"
        print "Case #%d: %s" % (case+1, win)
        
if __name__ == "__main__":
    main()