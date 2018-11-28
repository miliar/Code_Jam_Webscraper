class Case:
    def __init__(self, id_case, file_in, file_out):
        self.res = ""
        self.N = None
        self.id_case = id_case
        self.read(file_in)
        self.solve()
        self.write_output(file_out)

    def read(self,file):
        self.N = int(file.readline())

    def write_output(self,file):
        file.write("Case #"+str(self.id_case)+": "+str(self.res)+"\n")

    def is_tidy(self, table_number):
        for i in range(len(table_number)-1):
            if table_number[i] > table_number[i+1]:
                return False
        return True

    def to_table(self, number):
        table_number = []
        while (number != 0 ):
            weak = number - (number//10)*10
            table_number.insert(0,weak)
            number = number//10
        return table_number
    
    def to_int(self, table_number):
        number = 0
        for i in table_number:
            number = 10 * number + i
        return number

    def solve(self):
        print("############ CASE : "+str(self.id_case))
        table_N = self.to_table(self.N)
        number = self.N
        while not self.is_tidy(self.to_table(number)):
            number -= 1
        self.res = str(number)


file_in = open("B-small-attempt2.in",'r')
file_out = open("data.out", 'w')
for i in range(int(file_in.readline())):
    Case(i+1,file_in,file_out)
