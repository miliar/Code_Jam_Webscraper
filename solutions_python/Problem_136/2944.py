
#            C   F      X
def solve(casen, cost, prod, goal):
    vel = 2.0
    ret = goal / vel
    inv_sum = 1 / vel
    last = ret
    farm_amount = 1
    while(last <= ret):
        last = cost * inv_sum + goal / (2 + prod * farm_amount)
        ret = min(ret, last)
        inv_sum += 1 / (2 + farm_amount * prod)
        farm_amount += 1
    print "Case #%d: %s" % (casen, ret)

def main():
    amount = int(raw_input())
    for n in range(amount):
        r = [float(x) for x in raw_input().split(" ")]
        solve(n + 1, r[0], r[1], r[2])

if __name__ == "__main__": main()
