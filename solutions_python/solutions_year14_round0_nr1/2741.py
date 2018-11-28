import pandas as pd
import sys

input_string = sys.argv[1]

input_data = pd.read_csv(input_string, header=None)

number_of_cases = input_data.iloc[0]
input_data = input_data.drop(0).reset_index(drop=True)

output_list = []
for i in range(0, number_of_cases):
    data = input_data.iloc[:10]
    input_data = input_data.drop(range(0, 10)).reset_index(drop=True)
    
    row_1 = int(data.iloc[0])-1
    data_1 = data.iloc[1:5]
    
    row_2 = int(data.iloc[5])-1
    data_2 = data.iloc[6:]
    
    data_1 = set(int(x) for x in data_1.iloc[row_1].values[0].split())
    data_2 = set(int(x) for x in data_2.iloc[row_2].values[0].split())
    
    output = data_1.intersection(data_2)
    output_list.append(output)

output_list = [str(x.pop()) if len(x) == 1
               else 'Bad magician!' if len(x) > 1
               else 'Volunteer cheated!'
               for x in output_list]
output_list = ['Case #' + str(num+1) + ': ' + x for (num, x) in enumerate(output_list)]
output = pd.DataFrame(output_list)
output.to_csv('output', header=False, index=False)
