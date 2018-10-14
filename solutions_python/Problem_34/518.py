class ProblemA:

    def Solve(self, file_in, file_out):
        self.__Read(file_in)
        for i_case, case in enumerate(self.cases):
            self.__SolveCase(i_case, case)
        self.__Write(file_out)
        
    def __Read(self, file_in):
        f = open(file_in, "r")
        line = self.__ReadLineAndWithoutBreaks(f)
        line_data = line.split(" ")
        self.length_of_words = int(line_data[0])
        self.number_of_words = int(line_data[1])
        self.number_of_cases = int(line_data[2])
        self.words = []
        for i_word in range(0, self.number_of_words):
            self.words.append(self.__ReadLineAndWithoutBreaks(f))
        self.cases = []
        self.matches_in_case = []
        for i_case in range(0, self.number_of_cases):
            self.cases.append(self.__ReadLineAndWithoutBreaks(f))
            self.matches_in_case.append(0)
        f.close()
        
    def __ReadLineAndWithoutBreaks(self, f):
        return f.readline().rstrip("\n\r")
        
    def __SolveCase(self, i_case, case):
        tokens = self.__CreateTokens(case)
        posible_words = []
        for word in self.words:
            posible_words.append(word)
        i_token = 0
        stop = False
        while i_token < self.length_of_words and not stop:
            token = tokens[i_token]
            token_posible_words = []
            for word in posible_words:
                i_char = 0
                chars_of_token = len(token)
                the_word_is_posible = False
                while i_char < chars_of_token and not the_word_is_posible:
                    c = token[i_char]
                    if word[i_token] == c:
                        token_posible_words.append(word)
                        the_word_is_posible = True
                    i_char+= 1
            posible_words = token_posible_words
            i_token+= 1
        self.matches_in_case[i_case] = len(posible_words)
        
    def __CreateTokens(self, pattern):
        tokens = []
        in_token = False
        for c in pattern:
            if c == "(":
                in_token = True
                token = ""
            elif c == ")":
                in_token = False
                tokens.append(token)
            else:
                if in_token:
                    token+= c
                else:
                    tokens.append(c)
        return tokens
        
    def __Write(self, file_out):
        f = open(file_out, "w")
        for i_case in range(0, self.number_of_cases):
            if(i_case > 0):
                f.write("\n")
            line = "Case #%i: %i" % ((i_case + 1),  self.matches_in_case[i_case])
            f.write(line)
            print line
        f.close()

problem_a = ProblemA()
#problem_a.Solve("A-example.in", "A-example.out")
#problem_a.Solve("A-small-attempt0.in", "A-small-attempt0.out")
problem_a.Solve("A-large.in", "A-large.out")
