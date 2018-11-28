def good_read(f):
    return f.readline().replace("\n","")

def read_line_and_split(f, splitter=" "):
    return good_read(f).split(splitter)

def read_int_line(f):
    return int(good_read(f))

def read_int_arr(f):
    return map(int, read_line_and_split(f))

def read_input(f):
    R, C = read_int_arr(f)
    rows = []
    for r in range(R):
        rows.append(list(good_read(f)))
    return rows


def main(inf, outf):
    fr = open(inf)
    fw = open(outf, 'w')
    T = read_int_line(fr)
    for i in range(T):
        pattern = read_input(fr)
        print "\nCase #%d" % (i + 1)
        res = "Case #%d:\n%s\n" % (i+1, result(pattern))
        fw.write(res)
    fw.close()
    fr.close()

def replace_4blues_2red(pattern, hi, wi):
    replaced = False
    if  pattern[hi][wi:wi+2] == ["#","#"] and \
        pattern[hi+1][wi:wi+2] == ["#","#"]:
        pattern[hi][wi:wi+2] = ["/","\\"]
        pattern[hi+1][wi:wi+2] = ["\\","/"]
        replaced = True
        
    return pattern, replaced

def start_replacing(pattern):
    h,w = len(pattern), len(pattern[0])
    hi, wi = 0, 0
    while hi < h-1:
        while wi < w-1:
            pattern, is_replaced = replace_4blues_2red(pattern, hi, wi)
            wi+=2 if is_replaced else 1
        hi+=1
        wi = 0
    return pattern

def result(pattern):
    orig_pattern = pattern
    result_pattern = start_replacing(pattern)
    result_txt = "\n".join(["".join(row) for row in result_pattern])
    if "#" in result_txt:
        return "Impossible"
    else:
        return result_txt

if __name__ == "__main__":
    main("A-large.in","test-out.txt")
  