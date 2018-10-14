import argparse

def function(num_files, disk_cap, file_sizes):
    file_sizes.sort()
    print(file_sizes)
    
    num_disks = 0
    while len(file_sizes) > 1:
        first_file = file_sizes.pop()
        empty_space = disk_cap - first_file
        for i in range(len(file_sizes) - 1, -1, -1):
            if file_sizes[i] <= empty_space:
                file_sizes.pop(i)
                break
        num_disks += 1
        #print (file_sizes)
        
    if (len(file_sizes) == 1):
        num_disks += 1
    return num_disks

def main():
    # parse command line options
    parser = argparse.ArgumentParser()
    parser.add_argument('infile', type=str)
    args = parser.parse_args()
    outfile = args.infile.replace('.in', '.out')
    
    with open(args.infile) as f_in, open(outfile, 'w') as f_out:
        num_cases = int(f_in.readline().strip())
        for i in range(num_cases):
            num_files, disk_cap = [int(x) for x in f_in.readline().strip().split()]
            file_sizes = [int(x) for x in f_in.readline().strip().split()]
            
            result = function(num_files, disk_cap, file_sizes)
            
            outputline = "Case #{}: {}\n".format(i + 1, result)
            print(outputline)
            f_out.write(outputline)
        
# main function
if __name__ == "__main__":
    main()        