#!/usr/bin/python
def main():
        regex = {
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
        ' ':' ',
        '\n':'',
        '':''
        }
        f=open('A-small-attempt2.in','r')
        #t = int(input(''))
        i=0
        for a in f:
                if i == 0:
                       i = i+1
                else:
                        tx = replace_all(a,regex)
                        print('Case #'+str(i)+': '+tx)
                        i = i+1   
	#for a in range(0,t):
	#	c=input('');
	#	tx = replace_all(c,regex);
	#	print('Case #',i,':',tx)
	#	i = i+1;

# define our method
def replace_all(text, dic):
        outstr=''
        i=0
        while(i<len(text)):
                outstr=outstr+dic[text[i]]
                i=i+1
        return outstr

if __name__ == '__main__':
    main()
