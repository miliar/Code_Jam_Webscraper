#!/usr/bin/python

inputs = 'A-small-attempt0.in'

lines   = [line.strip() for line in open(inputs)]
T       = int(lines[0])
case    = 1
out     = ''
y       = 0
total   = 0
voc = ['a','e','i','o','u']

for x in xrange(1, T+1):
    ex      = lines[x].split(' ')
    s       = ex[0]
    c       = int(ex[1])
    total   = 0
    while s:
        s2 = s
        while s2:
            for a in s2:
                if a in voc:
                    y = 0
                else:
                    y += 1

                if y == c:
                    total +=1
                    break
            y = 0
            s2 = s2[:-1]
        s = s[1:]
    out = 'Case #%i: %i' % (x, total) 
    print out
    # print total



# test = 'gcj'
# test2 = test[:-1]
# x = 2
# n = 0
# y = 0


# # for a in test:
# #     if a in voc:
# #         y = 0
# #     else:
# #         y += 1
# #     if y == x:
# #         print test
# #         break
# #     print y
# # y = 0

# while test:
#     test2 = test
#     while test2:
#         for a in test2:
#             if a in voc:
#                 y = 0
#             else:
#                 y += 1

#             if y == x:
#                 print test2
#                 break
#         y = 0
#         test2 = test2[:-1]

#     test = test[1:]