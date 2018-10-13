import re

class run():
    def __init__(self, file):
        line = file.readline()
        [L, D, N] = [int(i) for i in line.split(" ")]
        self.words = []
        for word in range(D):
            self.words.append(file.readline()[:-1])


        self.output = ""
        for case in range(N):
            print case
            pattern = file.readline()
            comb = 0
            for word in self.words:
                if self.match(word, pattern):
                    comb += 1
                
            self.output += "Case #%d: %d\n" %(case+1, comb)

    def match(self, word, pattern):
        p = re.compile("\((?P<sequence>[a-z]+)\)|(?P<single>[a-z])")
        letters = p.findall(pattern)
        letters = ["".join(i) for i in letters]
        for letter in range(len(word)):
            if word[letter] not in letters[letter]:
                return False
        return True

    


file = open("A-small.in")
process = run(file)
file.close()
file = open("A-small.out", "w")
file.write(process.output)
file.close()
