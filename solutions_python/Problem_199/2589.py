t = int(input())
for q in range(1, t + 1):
    st, leng = input().split(" ")
    leng = int(leng)
    st = list(st)
    if '-' not in st:
      print("Case #{}: {}".format(q, 0))
      continue
    flips = 0
    for i in range(len(st)-leng+1):
      if st[i] == '-':
          for j in range(leng):
              if st[i+j] == '-':
                  st[i+j] = '+'
              else:
                  st[i+j] = '-'
          flips += 1
    if '-' in st:
        print("Case #{}: {}".format(q, "IMPOSSIBLE"))
    else:
        print("Case #{}: {}".format(q, flips))
