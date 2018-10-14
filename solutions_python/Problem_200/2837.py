# cook your code here
# cook your dish here
t = int(raw_input().strip())

i = 1
while i<=t:
  string_number = raw_input().strip()
  n = int(string_number)
  number = [int(x) for x in string_number]
  l = len(number)

  j=0
  while l>1 and j<l-1:

    if number[j] > number[j+1]:

      flag = 0
      for k,val in enumerate(number):
        if val == number[j]:
          if flag == 0:
              number[k] = number[k]-1
              flag = 1
          else:
              number[k] = 9

        if k > j:
          number[k] = 9


    j = j+1

  final = ''
  for f in number:
      final = final+str(f)

  print("Case #{i}: {final}".format(i=i,final=int(final)))

  i = i+1
