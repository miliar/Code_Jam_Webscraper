for _ in range(1, int(raw_input())+1):
    _c = 0
    c = {}
    _d = 0
    d = []
    _inp_ = raw_input().split()

    if int(_inp_[0]) > 0:
        _c = int(_inp_[0])
        for each in _inp_[1: 1 + _c] :
            c[each[:2]] = each[2]
            c[each[1::-1]] = each[2]
    
    _inp_ = _inp_[_c+1:]
    if int(_inp_[0]) > 0:
        _d = int(_inp_[0])
        for each in _inp_[1: 1 + _d] :
            d.extend([each[:2]])
    
    case = [_inp_[-1][:1]]
    for e in _inp_[-1][1:]:
        case.append(e)
        flag = 1
        x = c.get(''.join(case[-2:]))
        while(x):
            flag = 0
            case = case[:-2] + [x]
            x = None
            #x = c.get(''.join(case[-2:]))
        
        if flag:
            for each_d in d:
                if each_d[0] in case and each_d[1] in case:
                    case = []
    
    print 'Case #'+str(_)+':', str(case).replace("'","")
    