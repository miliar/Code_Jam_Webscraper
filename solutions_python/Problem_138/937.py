import copy
input = open('input4', 'r')
output = open('output4', 'w')

def find_real_points(naomi,ken, blocks):
    result = 0
    while blocks > 0:
        if naomi[-1] > ken[-1]:
            result +=1
            del ken[0]
        else:
            del ken[-1]
        del naomi[-1]
        blocks -= 1
    return result

def find_deceitful_points(naomi, ken, blocks):
    result = 0
    while blocks > 0:
        if naomi[0] < ken[0]:
            del ken[-1]
            del naomi[0]
        else:
            result += 1
            del naomi[0]
            del ken[0]
        blocks -= 1
    return result
            

testcases = int(input.readline().strip())
for testcase in xrange(1, testcases+1):
    blocks = int(input.readline().strip())
    naomi = [float(v) for v in input.readline().strip().split(' ')]
    ken = [float(v) for v in input.readline().strip().split(' ')]
    naomi.sort()
    ken.sort()
    actual = find_real_points(copy.copy(naomi), copy.copy(ken), blocks)
    deceitful = find_deceitful_points(copy.copy(naomi), copy.copy(ken), blocks)
    output.write("Case #%s: %s %s\n" % (testcase, deceitful, actual))

input.close()
output.close()
