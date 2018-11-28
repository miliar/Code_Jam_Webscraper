class GameInstance:
    def __init__(self, init_str):
        self.strs = init_str
        self.total_action = 0
        self.tab_strs = []
        self.tabularize()

    def tabularize(self):
        #set_trace()
        N = len(self.strs)
        for i in range(0, N):
            self.tab_strs.append([[self.strs[i][0],1]])
            for j in range(1, len(self.strs[i])):
                if self.tab_strs[i][-1][0] == self.strs[i][j]:
                    self.tab_strs[i][-1][1] +=1
                else:
                    self.tab_strs[i].append([self.strs[i][j],1])

    def del_rep(self, si):
        clean_ptr = 0
        clean_str = self.strs[si][0]
        #set_trace()
        del_start = False
        for i in xrange(1, len(self.strs[si])):
            if clean_str[-1] == self.strs[si][i]:
                #i+= 1
                if not del_start:
                    self.total_action += 1
                    del_start = True
            else:
                del_start = False
                clean_str += self.strs[si][i]
                #i += 1

        return clean_str

    def solve(self):
        #the point is that as long as there is no repetition we can't do anything.
        #if there is a character in one of the string that is not in the other one
        #then we are done impossible.
        #also the order of repetition doesn't matter
        #so we move the pointer for all of them if we can repair we repair if not game
        #over
        N = len(self.strs)
        ref_len = len(self.tab_strs[0])
        # mod_str = self.del_rep(0)
        # poss = True
        # for i in range(1,N):
        #     if (mod_str != self.del_rep(i)):
        #         return "Fegla Won"
        for i in range(1,N):
            if ref_len  != len(self.tab_strs[i]):
                return "Fegla Won"

            for j in range(0, ref_len):
                if (self.tab_strs[0][j][0] != self.tab_strs[i][j][0]):
                    return "Fegla Won"

        #set_trace()
        # all_mins = [self.tab_strs[0][i][1] for i in range(0, ref_len)]
        # for i in range(1, N):
        #     for j in range(0, ref_len):
        #         if all_mins[j] > self.tab_strs[i][j][1]:
        #             all_mins[j] = self.tab_strs[i][j][1]


        for j in range(0, ref_len):
            sum_cl = 0
            for i in range(0, N):
                sum_cl += self.tab_strs[i][j][1]

            average = float(sum_cl)/float(N)

            av = [0,0]
            no_action = [0,0]
            av[0] = int(average)
            av[1] = int(average)+1

            for side in range(0,2):
                for i in range(0, N):
                    no_action[side] += abs(av[side] - self.tab_strs[i][j][1])

            if no_action[0] <  no_action[1]:
                self.total_action += no_action[0]
            else:
                self.total_action += no_action[1]

        return str(self.total_action)

N = input()
for i in range(1,N+1):
    T = input()
    cur_case = []
    from pdb import set_trace
    for j in range(0,T):
        cur_case.append(raw_input())
    #set_trace()
    cur_game = GameInstance(cur_case)
    print "Case #%i: %s"%(i,cur_game.solve())
