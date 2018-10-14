__author__ = 'tmehta'

file = open('A-small-attempt4.in', 'r')
out = open('output_tic.txt', 'w')
number_of_cases = file.readline()
lines = file.readlines()


def check_game_status(four_lines):
    points_to_check = [(0, 0), (0, 1), (0, 2), (0, 3), (1, 0), (2, 0), (3, 0)]
    for points in points_to_check:
        start_char = four_lines[points[0]][points[1]]
        if start_char != ".":
            if points[0] == 0 and points[1] == 0:
                for x in [1, 2, 3]:
                    if (four_lines[x][points[1]] == start_char or four_lines[x][points[1]] == "T") and x == 3:
                        return str(start_char) + " won"
                    elif four_lines[x][points[1]] != start_char and four_lines[x][points[1]] != "T":
                        break
                for y in [1, 2, 3]:
                    if (four_lines[points[0]][y] == start_char or four_lines[points[0]][y] == "T") and y == 3:
                        return str(start_char) + " won"
                    elif four_lines[points[0]][y] != start_char and four_lines[points[0]][y] != "T":
                        break
                for x, y in zip([1, 2, 3], [1, 2, 3]):
                    if (four_lines[x][y] == start_char or four_lines[x][y] == "T") and x == 3 and y == 3:
                        return str(start_char) + " won"
                    elif four_lines[x][y] != start_char and four_lines[x][y] != "T":
                        break
            elif points[0] == 0:
                for x in [1, 2, 3]:
                    if (four_lines[x][points[1]] == start_char or four_lines[x][points[1]] == "T") and x == 3:
                        return str(start_char) + " won"
                    elif four_lines[x][points[1]] != start_char and four_lines[x][points[1]] != "T":
                        break
            elif points[1] == 0:
                for y in [1, 2, 3]:
                    if (four_lines[points[0]][y] == start_char or four_lines[points[0]][y] == "T") and y == 3:
                        return str(start_char) + " won"
                    elif four_lines[points[0]][y] != start_char and four_lines[points[0]][y] != "T":
                        break
    if four_lines[3][0] != "." and four_lines[0][3] != "." and four_lines[0][3] == four_lines[3][0]:
        if four_lines[2][1] == four_lines[3][0] and four_lines[1][2] == four_lines[3][0]:
            return str(four_lines[3][0]) + " won"
    for i in range(4):
        if "." in four_lines[i]:
            return "Game has not completed"
    return "Draw"


output = ""
for i in range(int(number_of_cases)):
    four_lines = lines[i * 5:i * 5 + 4]
    game_status = check_game_status(four_lines)
    if game_status == "0 won":
        game_status = "O won"
    output += "Case #" + str(i + 1) + ": " + game_status + "\n"

out.write(output)
