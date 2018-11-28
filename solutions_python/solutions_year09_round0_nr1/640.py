class AlienLanguage(object):
    def __init__(self, input_file_name):
        trimmed_lines = [line.strip() for line in open(input_file_name).readlines() if len(line.strip()) > 0] 
        self.header = trimmed_lines[0]
        self.lines = trimmed_lines[1:]
        self.parse_input()
    
    def parse_input(self):
        header_list = self.header.split(' ')
        self.L = int(header_list[0])
        self.D = int(header_list[1])
        self.N = int(header_list[2])
        
        self.input_words = self.lines[:self.D]
        self.samples = self.lines[self.D:self.D+self.N]
        
    def solve(self):
        output_lines = []
        for i in range(len(self.samples)):
            sample = self.samples[i]
            sample_list = self.convert_sample_to_list(sample)
            success_count = self.get_count_of_success(sample_list, self.input_words)
#            total_probable_list = self.get_total_probable_list(sample_list, self.L)
#            success_list = [probable for probable in total_probable_list if probable in self.input_words]
            output_lines.append("Case #%s: %s"%(i+1,success_count))
        return output_lines
    
    @classmethod
    def get_count_of_success(cls, sample_list, input_words):
        success_count = 0
        for input_word in input_words:
            success = True
            for i in range(len(input_word)):
                if input_word[i] in sample_list[i]:
                    continue
                else:
                    success = False
                    break
            if success:
                success_count+=1
        return success_count
    @classmethod
    def convert_sample_to_list(cls, sample):
        temp = []
        multiple = False
        temp_word = ''
        for temp_char in sample:
            if temp_char == '(':
                multiple = True
                temp_word = ''
                continue
            elif temp_char == ')':
                multiple = False
                if len(temp_word) > 0:
                    temp.append(temp_word)
                    temp_word = ''
                continue
            else:
                if not multiple:
                    temp.append(temp_char)
                    continue
                temp_word = '%s%s'%(temp_word, temp_char)
        if len(temp_word) > 0:
            temp.append(temp_word)
        return temp
    
#    @classmethod
#    def get_total_probable_list(cls, input_list, L):
#        grand_total = [input_list]
#        grand_total_copy = []
#        for iteration in range(L):
#            for row in grand_total:
#                total_rows = cls.sub_method(row, iteration)
#                grand_total_copy.extend(total_rows)
#            grand_total = []
#            grand_total.extend(grand_total_copy)
#            grand_total_copy = []
#        final_total = []
#        for x in grand_total:
#            final_total.append(''.join(x))
#        return final_total
#    
#    @classmethod
#    def sub_method(cls, input_row, iteration):
#        element = input_row[iteration]
#        if len(element) > 1:
#            temp_row_list = []
#            for x in element:
#                f_row = []
#                f_row.extend(input_row)
#                temp_row_list.append(f_row)
#            for j in range(len(element)):
#                sub_element = element[j]
#                temp_row_list[j][iteration] = sub_element
#            return temp_row_list
#        else:
#            return [input_row]
            