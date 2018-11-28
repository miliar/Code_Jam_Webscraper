class ProblemC:

    def Solve(self, file_in, file_out):
        self.text = "welcome to code jam"
        self.h = len(self.text)
        self.__Read(file_in)
        for i_case, case_text in enumerate(self.cases):
            self.__SolveCase(i_case, case_text)
        self.__Write(file_out)
        
    def __Read(self, file_in):
        f = open(file_in, "r")
        self.number_of_cases = int(self.__ReadLineAndWithoutBreaks(f))
        self.cases = []
        self.subsequences = []
        for i_case in range(0, self.number_of_cases):
            self.subsequences.append(0)
            self.cases.append(self.__ReadLineAndWithoutBreaks(f))
        f.close()
        
    def __ReadLineAndWithoutBreaks(self, f):
        return f.readline().rstrip("\n\r")
        
    def __SolveCase(self, i_case, case_text):
        cs_is = []
        for c1 in self.text:
            c_is = []
            for i_c2, c2 in enumerate(case_text):
                if c2 == c1:
                    c_is.append(i_c2)
            if len(c_is) == 0:
                return
            else:
                cs_is.append(c_is)
        for i_c2 in cs_is[0]:
            self.__DFS(i_case, cs_is, 0, i_c2)
        
    def __DFS(self, i_case, cs_is, i_c1, i_c2):
        if i_c1 == self.h - 1:
            self.subsequences[i_case]+= 1
        else:
            next_c_is = cs_is[i_c1 + 1]
            for i_next_c in next_c_is:
                if i_next_c > i_c2:
                    self.__DFS(i_case, cs_is, i_c1 + 1, i_next_c)
        
    def __Write(self, file_out):
        f = open(file_out, "w")
        for i_case in range(0, self.number_of_cases):
            if(i_case > 0):
                f.write("\n")
            line = "Case #%i: %04i" % (i_case + 1, self.subsequences[i_case] % 10000)
            f.write(line)
            print line
        f.close()

problem_c = ProblemC()
#problem_c.Solve("C-example.in", "C-example.out")
problem_c.Solve("C-small-attempt0.in", "C-small-attempt0.out")
#problem_c.Solve("C-large.in", "C-large.out")
