t = int(input())

i = 1
while i<=t:
  n_str = input()
  n = int(n_str)
  n_list = [int(x) for x in n_str]
  l = len(n_list)

  j=0
  while l>1 and j<l-1:

    if n_list[j] > n_list[j+1]:

      check = 0
      for k,val in enumerate(n_list):
        if val == n_list[j]:
          if check == 0:
              n_list[k] = n_list[k]-1
              check = 1
          else:
              n_list[k] = 9

        if k > j:
          n_list[k] = 9


    j = j+1

  result = int(''.join([str(x) for x in n_list]))

  print("Case #{}: {}".format(i,result))

  i = i+1
