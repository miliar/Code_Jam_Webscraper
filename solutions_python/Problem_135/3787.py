filename = "A-small-attempt0.in"
filename_result = "A-small-attempt0.out"

file_resource = open (filename, "r")

t = int (file_resource.readline ())

for i in range(t):
    mat_1 = []
    mat_2 = []
    row_1 = -1
    row_2 = -1
    
    row_1 = int (file_resource.readline ())
    for fila_mat in range(4):
        mat_1.append ([int (line_element_str) for line_element_str in file_resource.readline ().strip ().split ()])

    row_2 = int (file_resource.readline ())
    for fila_mat in range(4):
        mat_2.append ([int (line_element_str) for line_element_str in file_resource.readline ().strip ().split ()])

#    print mat_1
#    print mat_2

    count_search = 0
    value_search = 0
    for mat_1_element in mat_1[row_1 - 1]:
        for mat_2_element in mat_2[row_2 - 1]:
            if mat_1_element == mat_2_element:
                count_search += 1
                value_search = mat_1_element

    file_resource_result = open (filename_result, "a")
    if count_search == 0:
        file_resource_result.write ("Case #" + str(i+1) + ": " + "Volunteer cheated!"  + "\n")
    elif count_search == 1:
        file_resource_result.write ("Case #" + str(i+1) + ": " + str(value_search) + "\n")
    else:
        file_resource_result.write ("Case #" + str(i+1) + ": " + "Bad magician!" + "\n")
    
    file_resource_result.close ()

file_resource.close ()
