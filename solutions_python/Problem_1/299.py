#!/usr/bin/python2.5

def find_next(query_l, c_server, start):
    Q = len(query_l)
    i = start
    while (i<Q) and (len(c_server) > 1):
        if (query_l[i] in c_server):
            c_server.remove(query_l[i])
        i += 1
    while (i<Q) and (query_l[i] != c_server[0]):
        i += 1
    return i

def main():
    for case in range(input()):
        S = int(input())
        server_l = []
        for server in range(S):
            server_l.append(raw_input())
        Q = int(input())
        query_l = []
        for query in range(Q):
            query_l.append(raw_input())

#        print '%s, %s' % (S, Q)
#        print server_l
#        print query_l
        solution = -1
        index = 0
        while (index<Q):
            c_server = server_l[:]
            if (index != 0):
                c_server.remove(query_l[index])
            index = find_next(query_l, c_server,index)
            solution += 1
            

        if (len(query_l) == 0): solution = 0

#        while (i<Q) and (len(c_server) > 1):
#            if (query_l[i] in c_server):
#                c_server.remove(query_l[i])
#            i += 1

#        if (i==Q):
#            solution = 0
#        else:
#            while (i<Q) and (query_l[i] != c_server[0]):
#                i += 1
#            if (i == Q):
#                solution = 0
#            else:
#                solution += 1
#                c_server = server_l[:]
#
#                i = 0
#                while (len(c_server) > 1) and (i < Q):
#                    if (query_l[i] in c_server):
#                        c_server.remove(query_l[i])
#                    i += 1
#
#                if (i==Q):
#                    solution = 0
#                else:
#                    while (i<Q) and (query_l[i] != c_server[0]):
#                        i += 1
#                    if (i == Q):
#                        solution = 0
        print 'Case #%s: %s' % (case + 1, solution)
main()
