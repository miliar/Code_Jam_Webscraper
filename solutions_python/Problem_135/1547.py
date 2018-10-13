class ProblemFileIO(object):
    def __init__(self, filename, case_function):
        self.input_file = open(filename + '.in', 'r')
        self.output_file = open(filename + '.out', 'w')
        self.case_num = 1
        self.case_function = case_function
        self.number_of_cases = read_int(self.input_file)
        
    def close(self):
        self.input_file.close()
        self.output_file.close()
        
    def case_generator(self):
        for i in xrange(self.number_of_cases):
            yield self.case_function(self.input_file)
    
    def write_result(self, result):
        self.output_file.write('Case #%d: %s\n' % (self.case_num, result))
        self.case_num += 1
            
def read_int(file_object):
    return int(read_string(file_object))
    
def read_int_list(file_object, separator):
        line = read_string(file_object)
        number_strings = tuple((line.split(separator)))
        return [int(item) for item in number_strings]
    
def read_string(file_object):
    line = file_object.readline()
    if ('\n' == line[-1]):
        line = line[:-1]
    return line