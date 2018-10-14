if __name__ == "__main__":
    t = int(input())
    for case in range(t):
        s_max, s = input().split()
        s_max = int(s_max)
        people_up = 0
        res = 0
        for s_level, n_people in enumerate(s):
            n_people = int(n_people)
            if n_people > 0 and s_level > people_up:
                friends_to_invite = s_level - people_up
                res += friends_to_invite
                people_up += friends_to_invite
            people_up += n_people
        print("Case #{0}: {1}".format(case+1, res))