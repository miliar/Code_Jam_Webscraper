def Iterate(n, target):
    Todo = [n];
    Done = 0;
    Dict = { n: 1 }
    
    while (True):
        Keys = Dict.keys();
        nextKey = max(Keys);
        number = Dict[nextKey];

        if (Done + number >= target):
            print nextKey/2, (nextKey-1)/2
            return;

        del Dict[nextKey];
        
        left = nextKey/2;
        right = nextKey-1-left;

        if (left in Dict.keys()):
            Dict[left] += number;
        else:
            if left != 0:
                Dict[left] = number;

        if (right in Dict.keys()):
            Dict[right] += number;
        else:
            if right != 0:
                Dict[right] = number;
            
        Done += number;

        
T = int(raw_input());
for q in range(T):
    [N, K] = map(int, raw_input().split());
    
    print "Case #%d:" % (q+1),;
    Iterate(N, K);
