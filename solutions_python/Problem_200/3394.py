def ltn(input_str):
	if (len(input_str) == 1):
		return input_str
	else:
		leftmost_digit = int(input_str[0])
		remainder_ltn = ltn(input_str[1:])
		if (leftmost_digit <= int(remainder_ltn[0])):
			return("{}{}".format(leftmost_digit, remainder_ltn))
		else:
			return("{}{}".format(leftmost_digit - 1, '9' * len(remainder_ltn)))

t = int(input())
for i in range(1, t + 1):
  n = input()
  print("Case #{}: {}".format(i, ltn(n).lstrip("0")))
  
  