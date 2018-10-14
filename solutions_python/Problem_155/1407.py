if __name__ == "__main__":
    test_cases = int(raw_input())
    for i in xrange(test_cases):
        line = raw_input().split()
        max_shy = int(line[0])
        audience = line[1]
        audience_up = int(audience[0])
        friends = 0
        for j in xrange(1, max_shy+1):
            if audience_up < j:
                friends += 1
                audience_up += 1
            audience_up += int(audience[j])
        print("Case #{}: {}".format(i+1, friends))
