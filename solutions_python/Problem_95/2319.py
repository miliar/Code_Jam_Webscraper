import sys

def main():
    in_file = open(sys.argv[1],'r')
    in_file_list = in_file.readlines();
    in_file_list = in_file_list[1:len(in_file_list)]
    out_file = open('out','w')
    counter = 1

    mappings = {'y':'a', 'n':'b', 'f':'c', 'i':'d', 'c':'e', 'w':'f', 'l':'g', 'b':'h', 'k':'i', 'u':'j', 'o':'k', 'm':'l', 'x':'m', 's':'n', 'e':'o', 'v':'p', 'z':'q', 'p':'r', 'd':'s', 'r':'t', 'j':'u', 'g':'v', 't':'w', 'h':'x', 'a':'y', 'q':'z'}

    for ciphertext in in_file_list:
        plaintext=''
        for i in range(0,len(ciphertext)):
            if(ciphertext[i] == ' '):
                plaintext += ' '
            elif (ciphertext[i] == '\n'):
                continue
            else:
                plaintext += mappings[ciphertext[i]]
	out_file.write('Case'+' '+'#'+str(counter)+': '+plaintext+'\n')
	counter+=1
    in_file.close()
    out_file.close()

if __name__ == "__main__":
    main()

        
