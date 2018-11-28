def binary_devide(old_map):
    new_map = dict()
    for key in old_map:
        remain = key-1
        first_half = int(remain / 2)
        second_half = remain - first_half
        if first_half not in new_map:
            new_map[first_half] = old_map[key]
        else:
            new_map[first_half] += old_map[key]
        if second_half not in new_map:
            new_map[second_half] = old_map[key]
        else:
            new_map[second_half] += old_map[key]
    return new_map

def size(a_map):
    answer = 0
    for key in a_map:
        answer += a_map[key]
    return answer

with open("input.txt","r") as reader, open("output.txt","w") as writer:
    cases = int(reader.readline())
    for cs in range(1,cases+1):
        N,K = map(int,reader.readline().split(' '))
        cache = dict()
        cache[N] = 1
        sz = 1
        while K > sz:
            K -= sz
        #    print(cache)
            cache = binary_devide(cache)
            sz = size(cache)

        max_key = max(cache.keys(),key=int)
        min_key = min(cache.keys(),key=int)
        mn,mx = 0,0
        if K <= cache[max_key]:
            max_key -= 1
            mn,mx = int(max_key/2),int(max_key/2)+max_key%2
        else:
            min_key -= 1
            mn,mx = int(min_key/2),int(min_key/2)+min_key%2
        writer.write("Case #"+str(cs)+": "+str(mx)+" "+str(mn)+"\n")

