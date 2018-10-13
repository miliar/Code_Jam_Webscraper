import functools
import itertools
# Sean is very good and __fast__ at maths !

def patrick_add_naive(ea, eb):
    """WTF version for display"""
    
    a = [x for x in bin(ea)]
    b = [x for x in bin(eb)]
    a.reverse()
    b.reverse()
    a = a[:-2]
    b = b[:-2]
    la = len(a)
    lb = len(b)
    a.reverse()
    b.reverse()
    if la != lb:
        lcompl = [c for c in abs(la - lb) * '0']
        if la < lb:
            a = lcompl + a
        else:
            b = lcompl + b
    lr = [repr(int(a) ^ int(b)) for (a, b) in zip(a, b)]
    binr = ''.join(lr)
    return int(binr, 2)

def patrick_add(a, b):
    return a ^ b

def patrick_add_pile(l):
    return functools.reduce(lambda x, y: x ^y, l)

def sean_split(l):
    if len(l) == 0:
        return 'NO'
    l.sort(reverse=True)

    for sean_pick in reversed(range(1, len(l))): # combien de bonbons pour sean N - 1 .. 1*
        list_of_choices = []
        for choice in itertools.combinations(range(0, len(l)), sean_pick):
            sean_pile = [l[x] for x in choice]
            sean_sum = functools.reduce(lambda x, y: x + y, sean_pile)
            list_of_choices.append([sean_pile] + [sean_sum] + list(choice))
            list_of_choices.sort(reverse=True)
        for choice in list_of_choices:
            sean_pile = choice[0]
            sean_real_sum = choice[1]
            ndx_taken = choice[2:]
            patrick_pile = []
            for j in range(0, len(l)):
                if j not in ndx_taken:
                    patrick_pile.append(l[j])
            sum_sean = patrick_add_pile(sean_pile)
            sum_patrick = patrick_add_pile(patrick_pile)
            if sum_sean == sum_patrick:
                return sean_real_sum

    return 'NO'
    
def atest(a, b):
    """Fun pour doctest

    >>> atest(12, 5)
    9
    >>> atest(5, 4)
    1
    >>> atest(7, 9)
    14
    >>> atest(50, 10)
    56
    """
    print(patrick_add(a, b))

def cas(i, l):
    print('Case #{}: {res}'.format(i, res=sean_split(l)))
   
# import doctest    
# doctest.testmod()
T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    li = input()
    l = [int(x) for x in li.split()]
    cas(tc, l)
