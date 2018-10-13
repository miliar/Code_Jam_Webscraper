cache = {}
def count_instances(string, corpus):
    if cache.get((corpus, string), None) != None:
        return cache[(corpus, string)]
    elif len(string) == 0:
        return 1
    else:
        num = 0
        head = string[0]
        for i,char in enumerate(corpus[::-1]):
            if char == head:
                num += count_instances(string[1:], corpus[-1 - i:])
        cache[(corpus, string)] = num
        return num

def main():
    infile = open('C-large.in')
    outfile = open('C-large.out', 'w')
    num_cases = int(infile.readline().rstrip())
    for i in xrange(num_cases):
        case = infile.readline().rstrip()
        num_instances = count_instances('welcome to code jam', case)
        output = 'Case #%d: %04d\n'%(i+1, num_instances % 10000)
        print output,
        outfile.write(output)
    outfile.close()
               
if __name__ == '__main__':
    main()
