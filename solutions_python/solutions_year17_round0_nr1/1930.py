
class PancakeFlipper(object):
    def __init__(self):
        self.T = None
        self.TABLE_PANKCAKE = []
        self.NUM_ATTEMPTS = []
        self.read_input()

    def read_input(self):
        self.T = int(raw_input())
        for i in xrange(1, self.T + 1):
            line = str(raw_input())
            params = line.split(" ")
            TABLE = params[0]
            TABLE = [1 if pan == "+" else 0 for pan in TABLE]
            K = int(params[1])
            self.TABLE_PANKCAKE.append((TABLE, K))

    def is_all_happy(self, TABLE):
        for pancake in TABLE:
            if pancake == 0:
                return False
        return True

    def flip_pancake(self, TABLE, start, K):
        # print start, K
        if start+K > len(TABLE):
            return None

        for i in range(start, start+K):
            TABLE[i] = 1-TABLE[i]
        return TABLE

    def solve_pancake(self, TABLE, K):
        counter = 0
        # print TABLE, K
        while not self.is_all_happy(TABLE):
            for i in range(0, len(TABLE)):
                if TABLE[i] == 0:
                    TABLE = self.flip_pancake(TABLE, i, K)
                    if TABLE==None:
                        return None
                    break
            counter+=1
        return counter

    def solve(self):
        for table in self.TABLE_PANKCAKE:
            table, pancake = table
            NUM = self.solve_pancake(table, pancake)
            self.NUM_ATTEMPTS.append(NUM if NUM !=None else "IMPOSSIBLE")

    def print_stats(self):
        # print self.T
        # print self.TABLE_PANKCAKE
        # print self.NUM_ATTEMPTS

        with open("output.txt", "w") as f:
            for i, num in enumerate(self.NUM_ATTEMPTS):
                str =  "Case #{0}: {1}".format(i+1, num)
                print str
                f.write(str+"\n")


if __name__ == "__main__":
    PFObj = PancakeFlipper()
    PFObj.solve()
    PFObj.print_stats()
