class IO (object):
    def __init__ (self, mode='test'):
        self.mode = mode
        if self.mode != 'debug':
            self.f_out = open ('output.txt', 'w')
            f_in = open ('input.txt', 'r')
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
            
    

def parse (sl):
    smax, tmp = sl.split (' ', 1)

    buckets = [int (a) for a in tmp]
    return int (smax), buckets

def solve (sl):
    smax, buckets = parse (sl)

    num_standing = buckets [0]
    friends_needed = 0

    for a in range (1, smax + 1):
        if num_standing < a:
            friends_needed += a - num_standing
            num_standing = a

        try:
            num_standing += buckets [a]
        except KeyError:
            num_standing += 0
            
    return friends_needed


def output (text):
    f.write (text + '\n')
    print text


io = IO ()

for a in range (int (io.cin ())):
    
    answer = solve (io.cin ())
    io.cout ('Case #' + str (a + 1) + ': ' + str (answer))

io.done ()
print 'done'
