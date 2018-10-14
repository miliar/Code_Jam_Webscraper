# First problem code jam

class question1:
    word_list = []
    test_list = []
    test_list_parsed = []
    L, D, N = 0, 0, 0
    def parse_input(self):

        f = open('A-large.in','r')

        lines = f.readlines()

        input_var = lines[0].split()

        self.L = int(input_var[0])
        self.D = int(input_var[1])
        self.N = int(input_var[2])
        
        for i in range(1, self.D+1):

            self.word_list.append(lines[i].strip())

        for i in range(self.D+1, self.D+self.N+1):

            self.test_list.append(lines[i].strip())

        # Resolve the regex strings into components

        for string in self.test_list:

            # Append an empty list to test_list_parsed
            buf_list = []
            i=0
            while(i < len(string)):
                if string[i] == '(':
                    i=i+1
                    buf=''
                    while(string[i] != ')'):
                        buf+=string[i]
                        i=i+1
                    buf_list.append(buf)
                    i=i+1
                else:
                    buf_list.append(string[i])
                    i=i+1
            self.test_list_parsed.append(buf_list)
                    
    
        f.close()

    def main_algo(self):
        case = 1
        # take each word in word list
        for regex in self.test_list_parsed:
            count = 0
            for word in self.word_list:
                # Take each character of word
                buf_count = 0
                for i in range(len(word)):
                    if word[i] in regex[i]:
                        buf_count = buf_count + 1
                if buf_count == len(word):
                    count = count + 1
            print "Case #"+str(case)+": "+str(count)
            case = case + 1
                    
                    

        

q1 = question1()
q1.parse_input()
q1.main_algo()

    
