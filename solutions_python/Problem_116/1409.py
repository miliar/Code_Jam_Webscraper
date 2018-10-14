def check(l,name):
    assert len(l)==4,l

    l=map(lambda x:(x in [name,'T']),l)
    return sum(l)==4

def select(map_):

    for i in range(4):
        yield map_[i]

        yield [x[i] for x in map_]

    yield [map_[i][i] for i in range(4)]
    yield [map_[i][3-i] for i in range(4)]

def init(name):
    with open(name) as f:
        num=int(f.readline())

        count=0
        map_=[]
        for i in f:
            i=i.strip()

            if i:
                map_.append(list(i))
                
            else:
                yield count,map_

                map_=[]
                count+=1

        assert count==num

def solve(map_):
    for i in select(map_):

        if check(i,'O'):
            return 'O won'

        if check(i,'X'):
            return 'X won'

    if not any('.' in x for x in map_) :
        return 'Draw'
    else :
        return 'Game has not completed'

for count,map_ in init(raw_input()):
   
    print 'Case #{}: {}'.format(count+1,solve(map_))
