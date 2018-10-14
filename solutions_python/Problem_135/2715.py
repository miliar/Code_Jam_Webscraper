import sys
def resolve(exo1, exo2):
    result = []
    for i in range(4):
        tmp = exo1[i]
        for y in range(4):
            if exo2[y] == tmp : result.append(tmp)
    if len(result) == 1:
        return result[0]
    elif len(result) > 1:
        return 'Bad magician!'
    return 'Volunteer cheated!'



samples = int(sys.stdin.readline().rstrip())
for i in range(samples):

      exo1 = []
      lineN1 = sys.stdin.readline().rstrip();
      exo1.append(sys.stdin.readline().rstrip())
      exo1.append(sys.stdin.readline().rstrip())
      exo1.append(sys.stdin.readline().rstrip())
      exo1.append(sys.stdin.readline().rstrip())

      exo2 = []
      lineN2 = sys.stdin.readline().rstrip();
      exo2.append(sys.stdin.readline().rstrip())
      exo2.append(sys.stdin.readline().rstrip())
      exo2.append(sys.stdin.readline().rstrip())
      exo2.append(sys.stdin.readline().rstrip())

      #print exo1[int(lineN1)-1]
      #print exo2[int(lineN2)-1]
      print 'Case #' + str(i+1) + ': ' + resolve(exo1[int(lineN1)-1].split(' '), exo2[int(lineN2)-1].split(' '))
