import sys

#input = open('test.in')
input = open('C-large.in')
#output = sys.stdout
output = open('C-large.out','w')
    
def myread():
    return input.readline().rstrip("\n\r")

def int_ize(an_array):
    return map(lambda x: int(x), an_array)

def main():
    n_cases = int(input.readline())
    
    case_no = 1
    while case_no <= n_cases:
        case_result = solve_case()
        output.write("Case #%d: %s\n" % (case_no, case_result))
        case_no+=1
    
def solve_case():
    (r,k,ngroups) = int_ize(myread().split(" "))
    group = int_ize(myread().split(" "))
    
    # Keep here a list of 'group numbers that are at the head of the line for the ith ride'
    heads = [0]
    # Here is a hash of the 'the group was already at the head of the line is X'
    gains = {}
    # Money earned by the roller coaster when the group heads[i] was at the head of the line
    gains_array = []
    
    # Part A: Discover the loop. There has to be a loop at most by the ngroup'th element
    head = 0
    while True:
        # Calculate how much people fit in the train and who will be standing in the head of the line next
        space = k
        for i in range(head,ngroups)+range(0,head):
            if group[i] > space:
                head = i
                break
            space -= group[i]
        gains[heads[-1]] = True
        gains_array.append(k - space)
    
        # Did we already have this group at the start of the line?
        if head in gains:
            # Where in the order of group heads does the loop restart?
            m = heads.index(head)
            break
        else:
            heads.append(head)
            
    #print "m = %d, heads = %s, gains_array = %s" % (m, heads, gains_array)
    
    # Part B: Calculate totals taking into account the looping that will happen
    total_revenue = 0
    
    # 1: Leading part
    if r < m:
        return kaching(gains_array[0:k])
    else:
        total_revenue += kaching(gains_array[:m])
    
    # 2: Loop
    loops = (r-m) / (len(heads)-m)
    total_revenue += loops*kaching(gains_array[m:])
    #print "%d loops from %d on" % (loops, m)
    
    # 3: Trail end
    #print "trailing is from %d to %d" % (m,m+(r-m)%(len(heads)-m))
    total_revenue += kaching(gains_array[m:m+(r-m)%(len(heads)-m)])

    return total_revenue

def kaching(the_array):
    if not the_array:
        return 0
    else:
        return reduce(lambda x,y: x+y, the_array)

main()
