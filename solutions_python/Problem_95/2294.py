
class Translator:

    def __init__(self):
        self.goog_to_eng= dict([('a', 'y') ,
                                ('c', 'e') ,
                                ('b', 'h') ,
                                ('e', 'o') ,
                                ('d', 's') ,
                                ('g', 'v') ,
                                ('f', 'c') ,
                                ('i', 'd') ,
                                ('h', 'x') ,
                                ('k', 'i') ,
                                ('j', 'u') ,
                                ('m', 'l') ,
                                ('l', 'g') ,
                                ('o', 'k') ,
                                ('n', 'b') ,
                                ('q', 'z') ,
                                ('p', 'r') ,
                                ('s', 'n') ,
                                ('r', 't') ,
                                ('u', 'j') ,
                                ('t', 'w') ,
                                ('w', 'f') ,
                                ('v', 'p') ,
                                ('y', 'a') ,
                                ('x', 'm') ,
                                ('z', 'q')])
        
    def googlerese_to_english(self,sentence):
        eng = "".join((self.goog_to_eng.get(letter,letter) for letter in sentence))
        return eng

def main():
    data = open("C:/Python27/q1.txt").readlines()
    num_tests = int(data[0])
    test_cases = data[1:1+num_tests]
    t = Translator()
    for i in range(num_tests):
        case = test_cases[i]
        print "Case #"+str(i+1)+":", t.googlerese_to_english(case.rstrip())

main()
        
