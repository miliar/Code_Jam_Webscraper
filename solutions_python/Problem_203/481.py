num = int(input())  # read a line with a single integer


for i in range(1, num + 1):
  rows, cols = input().split() 
  row, col = int(rows), int(cols)
  l = []
  for x in range (row):
    l.append(list(str(input())))
  #print(l)
  def transform(l):
    outputlst = []
    for lst in l:
        currentchar = ''
        newlst = []
        count = 0
        for i in range(len(lst)):
            if i == 0:
                if lst[i] == '?':
                    currentchar = '?'
                    count += 1
                    #print ("we changed the count")
                   # print (count)
                else:
                    currentchar = lst[i]
                    newlst.append(currentchar)
            else:
                if lst[i] == '?':
                    if currentchar != '?':
                        newlst.extend((count+1) * [currentchar])
                        #print("Just added " + str(count))
                        count = 0
                    else:
                        count += 1
                else:
                    currentchar = lst[i]
                    #print("The count is " + str(count))
                    newlst.extend((count+1) * currentchar)
                    #print("we tripping here1")
                    count = 0
            #print(i)
            #print(newlst)
        if count == col:
          newlst.extend(count * '?')
        outputlst.append(newlst)
    return outputlst
  
  k = transform(l)
  newthing = list(map(list, zip(*k)))
  m = transform(newthing)
  finalthing = list(map(list, zip(*m)))
  output = list(map(lambda x : ''.join(x), finalthing))
  print("Case #{}:".format(i))
  for i in output:
    print (i)   
