input_file = file(r'c:\input.txt', 'rb')
out_file = file(r'c:\output.txt', 'wb')
lines = input_file.readlines()
T = int(lines[0])
for index in xrange(0, T*2, 2):
    N_line = lines[index+1]
    N = int(N_line)
    array_line = lines[index+2]
    arr = array_line.split(' ')
    for i,element in enumerate(arr):
        arr[i] = int(element)
    result = 0
    for i,element in enumerate(arr):
        if element != i+1:
            result += 1
    out_file.write("Case #%d: %6f\n" % (index/2+1,result))
out_file.close()
input_file.close()
        
    
    
