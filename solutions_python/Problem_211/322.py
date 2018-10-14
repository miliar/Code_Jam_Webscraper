#!/usr/bin/python

def find_deficits(list, avg):
  num_items = len(list)
  total_deficits = 0.000000
  for i in range(0, num_items):
    if list[i] < avg:
      total_deficits += avg - list[i]

  return total_deficits

def find_avg(list, last_item, extras):
  total = 0.000000
  for i in range(0, last_item):
    total += list[i]
  avg = (total + extras)/last_item
  #print "avg="+str(avg)
  return avg

#def allocate_units(probs, units, final_avg):
##  total_num = len(probs)
#  remaining_units = units
#  for i in range(0, total_num):
#    if units[i] > final_avg:
#      break
#    elif i < (total_num - 1):
#      next_item = probs[i]
#      if remaining_units >= next_item - probs[i]:
#        probs[i] = next_item
#        remaining_units -= next_item -

def allocate_units(probs, units, target_avg):
  rem_units = units
  for i in range(0, len(probs)):
    if probs[i] < target_avg:
      if rem_units == 0:
        return probs
      elif rem_units >= (target_avg-probs[i]):
        probs[i] = target_avg
        rem_units -= target_avg - probs[i]
      else:
        probs[i] += rem_units
        return probs
    else:
      break
  return probs

def find_allocated_avg(probs, units, avg, num_items):
  final_item = num_items
  for i in range(0, num_items):
    if probs[i] > avg:
      final_item = i
  new_avg = find_avg(probs, final_item, units)
  if new_avg == avg:
    return avg
  else:
    renewed_avg = find_allocated_avg(probs, units, new_avg, final_item)
  #if new_avg == renewed_avg:
    return renewed_avg
  #else:
#    find_allocated_avg(probs, units, new_avg, final_item)

def find_probs(probs):
  cumulative_probs = 1.000000
  for i in range(0, len(probs)):
    cumulative_probs *= probs[i]
  return cumulative_probs

def solve_cases(input_name, output):
  fin = open(input_name)
  fout = open(output, 'w')

  inputline = fin.readline()
  numcase = int(inputline)
  for i in range (0,numcase):
    line = fin.readline().split()  
    num_cores = int(line[0])
    req_cores = int(line[1])
    units = float(fin.readline())
    probs = map(float, fin.readline().split())

    #print "units:"+str(units)
    #print probs    
    complete_deficit = find_deficits(probs, 1.0000000)
    if complete_deficit <= units:
      final_probs = 1.000000
    else:
      start_avg = find_avg(probs, len(probs), 0.000000)        
      #total_deficit = find_deficits(probs, avg)   
  
      final_avg = start_avg + (units / num_cores)
      probs = sorted(probs)
      new_mod_avg = find_allocated_avg(probs, units, final_avg, len(probs))
      new_probs = allocate_units(probs, units, new_mod_avg)
      final_probs = find_probs(new_probs)



    
    answer = "Case #"+str(i+1)+": "+ str("%0.6f" %final_probs) + "\n"

    print answer,
    fout.write(answer)
    #fout.write('\n')
  fin.close
  fout.close


sample_input = "c_sample_input.txt"
sample_output = "c_sample_output.txt"
small_input =  "C-small-1-attempt0.in"
small_output = "C-small-out.txt"
large_input =  "C-large.in"
large_output = "C-large-out.txt"

solve_cases(small_input, small_output)