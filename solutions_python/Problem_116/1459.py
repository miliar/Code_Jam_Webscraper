def find4(table):
    for i in xrange(4):
        if table[i] == list("*" * 4):
            return True
    return [table[i][i] for i in xrange(4)] == list("*" * 4)

def calc(table, mark):
    table = [list(i.replace(mark, "*").replace("T", "*")) for i in table]
    return find4(table) or find4([list(i[::-1]) for i in zip(*table)])

def ans(table):
    if calc(table, "O"):
        return "O won"
    elif calc(table, "X"):
        return "X won"
    elif any(["." in x for x in table]):
        return "Game has not completed"
    else:
        return "Draw"

def main():
    for t in xrange(input()):
        table = []
        for i in xrange(4):
            table.append(raw_input())
        print "Case #%d:" % (t + 1), ans(table)
        try:
            raw_input()
        except EOFError:
            pass

if __name__ == "__main__":
    main()
