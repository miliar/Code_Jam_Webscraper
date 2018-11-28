import sys

f = open(sys.argv[1], 'r')
of = open("out.out", 'w')


num_cases = int(f.readline())
for test, line in enumerate(f): # read rest of lines
    array = []
    num_friends = 0
    array = line.split()
    current_applause = 0
    while(current_applause < int(array[0])):
        if( str(array[1])[current_applause] == '0'):
             current_applause+=1
             num_friends+=1
        else:
             pos = current_applause
             current_applause += int(str(array[1])[current_applause])
             while current_applause > pos and int(array[0]) > current_applause:
                 pos+=1
                 current_applause+=int(array[1][pos])
    of.write("Case #" + str(test) + ": " + str(num_friends)+"\n")                 
