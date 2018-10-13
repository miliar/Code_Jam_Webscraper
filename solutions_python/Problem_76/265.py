from operator import xor

def cjwrap(answerer, input_filename):
    fin = file(input_filename, 'r')
    fout = file('output.txt', 'w')
    inputs = int(fin.readline())
    for i in xrange(inputs):
        output = answerer(fin)
        fout.write("Case #%s: %s\n" % (i+1, output))
    fout.close()

def answer(f):
    f.readline()
    candies = f.readline().split(" ")
    candies = [int(x) for x in candies]
    return cheat(candies)
    
def cheat(candies):
    if reduce(xor, candies) == 0:
        return sum(candies) - min(candies)
    else:
        return "NO"
    
cjwrap(answer, 'candies_sample.in')