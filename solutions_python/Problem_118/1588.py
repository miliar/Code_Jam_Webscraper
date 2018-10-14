import bisect
def is_palindrome( data) :
    data = str(data)
    return data == data[::-1]

def palindrome_squares( limit) :
    for i in range( limit) :
        if is_palindrome( i) :
            if is_palindrome( i * i) :
                yield i * i
data = list(palindrome_squares(10**8))
n = int(raw_input())
for t in range(1,n + 1):
    A, B = map(int, raw_input().split())
    print "Case #{}: {}".format(t,len(data[bisect.bisect_left(data,A): bisect.bisect_right(data,B)]))

