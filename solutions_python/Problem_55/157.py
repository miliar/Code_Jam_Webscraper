def run_case(case_num):
    num_runs, coaster_size, num_groups = map(int, infile.readline().split())
    groups = map(int, infile.readline().split())
    assert len(groups) == num_groups

    load = 0
    riders = 0
    runs = 0
    groups_in_load = 0
    while True:
        for group in groups:
            if load + group > coaster_size or groups_in_load == num_groups:
                # print " - %s" % load
                riders += load
                load = 0
                runs += 1
                groups_in_load = 0
                if runs == num_runs:
                    print "Case #%d: %d" % (case_num, riders)
                    return
            load += group
            groups_in_load += 1

infile = file("theme-park-sample.in")
num_cases = int(infile.readline())

for c in xrange(num_cases):
    run_case(c)
