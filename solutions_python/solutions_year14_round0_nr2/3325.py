class CookieCutter():

    file_name = 'B-small-attempt0.in'
    output_name = 'output.txt'

    def as_nums(self, spaced_nums):
        """
        :type spaced_nums : str
        """
        nums = []
        for string_num in spaced_nums.split(' '):
            nums.append(float(string_num))
        return nums

    def solve(self, c, f, x):
        best = x/2
        new_try = best
        farms = 0
        while new_try <= best:
            best = new_try
            farms += 1
            total_time = 0
            for i in xrange(farms):
                time_for_farm = c/(2+i*f)
                total_time += time_for_farm
            new_try = x/(2+farms*f) + total_time
            print "%s %s" % (new_try, best)

        return "%.7f" % round(best, 7)





    def read_input(self):
        f = open(CookieCutter.file_name, 'r')
        w = open(CookieCutter.output_name, 'w')
        line = f.readline()
        cases = int(line.strip())
        print "there are %s cases" % cases
        for i in xrange(cases):
            values = self.as_nums(f.readline().strip())

            solve_line = self.solve(*values)
            w.write("Case #%s: %s\n" % (i+1, solve_line))


if __name__ == '__main__':
    main  = CookieCutter()
    main.read_input()