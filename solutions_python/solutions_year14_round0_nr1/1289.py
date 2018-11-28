fout = open('MagicAns.txt', 'w')
fin = open('A-small-attempt0.in','r')
T = int(fin.readline())
for i in range(T):
    firstAns = int(fin.readline());
    rows1 = list( [map(int, fin.readline().split()) for j in range(4)]);    secondAns = int(fin.readline());
    rows2 = list( [map(int, fin.readline().split()) for j in range(4)]);
    n = 0;
    ans = '';
    for item in rows1[firstAns-1]:
        if item in rows2[secondAns-1]:
            n+= 1;
            ans = item;
    if n == 0:
        fout.write('Case #' + str(i + 1) + ': Volunteer cheated!\n');
    elif n == 1:
        fout.write('Case #' + str(i + 1) + ': ' + str(ans) + '\n');
    else:
        fout.write('Case #' + str(i + 1) + ': Bad magician!\n');


fin.close()
fout.close()
        
