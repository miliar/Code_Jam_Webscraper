class Case:

    def __init__(self, shy_level_max, num_shy_ppl_str):
        self.shy_level_max = shy_level_max

        self.num_shy_ppl_list = []
        for i in range(len(num_shy_ppl_str)):
            self.num_shy_ppl_list.append(int(num_shy_ppl_str[i]))


    def print_itself(self):
        print self.shy_level_max, self.num_shy_ppl_list


    def activate_itself(self):
        if self.shy_level_max == 0:
            return 0

        curr_num_ppl = 0
        need_num_ppl = 0
        for idx in range(len(self.num_shy_ppl_list)):
            curr_num_ppl += self.num_shy_ppl_list[idx]
            if curr_num_ppl < idx + 1:
                need_num_ppl += idx + 1 - curr_num_ppl
                curr_num_ppl += idx + 1 - curr_num_ppl
            print curr_num_ppl, need_num_ppl



            if curr_num_ppl >= self.shy_level_max:
                break

        return need_num_ppl


if __name__=="__main__":
    file_in = open("data/A-large.in", "rt")
    file_out = open("data/A-large.out", "wt")

    num_test_case = int(file_in.next())

    for i in range(num_test_case):
        tmp_list = file_in.next().strip().split()

        tmp_case = Case(int(tmp_list[0]), tmp_list[1])
        #tmp_case.print_itself()
        file_out.write("Case #" + str(i+1) + ": " + str(tmp_case.activate_itself()) + '\n')