def find_number_of_pairs(low, high):
  number_of_pair = 0
  pairs = list()
  for n in range(low,high + 1):
    string_n = str(n)
    len_string_n = len(string_n)
    for i in range(1,len_string_n):
      string_m = string_n[-i:] + string_n[:-i]
      m = int(string_m)
      string_m = str(m)
      pair = [n,m]
      if (len(string_m) == len(string_n)):
        if (low <= n <= m <= high):
          if (n != m):
            if not pair in pairs:
              if not [m,n] in pairs:
                pairs.append(pair)
              	number_of_pair += 1
  return number_of_pair

def solve(input_line):
  input_split = input_line.split(" ")
  return find_number_of_pairs(int(input_split[0]),int(input_split[1]))

def process_tests(command_to_run):
    in_file = open('in')
    out_file = open("out","w")
    number_of_tests = int(in_file.readline())
    for test_case in range(number_of_tests):
        test_string = in_file.readline()[:-1]
        test_answer = command_to_run(test_string)
        out_file.write("Case #" + str(test_case + 1) + ": " + str(test_answer) + "\n")
    out_file.close()
    in_file.close()

process_tests(solve)
