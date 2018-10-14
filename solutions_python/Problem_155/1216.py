import sys
def ova(input_str):
    l = [elem for elem in input_str]
    friends_req = 0
    total_friends = 0
    total_person_stood = 0
    for min_person_req, person_count in enumerate(l):
        min_person_req = int(min_person_req)
        person_count = int(person_count)
        if person_count == 0:
            continue
        if (total_person_stood < min_person_req):
            friends_req = min_person_req - total_person_stood
            total_friends += friends_req
            total_person_stood = total_person_stood + friends_req + person_count
        else:
            total_person_stood = total_person_stood + person_count
                
    return total_friends
        
if __name__=="__main__":
    fread=open(sys.argv[1],'r')
    total_case=fread.readline().strip()
    for case in range(int(total_case)):
        smax,x=fread.readline().strip().split(" ")

        print "Case #{0}: {1}".format(case+1, ova(x) )
