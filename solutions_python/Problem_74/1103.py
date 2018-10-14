class Solve:
    def __init__(self, name_file):
        print "Name: ", name_file
        self.arch = file(name_file, "r")
        self.N = int( self.arch.readline())
        print self.N
        self.lines = self.arch.readlines()
        self.arch.close()
    def invertLine(self, line):
        line2 = line[0:len(line)-1]
        words = line2.split(" ")
        words.reverse()
        new_line = ""
        for i in range(len(words)-1):
            new_line = new_line + words[i] + " "
        new_line = new_line + words[len(words)-1]
        return new_line
    def invertLines(self):
        output_str = ""
        for i in range(self.N):
            case_number = i + 1
            line = self.invertLine(self.lines[i])
            output_str = output_str + "Case #" + str(case_number) + ": "
            output_str = output_str + line + "\n"
        return output_str

    def writeOutput(self, file_name):
        out_file = file(file_name, "w")
        out_file.write(self.invertLines())
        out_file.close()
    
