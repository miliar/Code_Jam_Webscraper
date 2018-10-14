__author__ = 'Gauthier'

def should_split(max_p, eaters, rest_time):
    nb_occ = eaters.count(max_p)
    return max_p / 2 + nb_occ < rest_time

# def main(input_file):
#     f = open(input_file)
#     lines = map(lambda x: x.strip(), list(f))
#     num_cases, lines = int(lines[0]), lines[1:]
#     for i in range(num_cases):
#         eaters = map(int, lines[i*2+1].split(' '))
#         time = 0
#         max_time = max(eaters)
#         # print "MAX TIME", max_time
#         while max(eaters) > 0:
#             # print "time", time, "max time", max_time
#             max_p = max(eaters)
#             idx = eaters.index(max_p)
#             if max_p % 2 == 0 and should_split(max_p, eaters, max_time - time):
#                 # print "avant", eaters
#                 eaters.append(max_p/2)
#                 eaters[idx] = max_p/2
#                 # print "apres", eaters
#             else:
#                 eaters = [ e - 1 if e > 0 else 0 for e in eaters  ]
#             time += 1
#         print "Case #{}: {}".format(i+1, min(time, max_time))
#     f.close()

def main(input_file):
    f = open(input_file)
    lines = map(lambda x: x.strip(), list(f))
    num_cases, lines = int(lines[0]), lines[1:]
    for i in range(num_cases):
        eaters = map(int, lines[i*2+1].split(' '))
        max_p = max(eaters)
        t = 2
        while t < max_p:
            ans = min(max_p, sum([(x-1)])+t)
            t += 1
        print "Case #{}: {}".format(i+1, min(time, max_time))
    f.close()

if __name__ == "__main__":
    main("B-small-attempt1.in")
