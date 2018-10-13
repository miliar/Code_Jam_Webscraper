import math

class BathroomStalls(object):

    def __init__(self):
        self.T = None
        self.PARAMS = []
        self.read_input()
        self.OUTPUT=[]

    def read_input(self):
        self.T = int(raw_input())
        for i in xrange(1, self.T + 1):
            line = str(raw_input())
            params = line.split(" ")
            N = int(params[0])
            K = int(params[1])
            self.PARAMS.append((N, K))

    def simulate_all(self):
        for i in range(0, self.T):
            self.simulate(self.PARAMS[i][0], self.PARAMS[i][1])

    def simulate(self, N, K):
        OCCUPANCY_ARRAY = [0, N+1]
        # print "Input_PARAMS:{} {}".format( N, K)
        # print OCCUPANCY_ARRAY
        global_min = -0.5
        global_max = -0.5

        for i in range(0, K):
            global_min = -0.5
            global_max = -0.5
            # print "K={}".format(i)
            global_index_list = []

            for idx in range(0, len(OCCUPANCY_ARRAY)-1):
                left_stall = OCCUPANCY_ARRAY[idx]
                right_stall = OCCUPANCY_ARRAY[idx+1]

                empty_seats = right_stall-left_stall-2
                Ls = int(math.floor((empty_seats)/2.0))
                Rs = int(math.ceil((empty_seats)/2.0))
                local_min = min([Ls, Rs])
                local_max = max([Ls, Rs])
                seat_occupied = left_stall+Ls+1

                # print "parsm: {}, {}, {}, {}".format(Ls, Rs, empty_seats, seat_occupied)

                if local_min > global_min:
                    global_min = local_min
                    global_max = local_max
                    global_index_list=[]
                    global_index_list.append((idx, seat_occupied))
                elif local_min == global_min:
                    if local_max > global_max:
                        global_max = local_max
                        global_index_list = []
                        global_index_list.append((idx, seat_occupied))
                    elif local_max == global_max:
                        global_index_list.append((idx, seat_occupied))

            # print global_index_list
            # print global_index_list[0]
            index = global_index_list[0][0]
            val = global_index_list[0][1]
            left_buffer = index+1
            # right_buffer = (len(OCCUPANCY_ARRAY)-index-1)
            OCCUPANCY_ARRAY[left_buffer:left_buffer] = [val]

        self.OUTPUT.append((global_max, global_min))
        # print "gloabl: {} {}".format(global_max, global_min)
        # print "OCCUPANCY_ARRAY={}".format(OCCUPANCY_ARRAY)

    def print_stats(self):
        # print self.T
        # print self.PARAMS
        with open("output.txt", "w") as f:
            for i, num in enumerate(self.OUTPUT):
                str =  "Case #{0}: {1} {2}".format(i+1, num[0], num[1])
                print str
                f.write(str+"\n")


if __name__ == "__main__":
    BSObj = BathroomStalls()
    BSObj.simulate_all()
    BSObj.print_stats()
