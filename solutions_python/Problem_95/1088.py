from string import ascii_lowercase

googlerese_map = ('y', 'h', 'e', 's', 'o', 'c', 'v', 'x', 'd', 'u', 'i', 'g', 'l',
                  'b', 'k', 'r', 'z', 't', 'n', 'w', 'j', 'p', 'f', 'm', 'a', 'q',)

def main():
    with open('input.txt', 'r') as input, open('output.txt', 'w') as output:
        T = input.readline()
        for i in range(1, int(T)+1):
            G = input.readline()
            output.write('Case #' + str(i) + ': ' + translate(G));

def translate(G):
    S = []
    G = list(G)
    for c in G:
        if c in ascii_lowercase:
            S.append(googlerese_map[ord(c) - ord('a')])
        else:
            S.append(c)
    return ''.join(S)

if __name__ == "__main__":
    main()
