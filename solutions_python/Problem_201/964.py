from math import ceil, floor

def solution(n, k):
    ls = n 
    rs = k
    sections_q = [n]
    sections_count = {n:1}

    count = 1
    index = 0
    while count < k:
        next_section = sections_q[index]
        num_of_same_sections = sections_count[next_section]
        index += 1
        if next_section%2 == 0:
            rest = (next_section - 1)
            small = rest // 2
            large = rest - small
            if large > 0:
                if large < sections_q[-1]:
                    sections_q.append(large)
                    sections_count[large] = num_of_same_sections
                else:
                    sections_count[large] += num_of_same_sections
                count += num_of_same_sections
                

            if count < k:
                if small > 0:
                    if small < sections_q[-1]:
                        sections_q.append(small)
                        sections_count[small] = num_of_same_sections
                    else:
                        sections_count[small] += num_of_same_sections
                    count += num_of_same_sections
            else:
                break

        else:
            half = next_section // 2            
            if half > 0:
                if half < sections_q[-1]:
                    sections_q.append(half)
                    sections_count[half] = 2*num_of_same_sections
                else:
                    sections_count[half] += 2*num_of_same_sections
                count += 2 * num_of_same_sections
        #print(sections_count, sections_q)
    
    last_section = sections_q.pop()
    rest = last_section - 1
    small = rest // 2
    large = rest - small
    return large, small


# input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
total = int(input())  # read a line with a single integer
for i in range(1, total + 1):
  n, k = [int(s) for s in input().split(" ")]  # read a list of integers, 2 in this case
  Ms, ms = solution(n, k)
  print("Case #{}: {} {}".format(i, Ms, ms))
  # check out .format's specificatin for more formatting options