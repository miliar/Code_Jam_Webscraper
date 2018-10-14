with open('A-large.in') as file_in:
    n = int(file_in.readline().strip())
    for case_no, line in enumerate(file_in.readlines()):
        max_shy, audience = line.strip().split()
        max_shy = int(max_shy)
        so_far = 0
        added = 0
        total = 0
        for needed, a in enumerate(audience):
            current = int(a)
            if not current:
                continue
            if so_far < needed:
                to_add = needed - so_far
                added += to_add
            else:
                to_add = 0
            so_far += current + to_add
        print "Case #%s: %s" % (case_no + 1, added)
