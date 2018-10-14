class IO (object):
    def __init__ (self, in_file, out_file, mode='!debug'):
        self.mode = mode
        if self.mode != 'debug':
            self.f_out = open (out_file, 'w')
            f_in = open (in_file, 'r')
            self.lines = [line.strip () for line in f_in.readlines ()]
            f_in.close ()
            self.line_id = -1

            
    def cin (self):
        if self.mode == 'debug':
            return raw_input ()
        else:
            self.line_id += 1
            return self.lines [self.line_id]

    def cout (self, text):
        if self.mode == 'debug':
            print text
        else:
            print text # sanity check
            self.f_out.write (text + '\n')

    def done (self):
        self.f_out.close ()
            
    
class QuestionBase (object):
    def __init__ (self, mode='!debug', in_file='input.txt', out_file='output.txt'):
        self.io = IO (in_file, out_file, mode)
        self.run ()

    def run (self):
        for a in range (int (self.io.cin ())):
            answer = self.solve ()
            self.io.cout ('Case #' + str (a + 1) + ': ' + str (answer))
        self.io.done ()
        print 'done'

    def solve (self, text):
        return 'NAN'


class Dijkstra (QuestionBase):
    def __init__ (self, *args, **kwargs):
        self.lookup = {
            '1': {'1':'1', 'i':'i', 'j':'j', 'k':'k'},
            'i': {'1':'i', 'i':'-1', 'j':'k', 'k':'-j'},
            'j': {'1':'j', 'i':'-k', 'j':'-1', 'k':'i'},
            'k': {'1':'k', 'i':'j', 'j':'-i', 'k':'-1'},
        }
        self.c = 0 
        super (Dijkstra, self).__init__ (*args, **kwargs)
        
          
    def solve (self):
        L, X = self.io.cin ().split (' ')
        self.text = self.io.cin ()
        self.text *= int (X)

        self.back_lookup = ['1']
        reduced = '1'
        for a in range (len (self.text) - 1, -1, -1):
            reduced = self.mul (self.text [a], reduced)
            self.back_lookup += [reduced]

        if self.solveI (self.text):
            return 'YES'
        else:
            return 'NO'


    def solveI (self, text):
        value = '1'
        index = 0
        target = 'i'
        while (True):
            try:
                value = self.mul (value, text [index])
            except IndexError:
                return False
            
            if value == target:
                if self.solveJ (text [index+1:]):
                    return True

            index += 1

    def solveJ (self, text):
        value = '1'
        index = 0
        target = 'j'
        while (True):
            try:
                value = self.mul (value, text [index])
            except IndexError:
                return False
            
            if value == target:
                if self.solveK (text [index+1:]):
                    return True

            index += 1
            

    def solveK (self, text):
        return self.back_lookup [len (text)] == 'k'

        

    def mul (self, a, b):
        sign = 1
        if a [0] == '-':
            sign *= -1
        if b [0] == '-':
            sign *= -1
        result = ('-' if sign < 0 else '') + self.lookup [a [-1]] [b [-1]]
        if result [0] == '-' and result [1] == '-':
            result = result [2:]
        return result
            



Dijkstra (in_file='C-small-attempt2.in')
#Dijkstra ()
