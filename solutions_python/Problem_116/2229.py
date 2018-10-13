# source code for GCJ2013 qualification round
# by Pengyu CHEN(cpy.prefers.you@gmail.com)
# COPYLEFT, ALL WRONGS RESERVED.

def win(s, p):
    if any(map(lambda x: x == p * 4, s)):
        return True
    elif any(map(lambda x: all(map(lambda y: s[y][x] == p, range(4))), range(4))):
        return True
    elif all(map(lambda x: s[x][x] == p, range(4))):
        return True
    elif all(map(lambda x: s[3 - x][x] == p, range(4))):
        return True
    return False

def main():
    T = int(input())
    for t in range(T):
        s = [input() for i in range(5)]
        x = list(map(lambda x: x[:].replace("T", "X"), s))
        o = list(map(lambda x: x[:].replace("T", "O"), s))
        if win(x, "X"):
            msg = "X won"
        elif win(o, "O"):
            msg = "O won"
        elif "".join(s).count(".") > 0:
            msg = "Game has not completed"
        else:
            msg = "Draw"
        print("Case #%d: %s" %(t + 1, msg))
    pass

if __name__ == "__main__":
    main()
