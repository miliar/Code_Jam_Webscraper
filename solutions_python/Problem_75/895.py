from copy import copy

class TestCase():
    def __init__(self, case_id, combineable_elements = {}, conflicting_elements = {}, invoke_sequence = ""):
       self.case_id = case_id
       self.combineable_elements = copy(combineable_elements)
       self.conflicting_elements = copy(conflicting_elements)
       
       self.invoke_sequence = copy(invoke_sequence)
       
    def from_line(self, line):
        line = line.split(" ")
        
        c = int(line[0])
        
        line_i = 1
        
        # Combineable elements
        for i in range(c):
        
            elements = line[line_i+i]

            if not elements[0] in self.combineable_elements:
               self.combineable_elements[elements[0]] = {}
            if not elements[1] in self.combineable_elements:
               self.combineable_elements[elements[1]] = {}
          
            self.combineable_elements[elements[0]][elements[1]] = elements[2]
            self.combineable_elements[elements[1]][elements[0]] = elements[2]
       
        
        
        # Conflicting elements
        line_i += c
        d = int(line[line_i])        
        line_i += 1
        
        for i in range(d):
            elements = line[line_i+i]

            if not elements[0] in self.conflicting_elements:
              self.conflicting_elements[elements[0]] = []              
            if not elements[1] in self.conflicting_elements:
              self.conflicting_elements[elements[1]] = []
              
            self.conflicting_elements[elements[0]].append(elements[1])
            self.conflicting_elements[elements[1]].append(elements[0])
        
        line_i += d
        n = int(line_i)
        line_i += 1
        
        self.invoke_sequence = line[line_i]
    
    def combine(self, element1, element2):
        if element1 in self.combineable_elements and element2 in self.combineable_elements[element1]:
            return self.combineable_elements[element1][element2]
        else:
            return None
    
    def get_conflicting(self, element1):
       if element1 in self.conflicting_elements:
            return  self.conflicting_elements[element1]
       else:
            return []
            
    def __repr__(self):
        return 'TestCase(%s, combineable_elements = %s, conflicting_elements = %s, invoke_sequence = %s)' \
                 % ( 
                   repr(self.case_id), 
                   repr(self.combineable_elements), 
                   repr(self.conflicting_elements), 
                   repr(self.invoke_sequence)
                   )
                
    def __str__(self):
        return 'Case #%s: ' % self.case_id
         

# Solver:

      
      
def solve(test_case):

    element_list       = []
    elements_in_list   = {}
    
    for element in test_case.invoke_sequence:
       if element_list:
           combined_element = test_case.combine(element, element_list[-1])
           if combined_element:
              last_element = element_list.pop()
              elements_in_list[last_element] -= 1
              
              element_list.append(combined_element)
       
              if not combined_element in elements_in_list:
                  elements_in_list[combined_element] = 1
              else:
                  elements_in_list[combined_element] += 1
                  
           else: # Cannot combine, possible conflict
                conflicting_elements = test_case.get_conflicting(element)

                have_conflict = False
                for conflicting_element in conflicting_elements:
                  if conflicting_element in elements_in_list and elements_in_list[conflicting_element] > 0:
                      # Clear everything
                      element_list = []
                      elements_in_list = {}
                      have_conflict = True                     
                      break
                      
                if not have_conflict:
                
                    element_list.append(element)

                    if not element in elements_in_list:
                        elements_in_list[element] = 1
                    else:
                        elements_in_list[element] += 1
  
          
       else:
           element_list.append(element)
           
           if not element in elements_in_list:
              elements_in_list[element] = 1
           else:
              elements_in_list[element] += 1
     
    return element_list
    
                  
# Main:

test_cases = int(raw_input())

for i in range(test_cases):
    line = raw_input()
    case = TestCase(i+1)
    case.from_line(line)
    answer = solve(case)
    print '%s[%s]' % (case, ', '.join(answer))

