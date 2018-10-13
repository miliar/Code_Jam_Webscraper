import sys

message_template = "Case #{x}: {y}"

def main():
    with open(sys.argv[1]) as input_file:
        tests = int(input_file.readline())

        test_num = 0
        for testcase in input_file:
            #print('Testing case: {}'.format(testcase.strip()))
            test_num += 1
            s_max, audience = testcase.strip().split()
            s_max = int(s_max)
            audience = [int(x) for x in audience]

            #print('s_max = {}\naudience = {}'.format(s_max, audience))

            friends = 0
            people_standing = 0
            for k, v in enumerate(audience):
                if people_standing >= k:
                    people_standing += v

                if people_standing < k:
                    friends += k - people_standing
                    people_standing += k - people_standing
                    people_standing += v

                #print('at {}, friends: {}, people_standing: {}'.format(k, friends, people_standing))

            print(message_template.format(x=test_num, y=friends))
if __name__ == '__main__':
    main()
