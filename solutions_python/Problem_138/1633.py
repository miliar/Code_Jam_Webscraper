__author__ = 'iToR'

in_file_name  = "D-large.in"#"D-small-attempt1.in" #"D-small-attempt0.in"
out_file_name = "D-answer-large.out"

def warOptimal(naomi_block, sorted_ken_block):
    win_count = len(naomi_block)
    for naomi in naomi_block:
        for ken in sorted_ken_block:
            if ken > naomi:
                sorted_ken_block.remove(ken)
                win_count -= 1
                break
    return win_count

def deceitfulWarOptimal(sorted_naomi_block, sorted_ken_block):
    done = False

    test_ken_block = list(sorted_ken_block)
    while not done:
        repeat = False
        for naomi,ken in zip(sorted_naomi_block, test_ken_block):
            if naomi < ken:
                del test_ken_block[len(test_ken_block) - 1]
                del sorted_naomi_block[0]
                repeat = True
                break
        if not repeat:
            done = True
    return len(sorted_naomi_block)

def generateOutput(deceitful, honest, case):
    ans_file = open(out_file_name, "a")
    ans_file.write("Case #" + str(case) + ": ")
    ans_file.write(str(deceitful)+ " " + str(honest) +"\n")

f = open(in_file_name)

input_num = int(f.readline())

for i in range(1,input_num+1):
    num_wage = f.readline()
    naomi_block_in = f.readline()
    ken_block_in   = f.readline()

    naomi_block = [float(n) for n in naomi_block_in.split()]
    ken_block   = [float(n) for n in ken_block_in.split()]

    sorted_ken_block = sorted(ken_block)
    sorted_naomi_block = sorted(naomi_block)

    print sorted_naomi_block
    print sorted_ken_block
    generateOutput(deceitfulWarOptimal(sorted_naomi_block, sorted_ken_block), warOptimal(naomi_block, sorted_ken_block), i)