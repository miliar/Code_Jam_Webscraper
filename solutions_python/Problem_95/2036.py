x,y,f = 'abcdefghijklmnopqrstuvwxyz ', 'yhesocvxduiglbkrztnwjpfmaq ', open('A-small-attempt0.in')
for case in range(int(f.readline().strip())):
    print('Case #%d:'%(case+1),end=' ')
    for letter in f.readline().strip():
        print(y[x.index(letter)],end='')
    print()