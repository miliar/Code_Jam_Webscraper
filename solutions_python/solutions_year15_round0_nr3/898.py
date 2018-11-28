import heapq

def quaternion(m, n):
    if m == 1: return (n, 1)
    if n == 1: return (m, 1)
    if m == n: return ('', -1)
    if m == 'i':
        if n == 'j': return ('k', 1)
        if n == 'k': return ('j', -1)
    if m == 'j':
        if n == 'i': return ('k', -1)
        if n == 'k': return ('i', 1)
    if m == 'k':
        if n == 'i': return ('j', 1)
        if n == 'j': return ('i', -1)


def result(outcome):
    if outcome == True: return "YES"
    return "NO"


def dijkstra(string):
    sign = 1
    while len(string) > 3 and string[0] != 'i':
        (char, result_sign) = quaternion(string[0], string[1])
        string = char + string[2:]
        sign *= result_sign
    while len(string) > 3 and string[1] != 'j':
        (char, result_sign) = quaternion(string[1], string[2])
        string = 'i' + char + string[3:]
        sign *= result_sign
    while len(string) > 3:
        (char, result_sign) = quaternion(string[2], string[3])
        string = 'ij' + char + string[4:]
        sign *= result_sign
    
    return result(sign == 1 and string == "ijk")
    
        
if __name__ == '__main__':
    for T in range(int(raw_input())):
        num_chars, repeat = [int(p) for p in raw_input().split(' ')]
        string = raw_input() * repeat
        print "Case #%d: %s" % (T+1, dijkstra(string))