class Case:

    def __init__(self, d, P):
        self.d = d
        self.P = P


    def print_itself(self):
        print self.d, self.P


    #def remain_minute(self, P):
    #    return P[-1]


    def divide_max_by_2(self, P):
        tmp_max = P[-1]
        first = tmp_max/2
        second = tmp_max - first

        tmp_P =  P[:-1] + [first] + [second]
        tmp_P.sort()

        return tmp_P


    def divide_max_by_3(self, P):
        tmp_max = P[-1]
        first = tmp_max/3
        second = first
        third = tmp_max - first - second

        tmp_P =  P[:-1] + [first] + [second] + [third]
        tmp_P.sort()

        return tmp_P


    def find_quick(self, P):
        if P[-1] <= 3:
            return P[-1]

        return min(P[-1],
                   1 + self.find_quick(self.divide_max_by_2(P)),
                   2 + self.find_quick(self.divide_max_by_3(P)))

if __name__=="__main__":
    file_in = open("data/B-small-attempt1.in", "rt")
    file_out = open("data/B-small-attempt1.out", "wt")

    num_test_case = int(file_in.next())

    for count in range(num_test_case):
        d = int(file_in.next().strip())
        P = [int(p) for p in file_in.next().strip().split()]
        P.sort()

        if d is not len(P):
            print "Wrong input"
        tmp_case = Case(d, P)
        """
        tmp_case.print_itself()
        print tmp_case.find_quick(tmp_case.P)
        print
        """
        file_out.write("Case #" + str(count + 1) + ": " + str(tmp_case.find_quick(tmp_case.P)) + '\n')