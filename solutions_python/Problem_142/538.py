f_in = open("A-small-attempt0.in", 'r')
f_out = open("A-small.out", 'w')

def get_int():
    return int(f_in.readline().rstrip())
def get_string():
    return f_in.readline().rstrip()

T = get_int()

def searchfor(first, second, i):
    # Check that
    return 0

def extract(first):
    y = first[0]
    for x in first:
        if x != y:
            return 0
    return y
    

def solve():
    first = get_string()
    second = get_string()
    if first == second:
        return 0
    # No way to fix it if first letters aren't the same
    if first[0] != second[0]:
        return "Fegla Won"
    changes = 0
    i = 0
    while first != second:
        #print first, second, i
        
        if first[i] != second[i]:
            # If previous of other is current:
            if i > 0:
                if first[i] == second[i-1]:
                    # Add it in - duplicate in current
                    changes += 1
                    second = second[:i] + second[i-1] + second[i:]
                    continue
                if second[i] == first[i-1]:
                    # Add it in - duplicate in current
                    changes += 1
                    first = first[:i] + first[i-1] + first[i:]
                    continue
            # If second has first's current in future
            # with everything in between = current's previous
                  
                    #if searchfor(first, second, i):

        
        # Last character
        if i == len(first) - 1 or i == len(second) - 1:
            if len(first) == len(second):
                if first != second:
                    return "Fegla Won"
            if len(first) > len(second):
                if extract(first[i:]) != second[i]:
                    return "Fegla Won"
                if extract(second[i:]) != first[i]:
                    return "Fegla Won"
                return changes + len(first[i:]) - 1
            if len(second) > len(first):
                if extract(second[i:]) != first[i]:
                    return "Fegla Won"
                if extract(first[i:]) != second[i]:
                    return "Fegla Won"
                return changes + len(second[i:]) - 1
            
        i += 1
    return changes

for i in range(1, T + 1):

    N = get_int()

    if N == 2:
        # Special case
        x = solve()
        print "Case #{1}: {0}".format(x, i)
        f_out.write("Case #{1}: {0}".format(x, i))

f_in.close()
f_out.close()
