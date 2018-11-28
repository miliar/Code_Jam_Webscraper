import sys

T = int(raw_input())

for case in range(T):
   res = 0
   A = 0
   B = 0
   checked = [11, 22, 33, 44, 55, 66, 77, 88, 99, 
              111, 222, 333, 444, 555, 666, 777, 888, 999,
              1111, 2222, 3333, 4444, 5555, 6666, 7777, 8888, 9999]
   line = raw_input()
   tokens = line.split();
   A = int(tokens.pop(0))
   B = int(tokens.pop(0))

   for i in range(A, B+1):
      if i not in checked:
         checked.append(i)
         numstring = str(i)
         length = len(numstring)
         doublestring = numstring + numstring

         for c in range(1, length):
            if doublestring[c] != '0':
               num = int(doublestring[c: c+length])
               if (num not in checked) and (A <= num) and (num <= B):
                  res+=1

   print ("Case #%d: %d") %(case+1, res)

