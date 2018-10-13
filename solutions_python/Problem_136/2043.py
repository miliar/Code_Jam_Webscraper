with open('B-large.in') as f:
  with open('b_large_output.txt', 'w') as out:

    # Get number of test cases
    cases = int(f.readline())

    # Iterate over each test case
    for i in range(1,cases+1):
      # Get number of lines in each test case
      row = f.readline().strip('\n').split(' ')
      row = [float(val) for val in row]
      C = row[0]
      F = row[1]
      X = row[2]

      seconds = 0
      farms = 0
      seconds_to_win_with_farm = 0
      seconds_to_win_without_farm = X / float(2)
      while seconds_to_win_without_farm >= seconds_to_win_with_farm:
        seconds_to_win_without_farm = X / float(2 + farms*F)
        seconds_to_farm = C / float(2 + farms*F)
        seconds_to_win_with_farm = seconds_to_farm + (X / float(2 + (farms+1)*F))

        if seconds_to_win_with_farm > seconds_to_win_without_farm:
          seconds += seconds_to_win_without_farm
        else:
          seconds += seconds_to_farm
          farms += 1

      result = "{0:.7f}".format(seconds)

      # Output proper result
      out.write('Case #' + str(i) + ': ' + result)
      if i < cases:
        out.write('\n')