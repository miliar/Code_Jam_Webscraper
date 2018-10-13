import sys

def all_perms(v):
    if len(v) <= 1:
        yield v
    else:
        for perm in all_perms(v[1:]):
            for i in range(len(perm)+1):
                yield perm[:i] + v[0:1] + perm[i:]

def int2bin(n, count):
    return "".join([str((n >> y) & 1) for y in range(count-1, -1, -1)])

def satisfy(customer, batch):
    for flavor in customer:
        if batch[flavor[0]-1] == flavor[1]:
            return True
    return False

def solve(milkshake_n, customers):
    satisfied = [ ]
    for cur in range(2**milkshake_n):
        cur_batch = [int(x) for x in int2bin(cur, milkshake_n)]
        all_satisfied = True
        for customer in customers:
            if not satisfy(customer, cur_batch):
                all_satisfied = False
                break
        if all_satisfied:
            satisfied.append(cur_batch)

    minimum = None
    minimum_len = milkshake_n+1
    for batch in satisfied:
        l = batch.count(1)
        if l < minimum_len:
            minimum_len = l
            minimum = batch

    if minimum is None:
        return "IMPOSSIBLE"
    else:
        return " ".join([str(x) for x in minimum])

if __name__ == '__main__':
    if (len(sys.argv)) != 2:
        print "usage: %s [inputfile]" % sys.argv[0]
        sys.exit(0)

    fin = open(sys.argv[1])

    case_n = int(fin.readline())
    for i in range(case_n):
        milkshake_n = int(fin.readline())
        customer_n = int(fin.readline())
        customers = [ ]
        for j in range(customer_n):
            customer_data = [int(x) for x in fin.readline().strip().replace("\n", "").split()]
            data_n = customer_data[0]
            customer = [ ]
            for k in range(data_n):
                customer.append( tuple(customer_data[k*2+1:k*2+3]) )
            customers.append(customer)
        print "Case #%d: %s" % (i+1, solve(milkshake_n, customers))
