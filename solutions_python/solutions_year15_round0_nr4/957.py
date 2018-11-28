FILEPATH_INPUT = r"C:\Yam\input.txt"
FILEPATH_OUTPUT = r"C:\Yam\output.txt"
with open(FILEPATH_INPUT, 'rb') as reader:
    content = reader.read().splitlines()
writer = open(FILEPATH_OUTPUT, 'wb')

tests = int(content[0])
reader = 1
while reader <= tests:
    line = content[reader]
    ##################
    X, R, C = map(int, line.split())
    if X == 1:
        winner = "GABRIEL"
    elif X == 2:
        winner = ("GABRIEL" if (R*C)%2 == 0 else "RICHARD")
    elif X == 3:
        if R * C == 3:
            winner = "RICHARD"
        elif (R*C) % 3 == 0:
            winner = "GABRIEL"
        else:
            winner = "RICHARD"
    elif X == 4:
        winner = ("GABRIEL" if R*C in (16, 12) else "RICHARD")
    ##################
    writer.write("Case #{x}: {y}\n".format(x=reader, y=winner))
    reader += 1
    
writer.close()