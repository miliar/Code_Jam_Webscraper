'''
Created on Apr 13, 2012

@author: rob
'''

key = {' ': ' ', '\n':'', 'a': 'y', 'c': 'e', 'b': 'h', 'e': 'o', 'd': 's', 'g': 'v', 'f': 'c', 'i': 'd', 'h': 'x', 'k': 'i', 'j': 'u', 'm': 'l', 'l': 'g', 'o': 'k', 'n': 'b', 'q': 'z', 'p': 'r', 's': 'n', 'r': 't', 'u': 'j', 't': 'w', 'w': 'f', 'v': 'p', 'y': 'a', 'x': 'm', 'z': 'q'}

def main():
    fileInput = open('/Users/rob/Downloads/A-small-attempt0.in', 'r')
    N = int(fileInput.readline())
    
    for caseNum in range(1, N+1):
        g = fileInput.readline()
        print('Case #' + str(caseNum) + ': ' + "".join([''+key[s] for s in g]))
        
if __name__ == '__main__':
    main()