def try_strategy(ken, naomi):
    result = 0

    while (len(naomi) > 0):
        found = min(ken)

        for obj in ken:
            if (obj > naomi[0]):
                if (obj < found) or (found < naomi[0]):
                    found = obj

        if (found > naomi[0]):
            result += 1

        naomi.remove(naomi[0])
        ken.remove(found)

    return result

def parse_input(filename="D.in"):
    f = open(filename)

    ncases = int(f.readline())
    for ncase in range(ncases):
        n = int(f.readline())
        naomi = map(float, f.readline().split())
        ken = map(float, f.readline().split())
        deceipt, war = try_strategy(list(naomi), list(ken)), n - try_strategy(list(ken), list(naomi))
        print "Case #" + str(ncase + 1) + ": " + str(deceipt) + " " + str(war)

    f.close()

if __name__ == "__main__":
    parse_input("D-large.in")