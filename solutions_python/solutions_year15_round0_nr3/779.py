from sys import stdin

index = {'i': 0, 'j': 1, 'k': 2}
transformations = [['','k','j'], ['k','','i'], ['j','i','']]
minuses = [[1,0,1], [1,1,0], [0,1,1]]

cases = int(stdin.readline())

for case in range(1, cases+1):
    l, x = map(lambda x: int(x), stdin.readline().rstrip('\n').split(' '))
    ijk = stdin.readline().rstrip('\n') * x
    match, neg = 0, 0

    while 1:
       if len(ijk) == 0: break

       if match == 0 and ijk[0] == 'i':
           match += 1
           ijk = ijk[1:]
       if match == 1 and ijk[0] == 'j':
           match += 1
           ijk = ijk[1:]
       if match == 2 and ijk[0] == 'k':
           match += 1
           ijk = ijk[1:]

       if len(ijk) <= 1:
           break

       a = index[ijk[0]]
       b = index[ijk[1]]

       ijk = transformations[a][b] + ijk[2:]
       neg += minuses[a][b]
       

    print "Case #{}: {}".format(case, 'YES' if match == 3 and len(ijk) == 0 and neg%2 == 0  else 'NO')
