# author: Philip Ting
# Google Code Jam

def main():
    with open('A-small-attempt0.in', encoding='utf-8') as r:
        with open('output.txt', mode='w', encoding='utf-8') as w:
            
            T = int(r.readline()[:-1])

            for nth in range(T):
                line = r.readline()[:-1]
                english = translate(line)
                
                # output to file
                w.write('Case #' + str(nth+1) + ': ' + english + '\n')

def translate(line):
    g_dict = {
        'a':'y',
        'b':'h',
        'c':'e',
        'd':'s',
        'e':'o',
        'f':'c',
        'g':'v',
        'h':'x',
        'i':'d',
        'j':'u',
        'k':'i',
        'l':'g',
        'm':'l',
        'n':'b',
        'o':'k',
        'p':'r',
        'q':'z',
        'r':'t',
        's':'n',
        't':'w',
        'u':'j',
        'v':'p',
        'w':'f',
        'x':'m',
        'y':'a',
        'z':'q',
        ' ':' '
        }
    english = ""
    for i in line:
        english += g_dict[i]
        
    return english

if __name__ == "__main__":
    main()
