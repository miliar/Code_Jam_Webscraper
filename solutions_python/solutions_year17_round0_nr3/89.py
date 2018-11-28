def put_people_into_bath(length, peoples):
    p = peoples
    empty_interval= {length: 1}
    while True:
        w = max(empty_interval)
        wide_stall = empty_interval[w]
        if p > wide_stall:
            half_w = int(w/2)
            if w % 2 == 1:
                if half_w in empty_interval:
                    empty_interval[half_w] += 2 * wide_stall
                else:
                    empty_interval[half_w] = 2 * wide_stall
                    
            else:
                if half_w in empty_interval:
                    empty_interval[half_w] += wide_stall
                else:
                    empty_interval[half_w] = wide_stall
                
                if half_w - 1 in empty_interval:
                    empty_interval[half_w - 1] += wide_stall
                else:
                    empty_interval[half_w - 1] = wide_stall
            
            p -= wide_stall
            del empty_interval[max(empty_interval)]
        
        else:
            half_w = int(w/2)
            if w % 2 == 1:
                return (half_w, half_w)
            else:
                return (half_w, half_w - 1)

def phase():
    out_put = input().split(" ")
    out_put[0] = int(out_put[0])
    out_put[1] = int(out_put[1])
    return out_put

def main():
    test_times = int(input())
    for t in range(1, test_times + 1):
        stall, peoples = phase()
        y, z = put_people_into_bath(stall, peoples)
        print("Case #%d: %d %d" %(t,y,z))

if __name__ == '__main__':
    main()