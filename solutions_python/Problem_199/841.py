def read_input_data(file_name):
    input_data = list()
    f = open(file_name)
    items = f.read().splitlines()
    f.close()
    print("Input  : {}".format(file_name))
    return items[1:int(items[0]) + 1]

def write_output_data(file_name, output_data):
    f = open(file_name, 'w')
    f.writelines(map(lambda x: x + '\n', output_data))
    f.close()
    print("Output : {}".format(file_name))
    print("Done!")
