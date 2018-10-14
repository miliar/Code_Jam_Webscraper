import sys
mapping = eval("{' ': ' ', 'a': 'y', 'c': 'e', 'b': 'h', 'e': 'o', 'd': 's', 'g': 'v', 'f': 'c', 'i': 'd', 'h': 'x', 'k': 'i', 'j': 'u', 'm': 'l', 'l': 'g', 'o': 'k', 'n': 'b', 'q': 'z', 'p': 'r', 's': 'n', 'r': 't', 'u': 'j', 't': 'w', 'w': 'f', 'v': 'p', 'y': 'a', 'x': 'm', 'z': 'q'}")

num_cases = int(raw_input())
for case in range(1,num_cases+1):
    print "Case #"+str(case)+":",
    line = raw_input()
    for c in line:
        sys.stdout.write(mapping[c])
    if(case != num_cases):
        print
        
#sys.stdout.write(str(tests+1))
