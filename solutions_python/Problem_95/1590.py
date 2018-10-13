def change(S):
    R='';
    for L in S:
        if L=='a':
            R=R+'y'
        elif L=='b':
            R=R+'h'
        elif L=='c':
            R=R+'e'
        elif L=='d':
            R=R+'s'
        elif L=='e':
            R=R+'o'
        elif L=='f':
            R=R+'c'
        elif L=='g':
            R=R+'v'
        elif L=='h':
            R=R+'x'
        elif L=='i':
            R=R+'d'
        elif L=='j':
            R=R+'u'
        elif L=='k':
            R=R+'i'
        elif L=='l':
            R=R+'g'
        elif L=='m':
            R=R+'l'
        elif L=='n':
            R=R+'b'
        elif L=='o':
            R=R+'k'
        elif L=='p':
            R=R+'r'
        elif L=='q':
            R=R+'z'
        elif L=='r':
            R=R+'t'
        elif L=='s':
            R=R+'n'
        elif L=='t':
            R=R+'w'
        elif L=='u':
            R=R+'j'
        elif L=='v':
            R=R+'p'
        elif L=='w':
            R=R+'f'
        elif L=='x':
            R=R+'m'
        elif L=='y':
            R=R+'a'
        elif L=='z':
            R=R+'q'
        elif L==' ':
            R=R+' '
    return R

input = open('A-small-attempt3.in', 'r');
output = open('A-small.attempt3.out', 'w');

n=int(input.readline());

for x in range(1,n+1):
    output.write("Case #" + str(x) + ": " + change(input.readline()) + "\n");

input.close();
output.close();
