def create_directories(to_create, existing):
    dirs = to_create.split("/")
    cur_dict = existing
    count = 0
    for d in dirs:
        if d not in cur_dict:
            cur_dict[d] = {}
            count += 1
        cur_dict = cur_dict[d]
    return count

if __name__ == "__main__":
    n = int(raw_input())

    for i in range(1, n+1):
        N, M = map(int, raw_input().split())
        existing = {}
        for j in range(N):
            new_dir = raw_input()[1:]
            create_directories(new_dir, existing)
        count = 0
        for j in range(M):
            new_dir = raw_input()[1:]
            count += create_directories(new_dir, existing)
        print "Case #%d: %d" % (i, count)
