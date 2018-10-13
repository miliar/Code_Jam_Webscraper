print "hello world"

f = open('/Users/alarobric/Downloads/A-large.in', 'r')
g = open('/Users/alarobric/Downloads/A-large.out', 'w')
 
cases = int(f.readline())
 
for i in range (1, cases + 1):
    line = f.readline().split()
    numButtons = int(line.pop(0))
    print "case", i
    print numButtons, "buttons"
    
    orange = 1
    blue = 1
    storedOrange = 0
    storedBlue = 0
    time = 0
    
    for j in range (0, numButtons):
        color = line[j*2]
        position = int(line[j*2 + 1])
        
        if (color == 'O'):
        	dist = abs(orange - position)
        	if storedOrange >= dist:
        	    storedOrange = storedOrange - dist
        	    time = time + 1
        	    storedBlue = storedBlue + 1
        	    storedOrange = 0
        	elif storedOrange < dist:
        	    time = time + dist - storedOrange + 1
        	    storedBlue = storedBlue + dist - storedOrange + 1
        	    storedOrange = 0
        	orange = position
      	elif (color == 'B'):
      	    dist = abs(blue - position)
      	    if storedBlue >= dist:
      	        storedBlue = storedBlue - dist
      	        time = time + 1
      	        storedOrange = storedOrange + 1
      	        storedBlue = 0
      	    elif storedBlue < dist:
      	        time = time + dist - storedBlue + 1
      	        storedOrange = storedOrange + dist - storedBlue + 1
      	        storedBlue = 0
      	    blue = position
        
        print color, position
        print orange, blue
        print storedOrange, storedBlue
        print time, dist
        print ""
        
    print ""
    output = "Case #" + str(i) + ": " + str(time) + "\n"
    print output
    g.write(output)
    print ""
    
#3
#4 O 2 B 1 B 2 O 4
#3 O 5 O 8 B 100
#2 B 2 B 1