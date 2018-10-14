import sys

mapping = {' ': ' ', 'y': 'a', 'c': 'e', 'b': 'h', 'e': 'o', 'd': 's', 'g': 
'v', 'f': 'c', 'i': 'd', 'h': 'x', 'k': 'i', 'j': 'u', 'm': 'l', 'l': 'g', 
'o': 'k', 'n': 'b', 'p': 'r', 's': 'n', 'r': 't', 'u': 'j', 't': 'w', 'w': 
'f', 'v': 'p', 'y': 'a', 'x': 'm', 'q': 'z', 'a': 'y', 'z': 'q'}
           
def main():
    lines = open(sys.argv[1]).readlines()[1:]
    for i,line in enumerate(lines):
        print "Case #%d: %s" % (i + 1, ''.join(map(lambda x: mapping[x] if x in mapping else '#', line[:-1])))
    
if __name__ == "__main__":
    main()
    #lines = open(sys.argv[1]).readlines()[1:]
    #for i,line in enumerate(lines):
        #print "Case #%d: %s" % (i, ''.join(map(lambda x: mapping[x] if x in mapping else '#', line)))
