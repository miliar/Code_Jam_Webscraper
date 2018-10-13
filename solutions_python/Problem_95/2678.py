trans = [25, 8, 5, 19, 15, 3, 22, 24, 4, 21, 9, 7, 12, 2, 11, 18, 26, 20, 14, 23, 10, 16, 6, 13, 1, 17]
numLines = int(input())

for i in range(numLines):
    line = input()
    line_out = "Case #" + str(i + 1) + ": "
    for char in line:
        if char != ' ':
            line_out += chr(trans[ord(char) - ord('a')] + ord('a') - 1)
        else:
            line_out += ' '

    print(line_out)
