                  
def get_num_adds(a, mote, num_pops):
    count = 0
    if (a <= 1):
        return num_pops
    while ((a <= mote) and ((a-1) > 0) and (count <= num_pops)):
        a += a-1
        count += 1
    return count

def get_new_size(a, num_adds):
    count = 0
    while (count < num_adds):
        a += a - 1
        count+= 1
    return a

def get_progress(a, i):
    count = 0
    while (i < len(motes) and a > motes[i]):
        a += motes[i]
        i += 1
        count+= 1
    return count

if __name__ == "__main__":
    input_file = open("A-small-attempt1.in", "r")
    num_cases = int(input_file.readline())
    for case in range(num_cases):
        a, n = [int(k) for k in input_file.readline().split()]
        i = 0;
        count = 0;
        motes = []
        for k in input_file.readline().split():
            motes.append(int(k))
        motes = sorted(motes)
        while (i < len(motes)):
            if a > motes[i]:
                a += motes[i]
                i += 1
            else:
                #calculate num_adds required to eat next mote
                pops_reqd = len(motes) - i;
                num_adds = get_num_adds(a, motes[i], pops_reqd);
                if num_adds >= pops_reqd:
                    #add pops_reqd to count and you are done
                    count += pops_reqd
                    i += len(motes);
                else:
                    new_a  = get_new_size(a, num_adds);
                    #check if num_adds moves you at least num_adds forward (this is how many motes have been eaten)
                    forward = get_progress(new_a, i);
                    if forward > ((len(motes) - 1) - i):
                        #can eat rest of the list with this many adds
                        #add this many adds to count and you are done
                        count += num_adds
                        i += len(motes)
                    else:
                        a = new_a
                        a += motes[i]
                        count += num_adds
                        i += 1
        print "Case #%d: %d" %(case + 1, count)    
    