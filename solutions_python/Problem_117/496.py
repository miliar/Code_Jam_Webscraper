import re, numpy

class Lawn(object):
    def __init__(self, file_iter=None):
        if not file_iter:
            raise ValueError
        found_numbers = re.findall(r"\d+",file_iter.next())
        if not found_numbers or len(found_numbers) != 2:
            raise ValueError
        self.N_rows, self.N_columns = map(int, found_numbers)
        self.square = numpy.zeros(shape=(self.N_rows,self.N_columns))
        self.read_lawn(file_iter)
        self.check_result()        
    def read_lawn(self, file_iter):
        n_line = 0
        while 0 in self.square:
            line = re.findall(r"\d+",file_iter.next())            
            if line:
                self.square[n_line] = map(int, line)
                n_line += 1
    def check_result(self):
        self.cut_procedure()
        if (self.square == self.procedure_result).all():
            self.result = 'YES'
        else:
            self.result = 'NO'
    def cut_procedure(self):
        #Procedure for the columns
        procedure_column = self.square.max(0).tolist()
        if isinstance(procedure_column[0], list):
            procedure_column = procedure_column[0]
        procedure_column = map(int,procedure_column)
        #Procedure for the rows
        procedure_row = self.square.max(1).tolist()
        if isinstance(procedure_row[0], list):
            procedure_row = [item[0] for item in procedure_row]
        base = numpy.zeros(shape=(self.N_rows,self.N_columns))
        for i in range(self.N_rows):
            for j in range(self.N_columns):
                base[i][j] = min(procedure_row[i],procedure_column[j])        
        self.procedure_result = base
                      
#Reading the input file
with open("B-large.in", 'r') as file_obj:
    file_iter = iter(file_obj.readline,'')  #filedata = file.read()
    lawns = []
    try:
        while True:        
            found_number = re.search(r"\d+",file_iter.next())
            if found_number:
                N_lawns = int(found_number.group(0))
                lawns = [Lawn(file_iter) for i in range(N_lawns)]                
                break
    except (StopIteration, ValueError):
        print len(lawns)
        pass

#Writing the output file
output = '\n'.join(['Case #{0}: {1}'.format(n+1,lawn.result) for n,lawn in enumerate(lawns)])
with open("lawmower.out", 'w') as file_obj:
    file_obj.write(output)
