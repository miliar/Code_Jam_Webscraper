s = " ejpmysljylckdkxveddknmcrejsicpdrysirbcpcypcrtcsradkhwyfrepkymveddknkmkrkcddekrkdeoyakwaejtysrreujdrlkgcjvqz";
n = " ourlanguageisimpossibletounderstandtherearetwentysixfactorialpossibilitiessoitisokayifyouwanttojustgiveupzq";
d = dict()
f = open('output', 'w')
for i in range(len(n)):
      d[s[i]] = n[i]
a = open('input').read().split('\n')[:-1]
for i in range(1, int(a[0]) + 1):
      print('Case #' + str(i) +  ': ', end = '', file = f)
      for j in range(len(a[i])):
            print(d[a[i][j]], sep = '', end = '', file = f)
      print(' ', file = f)
