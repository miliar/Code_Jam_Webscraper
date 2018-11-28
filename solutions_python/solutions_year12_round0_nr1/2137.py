import sys


convertor = {' ': ' ', 'a': 'y', 'c': 'e', 'b': 'h', 'e': 'o', 'd': 's', 'g': 'v', 'f': 'c', 'i': 'd', 'h': 'x', 'k': 'i', 'j': 'u', 'm': 'l', 'l': 'g', 'o': 'k', 'n': 'b', 'p': 'r', 's': 'n', 'r': 't', 'u': 'j', 't': 'w', 'w': 'f', 'v': 'p', 'y': 'a', 'x': 'm', 'z': 'q', 'q': 'z'}

def foo():
    line = sys.stdin.readline()
    output = ''
    for i in range(len(line) - 1):
        output += convertor[line[i]]
    return output

def main():
    n = int(sys.stdin.readline())
    for i in range(n):
        print "Case #%s: %s" % (i+1, foo())

if __name__ == '__main__':
    main()