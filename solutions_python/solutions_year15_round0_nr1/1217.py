f = file("A-large.in")
w = file("A-large.out", "w")
num_tests = int(f.readline().strip())
test_cases = map(str.strip, f.readlines())
f.close()


def write_case(case_num, answer):
    w.write("Case #"+str(case_num+1)+": "+str(answer)+"\n")


for count, case in enumerate(test_cases):
    audience = map(int, case.split(" ")[1])
    num_clappers = 0
    num_friends = 0
    for shyness, people_count in enumerate(audience):
        additional_people = max(0, shyness-num_clappers)
        num_friends += additional_people
        num_clappers += additional_people + people_count
    write_case(count, num_friends)

w.close()