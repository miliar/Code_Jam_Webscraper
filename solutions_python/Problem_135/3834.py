
class Solver:
    """docstring for ClassName"""
    def __init__(self, arg):
        super(ClassName, self).__init__()
        self.arg = arg
        

if __name__ == "__main__":
    from GCJ import FileWrapper
    from sys import argv, stderr
    #print(argv)
    filepath = argv[1]
    outfile = argv[2]
    print filepath
    fw = FileWrapper(open(filepath, 'r'))
    cases_count = fw.getInt()
    text = ''
    #print cases_count

    for cases in range(1,cases_count+1):

        first_option = fw.getInt()
        #print first_option
        first_order = []
        second_order = []
        for raw in range(1,5):
            first_order.append( fw.getInts() )
        # print raws
        first_option_list = set(first_order[first_option-1])

        second_option = fw.getInt()
        #print second_option
        for raw in range(1,5):
            second_order.append(fw.getInts())
        second_option_list = set(second_order[second_option-1])
        x_result = first_option_list & second_option_list
        result = len(x_result)

        if result > 1:
            output = 'Bad magician!'
        elif result == 0:
            output = 'Volunteer cheated!'
        elif result == 1:
            output = list(x_result)[0]
        
         
        text = text.join(["Case #%d: %s \n" % (cases, output)])
        open(outfile, 'a').write(text)
    print text