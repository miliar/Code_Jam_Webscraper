import itertools

def is_tidy(x):
    x = str(x)
    numbers = list(x)
    numbers = [ int(q) for q in numbers ]
    numbers = sorted(numbers)
    numbers = [ str(q) for q in numbers ]
    numbers = "".join(numbers)
    if numbers == x:
        return True
    return False

results = []
num_of_in = int(input())
for inter in xrange(num_of_in):
    print("on case " + str(inter))
    N = int(input())
    for z in itertools.count(N, -1):
        if is_tidy(z):
            results.append(z)
            break
q = 0
for result in results:
    print("Case #" + str(q+1) + ": " + str(result))
    q += 1
        
