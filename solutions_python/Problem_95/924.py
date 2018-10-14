#! /usr/bin/env python3 -O

##########
## Adam Sorkin
## google codejam qual A
## 13 Apr 2012
##########


def main():
    "Translation"

    T = int(input()) # number of test cases
    for i in range(1, T+1):
        gibberish = input()
        translation = foo(gibberish)
        print("Case #{0}: {1}".format(i, translation) )
    return

alphabet = { 'a':'y' , 'b': 'h' , 'c':'e', 'd':'s', 'e':'o', 'f':'c', 'g':'v', 'h':'x', 'i':'d', 'j':'u', 'k':'i', 'l':'g', 'm':'l', 'n':'b', 'o':'k', 'p':'r', 'q':'z', 'r':'t', 's':'n', 't':'w', 'u':'j', 'v':'p', 'w':'f', 'x':'m', 'y':'a', 'z':'q', ' ':' ' }

def foo(goobly_gook):
    decoded = ''
    for j in range(len(goobly_gook)):
        decoded += alphabet[goobly_gook[j] ]
    return decoded


if __name__ == "__main__":
    main()


