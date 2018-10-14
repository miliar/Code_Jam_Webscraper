class Case:

    def __init__(self, X, R, C):
        self.X = X
        self.long_side = max(R, C)
        self.short_side = min(R, C)


    def print_itself(self):
        print self.X, self.long_side, self.short_side


    def can_make_hole(self):
        #if so, Richard wins
        if self.short_side == 1:
            return False

        if self.X >= 7:
            return True

        if self.X >= 2*self.short_side + 1:
            return True

        return False


    def is_not_multiple(self):
        #if not, Richard wins
        if (self.long_side*self.short_side)%self.X != 0:
            return True
        else:
            return False


    def can_be_outside(self):
        #if so, Richard winds
        if self.X > self.long_side:
            return True

        if self.short_side == 1:
            if self.X >= 3:
                return True
        else:
            if self.X - self.short_side + 1 > self.short_side:
                return True

        return False


    def check_conditions(self):
        if self.can_make_hole():
            print "can make hole"
            return True


        if self.can_be_outside():
            print "can be outside"
            return True


        if self.is_not_multiple():
            print "wrong grid size"
            return True

        return False


if __name__=="__main__":
    file_in = open("data/D-small-attempt7.in", "rt")
    file_out = open("data/D-small-attempt7.out", "wt")

    num_test_case = int(file_in.next())
    for count in range(num_test_case):
        tmp_list = file_in.next().split()
        tmp_X = int(tmp_list[0])
        tmp_R = int(tmp_list[1])
        tmp_C = int(tmp_list[2])


        print "Case ", count + 1
        tmp_case = Case(tmp_X, tmp_R, tmp_C)
        tmp_case.print_itself()
        richard_win = tmp_case.check_conditions()
        if richard_win:
            file_out.write("Case #" + str(count + 1) + ": " + "RICHARD\n")
        else:
            file_out.write("Case #" + str(count + 1) + ": " + "GABRIEL\n")

        print
