
def main():
    text_file = open("SmallOutput.in", "w")

    for i in range(int(input())):
        row = input().split()
        strCla = SortStr(row[0],int(row[1]))


        moves = strCla.sort()

        if (moves == 0):
            # print("Case #" + str(i + 1) + ": 0\n")
            text_file.write("Case #" + str(i + 1) + ": 0\n")
        elif(moves == None):
            # print("Case #" + str(i + 1) + ": IMPOSSIBLE\n")
            text_file.write("Case #" + str(i + 1) + ": IMPOSSIBLE\n")
        else:
            # print("Case #" + str(i + 1) + ": "+ str(moves) +"\n")
            text_file.write("Case #" + str(i + 1) + ": " + str(moves) + "\n")


class SortStr():
    def __init__(self,s,k):
        self.k = k
        self.s = s

    def getLastMinsOccur(self):
        return next((i for i, v in zip(range(len(self.s) - 1, -1, -1),
                                       reversed(self.s)) if v == '-'), None)

    def getLastPosOccur(self):
        return next((i for i, v in zip(range(len(self.s) - 1, -1, -1),
                                       reversed(self.s)) if v == '+'), 0)

    def sort(self,moves = 0):
        lastMins = self.getLastMinsOccur()
        lastPos = self.getLastPosOccur()

        if lastMins == None:
            return moves
        elif ( lastMins <= self.k  ) and (lastPos <= self.k ) and (len(self.s) < self.k) :
            return None
        else:
            moves += 1
            rev = self.reversIt(lastMins)
            if rev == False:
                return None
            return self.sort(moves)
        return moves

    def reversIt(self,lastMinPlace):
        s = ""
        for i, v in enumerate(self.s):
            if (lastMinPlace - self.k +1 ) < 0:
                return False
            if i >= (lastMinPlace - self.k +1 ) and i <= lastMinPlace:
                if v == "+":
                    s += "-"
                else:
                    s += "+"
            else:
                s += v
        self.s = s
        return True

if __name__ == '__main__':
    main()




















