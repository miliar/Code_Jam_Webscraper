def standing_ovation(test_case_arr):
    max_shyness = int(test_case_arr[0].strip())
    audience = test_case_arr[1].strip()
    total = 0
    required = 0
    
    for i in range(0,len(audience)):
        members = int(audience[i])
        diff = i - total
        if diff > 0:
            total += diff
            required += diff
        total += members

    return required

file_name = "A-large"
file_handle = open(file_name + ".in")
output_file = open(file_name + ".out", 'w')

test_cases = int(file_handle.readline())

for x in range(0,test_cases):
    required = standing_ovation(file_handle.readline().split(" "))
    output_file.write("Case #{0}: {1}\n".format(str(x+1),str(required)))

file_handle.close()
output_file.close()
