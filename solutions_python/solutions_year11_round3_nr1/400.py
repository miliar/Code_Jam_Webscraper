import sys

f = open(sys.argv[1], "r")

T = (int)(f.readline())

for t in range(1, T + 1):
    R, C = map(int, f.readline().split(" "))
    picture = []
    for r in range(R):
        line = f.readline().strip()
        row = []
        for char in line:
            row.append(char)
        picture.append(row)

    okay = True
    for r in range(R):
        for c in range(C):
            if picture[r][c] == "#":
                if r + 1 == R or c + 1 == C:
                    okay = False
                    break;
                if picture[r][c+1] == ".":
                    okay = False
                if picture[r+1][c] == ".":
                    okay = False
                if picture[r+1][c+1] == ".":
                    okay = False
                              
                picture[r][c] = "/"
                picture[r][c+1] = "\\"
                picture[r+1][c] = "\\"
                picture[r+1][c+1] = "/"

    print ("Case #" + str(t) + ":")
    if okay:
        for row in picture:
            print("".join(row))
    else:
        print ("Impossible")

f.close()
