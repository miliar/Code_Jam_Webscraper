def whoWonPlayerList(playerList):
    if ("O" in playerList and "X" in playerList) or "." in playerList:
        return ""
    if "O" in playerList:
        return "O won"
    else:
        return "X won"

def whoWon(check):
    for i in xrange(0, len(check)):
        winner = whoWonPlayerList(list(set(check[i])))
        if winner != "":
            return winner

    for i in xrange(0, len(check[0])):
        winner = whoWonPlayerList(list(set([_[i] for _ in check])))
        if winner != "":
            return winner

    winner = whoWonPlayerList(list(set([check[0][0], check[1][1], check[2][2], check[3][3]])))
    if winner != "":
        return winner

    winner = whoWonPlayerList(list(set([check[0][3], check[1][2], check[2][1], check[3][0]])))
    if winner != "":
        return winner


    for line in check:
        if "." in line:
            return "Game has not completed"

    return "Draw"






if __name__ == '__main__':
    size = int(raw_input())
    checkboards = [[]]

    nb = 0
    while nb != size:
        line = raw_input()
        if line != "":
            checkboards[-1].append(line)
        else:
            checkboards.append([])
            nb += 1

    del checkboards[-1]

    for i in xrange(0, size):
        print "Case #" + str(i+1) + ": " + whoWon(checkboards[i])
