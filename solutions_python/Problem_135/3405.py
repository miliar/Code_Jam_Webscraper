

class MagicTrick():

    file_name = 'A-small-attempt0.in'
    output_name = 'output.txt'

    def as_nums(self, spaced_nums):
        """
        :type spaced_nums : str
        """
        nums = []
        for string_num in spaced_nums.split(' '):
            nums.append(int(string_num))
        return nums

    def solve(self, ans_1,rows_1,ans_2,rows_2):
        possibles = set()
        for i in rows_1[ans_1-1]:
            possibles.add(i)

        actuals = []
        for i in rows_2[ans_2-1]:
            if i in possibles:
                actuals.append(i)

        if not actuals:
            return "Volunteer cheated!"
        elif len(actuals) == 1:
            return "%s" % actuals[0]
        else:
            return "Bad magician!"

    def read_input(self):
        f = open(MagicTrick.file_name, 'r')
        w = open(MagicTrick.output_name, 'w')
        line = f.readline()
        cases = int(line.strip())
        print "there are %s cases" % cases
        for i in xrange(cases):
            ans_1 = int(f.readline().strip())
            rows_1= []
            rows_1.append(self.as_nums(f.readline().strip()))
            rows_1.append(self.as_nums(f.readline().strip()))
            rows_1.append(self.as_nums(f.readline().strip()))
            rows_1.append(self.as_nums(f.readline().strip()))

            ans_2 = int(f.readline().strip())
            rows_2= []
            rows_2.append(self.as_nums(f.readline().strip()))
            rows_2.append(self.as_nums(f.readline().strip()))
            rows_2.append(self.as_nums(f.readline().strip()))
            rows_2.append(self.as_nums(f.readline().strip()))

            solve_line = self.solve(ans_1,rows_1,ans_2,rows_2)
            w.write("Case #%s: %s\n" % (i+1, solve_line))


if __name__ == '__main__':
    main  = MagicTrick()
    main.read_input()