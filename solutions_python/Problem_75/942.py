def main():
  file = open('B-large.in', 'r')
  lines = file.readlines()
  file.close()
  
  num_cases = int(lines.pop(0))
  print "Cases: %d" % (num_cases)
  
  case=0                        
  out_file = open("output.txt","w+")
  for line in lines:
    line = line.replace('\n', '')
    tokens = line.split(' ')
    
    num_combines = int(tokens.pop(0))
    all_combinations = []
    for n in range(0, num_combines):
      all_combinations.append(tokens.pop(0))  
        
    num_opposed = int(tokens.pop(0))
    all_oppositions = []
    for n in range(0, num_opposed):
      all_oppositions.append(tokens.pop(0))
      
    tokens.pop(0) # We don't really need the length
    
    invokees = tokens.pop()
    
    elements = []
    for element in invokees:  
      if len(elements) == 0:
        elements.append(element)
        continue
                                                      
      # Find elements that this element opposes. (We could cache this)
      oppositions = []
      for opposition in all_oppositions:
        if element in opposition:
          oppositions.append(opposition.replace(element,"",1))      
                                   
      # Find elements that this element combines with and what they form (same about caching)
      combinations = {}
      for combination in all_combinations:
        if element in combination[:2]:
          combinations[combination[:2].replace(element,"",1)] = combination[-1]
          
      if elements[-1] in combinations.keys():
        elements[-1] = combinations[elements[-1]]
      else:
        cleared = False
        for opposition in oppositions:
          if opposition in elements:
            elements = []
            cleared = True
            break
        if not cleared:
          elements.append(element)
          
    case += 1
    output = "Case #%d: %s" % (case, str(list(elements)).replace("'","")) 
    print output
    out_file.write("%s\n" % (output))
    
  out_file.close()

if __name__=="__main__":
  main()