def make_tidy(num):
    numl = [int(x) for x in str(num)]
    for i in range(len(numl)-1,0,-1):
        if numl[i] < numl[i-1]:
            numl[i:] = [9] * (len(numl) - i)
            numl[i-1] = numl[i-1] - 1
    return int("".join([str(x) for x in numl]))

num_tests = int(input())
for i in range(1, num_tests + 1):
  n = int(input())
  result = make_tidy(n)
  print("Case #{}: {}".format(i,result))
