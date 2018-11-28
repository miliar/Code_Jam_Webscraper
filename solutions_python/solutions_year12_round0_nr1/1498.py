import sys

def main(argv):    
    mapping = {'A': 'Y', 'C': 'E', 'B': 'H', 'E': 'O', 'D': 'S', 'G': 'V', 'F': 'C', 'I': 'D', 'H': 'X', 'K': 'I', 'J': 'U', 'M': 'L', 'L': 'G', 'O': 'K', 'N': 'B', 'Q': 'Z', 'P': 'R', 'S': 'N', 'R': 'T', 'U': 'J', 'T': 'W', 'W': 'F', 'V': 'P', 'Y': 'A', 'X': 'M', 'Z': 'Q', 'a': 'y', 'c': 'e', 'b': 'h', 'e': 'o', 'd': 's', 'g': 'v', 'f': 'c', 'i': 'd', 'h': 'x', 'k': 'i', 'j': 'u', 'm': 'l', 'l': 'g', 'o': 'k', 'n': 'b', 'q': 'z', 'p': 'r', 's': 'n', 'r': 't', 'u': 'j', 't': 'w', 'w': 'f', 'v': 'p', 'y': 'a', 'x': 'm', 'z': 'q'}

    f = open('/home/saba/Documents/codejam/in.txt', 'r')
    f.readline() #dont want number
    fo = open('/home/saba/Documents/codejam/out.txt', 'w')
    num = 1
    for line in f:
        fo.write("Case #%d: " % num)
        for c in line:
            if mapping.has_key(c):
                fo.write(mapping[c])
            else:
                fo.write(c)
        num += 1       
    f.close()
    fo.close()
                
             

if __name__ == "__main__":
    main(sys.argv[1:])
