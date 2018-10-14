vowels = ['a','e','i','o','u']
ntest = int(raw_input())
for itc in range(ntest):
  print 'Case #%d:' % (itc+1),
  name, n = raw_input().split()
  n = int(n)
  value = 0
  last = 0
  for index, i in enumerate(name):
      valid = 1
      if (index + n) > len(name):
          break
      if i in vowels :
          continue 
      for j in range(n-1):
          #print 'valid?:',name[index + j +1] 
          if name[index + j + 1] in vowels:
              valid = 0
              break
      if valid:
          if value == 0:
            value += (index + 1) * (len(name) - index - n +1)
          else:
            if (index - last) > 0:
                   value += (index - last + n -1) * (len(name) - index - n +1)
            #elif index <= last:
            else:
                   t = max(n- (last - index ) -1, 1)
                   value += t * (len(name) - index - n +1)
            #else :
            #       value += (len(name) - index - n +1)
          last = index + n -1;
      #print value,index,valid
  print value
