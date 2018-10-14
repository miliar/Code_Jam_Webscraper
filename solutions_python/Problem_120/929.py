

file = open('./A-small-attempt0.in')
new_file = open('./A-small.out', 'w')

testcases = [ x.rstrip() for x in file.readlines() ]

for i in range(int(testcases[0])):
    testcase = testcases[i+1].split()
    testcase = [int(x) for x in testcase]
    paint = testcase[1]
    radius = testcase[0]
    odd_even = testcase[0]%2
    count = 0
    while True:
        new_radius = radius + 1
        if (new_radius%2) != odd_even:
            area = new_radius**2 - radius**2
            if paint >= area:
                count = count + 1
                paint = paint - area
            if area > paint:
                break
        radius = new_radius
    
        
    
    
    new_file.write('Case #%s: %s\n' % (i+1, count))



file.close()
new_file.close()

