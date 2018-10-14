T = int(raw_input())
table = {'1': {'1':(1,'1'), 'i':(1,'i'),'j':(1,'j'), 'k':(1,'k')},
         'i': {'1':(1,'i'), 'i':(-1,'1'),'j':(1,'k'), 'k':(-1,'j')},
         'j': {'1':(1,'j'), 'i':(-1,'k'),'j':(-1,'1'), 'k':(1,'i')},
         'k': {'1':(1,'k'), 'i':(1,'j'),'j':(-1,'i'), 'k':(-1,'1')}}

def product(a, b):
    sign, sym = a
    new_sign, new_sym = table[sym][b[1]]
    return (sign*new_sign*b[0], new_sym)

divide_table = {}

def generate_divide_table():
    for sym in table:
        divide_table[sym] = {}
    for sym in table:
        for key in table[sym]:
            sign, symbol = table[sym][key]
            #print sym, key,':', sign, symbol
            divide_table[symbol][sym] = (sign, key)
            
generate_divide_table()

def divideleft(a, b):
    sign, sym = a
    new_sign, new_sym = divide_table[sym][b[1]]
    return (sign*new_sign*b[0], new_sym)

def findijk(x,chars):
    l = len(chars)
    record = [(1,'1') for _ in ' '+chars]
    power = [(1,'1'), None, None, None]
    for i in xrange(l):
        record[i+1] = product(record[i], (1, chars[i]))
    #print record
    left_record = [ [item for item in record] ]
    right_record = [ [divideleft(record[-1], item) for item in record]]
    for i in xrange(1,4):
        power[i] =  product(power[i-1], record[-1])
    #print power
    for i in xrange(1,4):
        left_record.append([product(record[-1], item) for item in left_record[i-1] ])
        right_record.append([product(item, record[-1]) for item in right_record[i-1] ])
    #print left_record, right_record


    for i in xrange(4):
        for j in xrange(4):
            if i + j > x -1:
                break
            left = [index for index, char in enumerate(left_record[i]) if char == (1,'i')]
            right = [index for index, char in enumerate(right_record[j]) if char == (1,'k')]
            if len(left) == 0 or len(right) == 0:
                continue
            #print i,j, len(left), len(right)
            if i + j == x - 1:
                start = 0
                #print len(left),len(right)
                for index_left in left:                    
                    for index_right in right[start:]:
                        if index_left > index_right:
                            start += 1
                        else:
                            #print index_left, index_right
                            #print record[index_right], record[index_left]
                            if divideleft(record[index_right], record[index_left]) == (1,'j'):
                                #print l,':', i, index_left, index_right, j
                                return True
            if i + j < x - 1:
                middle = power[(x - 2 - i - j) % 4]
                for index_left in left:
                    for index_right in right:
                        #print record
                        #print right_record[0]
                        #print index_left, index_right                        
                        #print record[index_right], middle,right_record[0][index_left]
                        temp = product(right_record[0][index_left], middle)
                        temp = product(temp, record[index_right])
                        #print temp
                        if temp == (1,'j'):
                            #print l,':', i, index_left, (x - 2 - i - j), index_right, j
                            return True

    return False



for index in xrange(T):
    (l, x) = map(int, raw_input().split(' '))
    chars = raw_input()
    if findijk(x,chars):
        result = 'YES'
    else:
        result = 'NO'
    

    print "Case #%d: " % (index+1) + result

