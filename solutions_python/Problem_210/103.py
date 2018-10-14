
DAY = 24 * 60
HALF_DAY = DAY // 2

def is_noon_activity(activity):
    begin, end = activity
    return begin < HALF_DAY < end

class Act(object):
    def __init__(self, begin, end, person):
        self.begin = begin
        self.end = end
        self.person = person
        self.next = None
        self.to_next = 0
        self.time = end - begin

    def __str__(self):
        return "{}({}, {})".format(self.person, self.begin, self.end)

def parenting_partnering(activities_c, activities_j):
    activities_c = [Act(begin, end, "C") for begin, end in activities_c]
    activities_j = [Act(begin, end, "J") for begin, end in activities_j]
    activities = activities_c + activities_j
    time_c = sum(act.time for act in activities_c)
    time_j = sum(act.time for act in activities_j)
    activities.sort(key=lambda act:act.begin)

    num = len(activities)
    count = 0

    for i, act in enumerate(activities):
        act.next = activities[(i + 1) % num]
        act.to_next = (act.next.begin + DAY - act.end) % DAY
        if act.next.person == act.person:
            count += 1

    activities_c.sort(key = lambda act:act.to_next)
    activities_j.sort(key = lambda act:act.to_next)

    for activities, time in [(activities_c, time_c), (activities_j, time_j)]:
        if len(activities) > 1:
            while activities:
                activity = activities.pop(0)
                if activity.to_next + time <= HALF_DAY and activity.person == activity.next.person:
                    time += activity.to_next
                    merge_act = activity.next
                    activity.end = merge_act.end
                    activity.to_next = merge_act.to_next
                    activity.next = merge_act.next
                    num -= 1
                    count -= 1
    return num + count



if __name__ == "__main__":
    T = int(input())

    for i in range(T):
        num_c, num_j = map(int, input().split())

        activities_c = [tuple(map(int, input().split())) for _ in range(num_c)]
        activities_j = [tuple(map(int, input().split())) for _ in range(num_j)]
        result = parenting_partnering(activities_c, activities_j)

        print("Case #{}: {}".format(i + 1, result))

