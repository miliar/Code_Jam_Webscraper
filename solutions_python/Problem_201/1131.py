def simulate(stall_size, customer_size):
    primary_dict, secondary_dict = dict(), dict()
    primary_dict[stall_size] = 1
    while True:
        if customer_size - sum(primary_dict.values()) > 0:
            for radius, count in primary_dict.items():
                customer_size -= count
                if radius & 1 == 1:
                    if secondary_dict.get(int(radius/2)) is None:
                        secondary_dict[int(radius/2)] = count * 2
                    else:
                        secondary_dict[int(radius/2)]  = secondary_dict.get(int(radius/2)) + count*2
                else:
                    if secondary_dict.get(int(radius/2)) is None:
                        secondary_dict[int(radius/2)] = count
                    else:
                        secondary_dict[int(radius/2)]  = secondary_dict.get(int(radius/2)) + count
                    if secondary_dict.get(int(radius/2)-1) is None:
                        secondary_dict[int(radius/2)-1] = count
                    else:
                        secondary_dict[int(radius/2)-1]  = secondary_dict.get(int(radius/2)-1) + count
            primary_dict = secondary_dict
            secondary_dict = dict()
        else:
            stall_list = sorted(list(primary_dict.items()), reverse=True)
#            print("customer_size:{}, list:{}".format(customer_size, stall_list))
            while True:
                if customer_size - stall_list[0][1] > 0:
                    customer_size -= stall_list[0][1]
                    del stall_list[0]
                else:
                    if stall_list[0][0] & 1 == 1:
                        return int(stall_list[0][0]/2), int(stall_list[0][0]/2)
                    else:
                        return int(stall_list[0][0]/2), int(stall_list[0][0]/2)-1


def main():
    num_of_inputs = int(input())
    for ith_input in range(1, num_of_inputs+1):
        num_of_stalls, num_of_customer = map(int, input().strip().split())
        print("Case #{}: {}".format(ith_input, " ".join(map(str, simulate(num_of_stalls, num_of_customer)))))

if __name__ == "__main__":
    main()
