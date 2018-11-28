import fileinput

def rle_string(source_str):
    compressed_str = []
    last_chr = None
    repeat_count = 0
    for c in source_str:
        if c != last_chr:
            if repeat_count > 0:
                compressed_str.append( (last_chr, repeat_count))
            last_chr = c
            repeat_count = 0
        repeat_count += 1
    if repeat_count > 0:
        compressed_str.append ( (last_chr, repeat_count))
    return compressed_str

def compare_rle_no_count(a,b):
    return len(a) == len(b) and min([x[0][0] == x[1][0] for x in zip(a,b)])

def count_changes_needed_to_get_to_a(a,b):
    return sum([abs(x[0][1]-x[1][1]) for x in zip(a,b)])

def solve_small(orig_a,orig_b):
    rle_a = rle_string(orig_a)
    rle_b = rle_string(orig_b)
    if not compare_rle_no_count(rle_a, rle_b):
        return "Fegla Won"
    return str(count_changes_needed_to_get_to_a(rle_a, rle_b))

def main():
    it = fileinput.input()
    num_cases = int(it.next())
    for i in range(num_cases):
        num_strs = int(it.next())
        assert(num_strs == 2)
        orig_a = it.next().strip()
        orig_b = it.next().strip()
        print "Case #%d: %s" % (i+1, solve_small(orig_a, orig_b))

if __name__ == "__main__":
    main()
