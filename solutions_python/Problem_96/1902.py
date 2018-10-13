 
def populateTriplets(normal_list, surprising_list):
  for i in xrange(31):
    val = i/3
    tempList = []
    if val*3 == i:
      tempList.append(val)
      tempList.append(val)
      tempList.append(val)
    elif val*3 + 1 == i:
      tempList.append(val)
      tempList.append(val)
      tempList.append(val+1)
    else:
      tempList.append(val)
      tempList.append(val+1)
      tempList.append(val+1)
    
    normal_list[i] = tempList
    
  for i in xrange(31):
    val = i/3
    tempList = []
    if val*3 == i and val > 0:
      tempList.append(val-1)
      tempList.append(val)
      tempList.append(val+1)
    elif val*3 + 1 == i and val > 0:
      tempList.append(val-1)
      tempList.append(val+1)
      tempList.append(val+1)
    elif val*3 + 2 == i:
      tempList.append(val)
      tempList.append(val)
      tempList.append(val+2)
    
    surprising_list[i] = tempList
    
    
  #print normal_list
  #print surprising_list
        
  return 1
    
def getSolution(N, input_list, S, p, normal_list, surprising_list):
  count  = 0
  tempS  = S 
  print "************************"
  #print input_list
  for i in xrange(N):
    if normal_list[input_list[i]][2] >= p:
      #print p, input_list[i], normal_list[input_list[i]][2]
      count += 1
    elif  len(surprising_list[input_list[i]]) > 0 and surprising_list[input_list[i]][2] >= p:
      if tempS > 0:
        count += 1
        tempS -= 1
  return count
 
  
def prepare_input(input_file):
    T = int(input_file.readline().replace('\n',''))
        
    output_file = file("B-large.out", "w")
    normal_list = {}
    surprising_list = {}
    populateTriplets(normal_list, surprising_list)    
    for test_case_counter in xrange(T):
        v1 = input_file.readline().replace('\n','').split(' ')
        
        input_list = []
        N = int(v1[0])
        S = int(v1[1])
        p = int(v1[2])
        for i in xrange(N):
          input_list.append(int(v1[3+i]))
        
        sol = getSolution(N, input_list, S, p, normal_list, surprising_list)
        #print N, S, p, sol
        #lowest count will be the number of switches in the server
        output_file.write("Case #"+str(test_case_counter+1)+": " + str(sol) + "\n")
        
        
    output_file.close()
    
if __name__ == "__main__":
    input_file = file("B-large.in")
    prepare_input(input_file)
