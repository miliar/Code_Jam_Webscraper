import sys
import os

def flip_values(line,pos_of_value,flip_counter,no_of_times):
    inCrmout = 1
    
    while inCrmout  <= flip_counter:
      if line[pos_of_value] == "-":
         line[pos_of_value] = "+"
         
      else:
         line[pos_of_value] = "-"
       
      pos_of_value += 1
      inCrmout += 1
      #print "inCrmout-pos_of_value-flip_counter-line", inCrmout, pos_of_value, flip_counter,line
    
   
    return line


def recur_loop(line,value_pos,no_of_times,flip):


    #print "comes to recur_loop", line,value_pos,no_of_times,flip

    incr = 0
    totl_leng_str = len(line)
    #print "length of line", totl_leng_str
    while incr <= len(line):
      #print "incr", incr
      if incr < totl_leng_str:
         if line[incr] == "-":
            tot_len = (totl_leng_str - incr)
            #print "line value", line, tot_len, flip 
            if tot_len  >= flip:
               line = flip_values(line,incr,flip,no_of_times)
               no_of_times = no_of_times + 1
               #print "flipped", line, no_of_times 
               incr =  1
                    
            else:
               print "impossible to flip"
               no_of_times = 'IMPOSSIBLE'
               break 
         else:
            incr = incr + 1
      else:
         incr = incr + 1
         no_of_times = 'IMPOSSIBLE'

      if line.count(line[0]) == len(line):
          break
 
    return no_of_times  

def check_len(line,flip):

    flip = int(flip)
    no_of_times = 0 
    if line[0] == "+" : 
       if line.count(line[0]) == len(line):
          return 0
       else:
         incr = 0
         while incr <= len(line):  
             if line[incr] == "-":
                value_pos = incr
                break
             incr = incr + 1
         return recur_loop(line,value_pos,no_of_times,flip)
    
    if line[0] == "-" :
       incr = 0
       while incr <= len(line):
              if line[incr] == "-":
                 value_pos = incr
                 break
              incr = incr + 1
       return recur_loop(line,value_pos,no_of_times,flip)
          
          

def main(args=None):
    
    target = open("/home/siyer/code_jam/result.txt", 'w')
    target.truncate()
    f = open("/home/siyer/code_jam/input.txt")
    next(f)
    cnt= 0
    for line in f:
        cnt = cnt + 1
        
        linestr,k = line.split(' ')
        linestr = linestr.strip()
        content =  [] 
        if linestr:
           print "line", cnt
           content.extend([(x).strip() for x in linestr])
        counter= check_len(content,k)
        target.write( "Case #"+ str(cnt) + ": "+ str(counter)) 
        target.write("\n")
   
    target.close()

if __name__ == "__main__":
    sys.exit(main())

