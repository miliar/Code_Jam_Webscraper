#Tongues.py
#Justin Roberts (tangofox10@gmail.com
#Code Jam Qualification Round
#Problem: Speaking in Tongues
#Written in Python

#Also written in my sleep, yo.
#Srsli...
#Step 1: Write dictionary.
#Step 2: ....
#Step 3: Profit.
#I guess I ought to start writing the program instead of cutesy comments.

fin = open('A-small-attempt0.in', 'r')
fout = open('TonguesOut.txt', 'w')
#I don't want to copy/paste or redirect.

T = int(fin.readline())
#My cat is scratching to be let out. Bitch, it's 10 PM. You're staying in.
#Oh, right. T test cases. Yep.

Googlerese_to_English_dict = {
    'a':'y','b':'h',
    'c':'e','d':'s',
    'e':'o','f':'c',
    'g':'v','h':'x',
    'i':'d','j':'u',
    'k':'i','l':'g',
    'm':'l','n':'b',
    'o':'k','p':'r',
    'q':'z','r':'t',
    's':'n','t':'w',
    'u':'j','v':'p',
    'w':'f','x':'m',
    'y':'a','z':'q',
    ' ':' '
    }
#Man, that was a long freaking list!
#Screw your 26!... 26 is a big enough number to make me cry.
#I probably should have written a program to type that all out for me.

#Funfact: If I were just a little less tired (done a bit of traveling lately)
#and a little more motivated (I doubt anyone will ever read this),
#I'd write this stupid thing in Brainf**k.
#I'm all about those >s, .s and [s.
#I wonder how big it would have to be. Probably a like 10 kB, right?
for case in range(1,T+1):
    Googlerese_string = fin.readline().strip()
    #raw_input()? Is that how babies are made?
    #Wait... I'm using my own input stream. Dammit.
    #Oh well, the joke stays, even if the code goes.

    English_string = ''
    for char in Googlerese_string:
        English_string += Googlerese_to_English_dict[char]
    fout.write('Case #' + str(case) + ': ' + English_string + '\n')
    print('Case #%d: %s'%(case,English_string)) #testing schtuff... too lazy to
                                                #remove

#a>y, b>h>x>m>l>g>v>p>r>t>w>f>c>e>o>k>i>d>s>n, j>u, q>z
#So if we applied the Googlerese-English decrypter recursively,
#it would take 20 iterations to arrive back at Googlerese.
#I was expecting more cycles, to be honest.

#Ok, time to test this bad boy.
#I'm going to feel dumb if I screwed something up.

#Alright, so I changed a couple things around.
#It was mostly just a non-Pythonic thing (stupid C++ making me silly).

#Ok, my stdout is working fine, but my custom output thing isn't printing.
#It's just making a blank document.

#Oh, I ran it outside my IDE, and it worked. Weird.
#I can live with that.

#Small (only!) case, here I come!