#! /usr/bin/python2

def main():
  # read in number of test cases
  ntc = int(raw_input())
  for i in range(ntc):
    words = raw_input().split(None)
    combiner_count = int(words[0])
    combiner_list = {}
    for j in range(combiner_count):
      combiner_list[words[j+1][:2]] = words[j+1][-1]
    destroyer_count = int(words[combiner_count+1])
    destroyer_list = words[combiner_count+2:combiner_count+2+destroyer_count]
    # we ignore number of characters
    input_string = words[combiner_count+3+destroyer_count]
    output_string = ""
    for j in range(len(input_string)):
      if output_string == "":
        output_string += input_string[j]
      else:
        # can we combine?
        combi = output_string[-1] + input_string[j]
        combi2 = input_string[j] + output_string[-1]
        if combi in combiner_list:
          output_string = output_string[:-1] + combiner_list[combi]
        elif combi2 in combiner_list:
          output_string = output_string[:-1] + combiner_list[combi2]
        else:
          output_string += input_string[j]
      # OK, now we checked for combinations!
      # let's check for deletions
      for k in range(len(output_string)-1):
        if output_string[k] + output_string[-1] in destroyer_list:
          output_string = ""
          break
        elif output_string[-1] + output_string[k] in destroyer_list:
          output_string = ""
          break
      # OK, we checked for deletions!
    # now we can output the string
    output_array = []
    for j in range(len(output_string)):
      output_array.append(output_string[j])
    print "Case #{0}: [{1}]".format(i+1, ", ".join(output_array))

if __name__ == '__main__':
  main()
