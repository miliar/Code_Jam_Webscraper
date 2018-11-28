def xor2(x, y): return x ^ y
def add(x, y): return x + y

src_file = "input_candy.txt"
dest_file = "output_candy.txt"
candies = 0
count = -1
out_list = []
per_bag_out = ""
with open(src_file, 'r') as src:
    for line in src:
        count += 1
        tokens = line.split()  
        if count > 0 and count % 2 == 0:
            total_xor = total_sum = 0;
            list_of_candies = []
            for i in range(candies):
                list_of_candies.append(int(tokens[i]))
                total_xor = total_xor ^ int(tokens[i])
                total_sum = total_sum + int(tokens[i])
            if total_xor != 0:
                per_bag_out = "NO"    
            else:
                list_of_candies.sort()
                final_sum = total_sum - list_of_candies[0]
                per_bag_out = str(final_sum)                    
            out_list.extend(["Case ", "#", str(count / 2), ": ", per_bag_out, "\n"])
        else:
            candies = int(tokens[0])        
output_string = "".join(out_list)
with open(dest_file, 'w') as dest:
    dest.write(output_string.rstrip("\n"))
print "done"
