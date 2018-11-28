def tidy_numbers():
  with open('B-small-attempt0.in') as f:
    content = f.readlines()

  content = [x.strip("\n") for x in content]

  T = int(content[0])

  for i in range(1,T+1):
    N = content[i]
    
    last = last_tidy_number(N)
    print "Case #{0}: {1}".format(i, last)

def last_tidy_number(N):
  if len(N) == 1:
    return N
  else:
    curr_n = int(N)
    curr_n_mod = curr_n
    tidy = False
    while not tidy:
      arr = [int(i) for i in str(curr_n)]
      tidy = all(x<=y for x, y in zip(arr, arr[1:]))

      if not tidy:
        
        split = curr_n / 10 - 1
        split_arr = [int(i) for i in str(split)]
        if not all(x<=y for x, y in zip(split_arr, split_arr[1:])):
          split = str(split_arr[0]) + "".join([str(0) for i in range(len(str(split))-1)]) + str(9)
          curr_n = int(split) - 1
        else:
          temp_str = str(split) + str(9)
          curr_n = int(temp_str)

    return curr_n



if __name__ == "__main__":
  tidy_numbers()
