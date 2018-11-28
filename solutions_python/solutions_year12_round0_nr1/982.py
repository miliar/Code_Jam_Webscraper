import sys

chars = {'\n': '\n', ' ': ' ', 'a': 'y', 'c': 'e', 'b': 'h', 'e': 'o', 'd': 's',
          'g': 'v', 'f': 'c', 'i': 'd', 'h': 'x', 'k': 'i', 'j': 'u', 'm': 'l', 
          'l': 'g', 'o': 'k', 'n': 'b', 'p': 'r', 's': 'n', 'r': 't', 'u': 'j', 
          't': 'w', 'w': 'f', 'v': 'p', 'y': 'a', 'x': 'm', 'z': 'q', 'q': 'z'}

def main():
    num_cases = int(sys.stdin.readline())
    
    for i in range(1, num_cases + 1):
        gglse = sys.stdin.readline()
        norml = [chars[c] for c in gglse]            
        print("Case #" + str(i) + ": " + ''.join(norml)).strip()

    
    
if __name__ == '__main__':
    main()
