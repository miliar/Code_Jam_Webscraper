file = open("input.in", "r");
def raw_input():
    return file.readline();

cases_number = int(raw_input());
cases = [];
done = {};

out = '';

def process(cooker, size, n):
    done[cooker] = n;
    n+=1;
    if not "-" in cooker:
        return n;
    low = 999999;
    a = False;
    for index in range(len(cooker)-size+1):
        if cooker[index:index+size] == "-"*size:
            a = True;
            n+=1;
            cooker =  flip(cooker, index, size);
    if a:
        return process(cooker, size, n-1);
    for index in range(len(cooker)-size+1):
        if not flip(cooker, index, size) in done:
                low = min(low, process(flip(cooker, index, size), size, n));
        elif done[flip(cooker, index, size)]>n:
                low = min(low, process(flip(cooker, index, size), size, n));
    return low;

def flip(cooker, index, size):
    return ''.join(["+" if ((index-1<i<index+size and cooker[i] == "-") or ((index>i or i>index+size-1) and cooker[i] == "+")) else "-" for i in range(len(cooker))]);

for case in range(cases_number):
    last_input = raw_input().split(" ");
    size = int(last_input[1]);
    cooker = last_input[0];
    done = {};

    temp = process(cooker, size, 0) - 1;
    if temp == 999998:
        temp = "IMPOSSIBLE";
    out = out + "Case #"+str(case+1)+": "+str(temp)+"\n";

print out
open("outputx.in", "w").write(out);
