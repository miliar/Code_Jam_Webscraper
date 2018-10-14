
def main():
    with open('D-small-attempt1.in') as f:
        with open('output.txt', 'w+') as o:
            f.readline()
            casenum = 1
            for line in f:
                parts = line.split()
                X = int(parts[0])
                R = int(parts[1])
                C = int(parts[2])
                minE = min(R, C)
                winner = "GABRIEL"
                if X > R * C:
                    winner = "RICHARD"
                if X > R and X > C:
                    winner = "RICHARD"
                if X > 2 and minE <= 1:
                    winner = "RICHARD"
                if X > 3 and minE <= 2:
                    winner = "RICHARD"
                if (R*C) % X != 0:
                    winner = "RICHARD"
                o.write("Case #" + str(casenum) + ": " + winner + "\n")
                casenum += 1

if __name__ == "__main__":
    main()
