#!/usr/bin/python

def solve(seat_c, ppl_c, ticket_c, tickets):
    ticket_by_seat = {}
    ticket_by_person = {}
    for i in xrange(1, seat_c + 1):
        ticket_by_seat[i] = []
    for i in xrange(1, ppl_c + 1):
        ticket_by_person[i] = []
    for ticket in tickets:
        ticket_by_person[ticket["person_id"]].append(ticket)
        ticket_by_seat[ticket["seat_id"]].append(ticket)
    num_rides = 0
    for person_id, ticket_list in ticket_by_person.iteritems():
        if len(ticket_list) > num_rides:
            num_rides = len(ticket_list)
    tickets_so_far = 0
    for i in xrange(1, seat_c + 1):
        tickets_so_far += len(ticket_by_seat[i])
        rides_needed_so_far = tickets_so_far / i
        if tickets_so_far % i != 0:
            rides_needed_so_far += 1
        if num_rides < rides_needed_so_far:
            num_rides = rides_needed_so_far
    promotions = 0
    for i in xrange(1, seat_c + 1):
        if len(ticket_by_seat[i]) > num_rides:
            promotions += len(ticket_by_seat[i]) - num_rides
    return str(num_rides) + " " + str(promotions)




import sys
input_lines = open(sys.argv[1], "rt").readlines()
stripped_input_lines = [line.strip() for line in input_lines]
num_tests = int(input_lines[0])
#print num_tests

i=1
current_line = 1
while len(stripped_input_lines) > current_line:
    #print "new test!!!!!!!!!!!"
    test_line = stripped_input_lines[current_line]
    #print test_line
    seat_c = int(test_line.split()[0])
    ppl_c = int(test_line.split()[1])
    ticket_c = int(test_line.split()[2])
    current_line += 1
    current_test_line = 0
    tickets = []
    while current_test_line < ticket_c:
        test_line = stripped_input_lines[current_line + current_test_line]
        seat_id = int(test_line.split()[0])
        person_id = int(test_line.split()[1])
        ticket = {"seat_id" : seat_id, "person_id" : person_id}
        tickets.append(ticket)
        current_test_line += 1
    current_line += ticket_c
    result = solve(seat_c, ppl_c, ticket_c, tickets)
    print "Case #"+str(i)+": "+str(result)
    i+=1
