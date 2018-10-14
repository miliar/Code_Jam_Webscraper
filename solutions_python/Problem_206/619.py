class Horse:

    def __init__(self, position, speed):
        self.position = position
        self.speed = speed

    def time_to_destination(self, destination):
        return max([
            0,
            (destination - self.position) / self.speed
        ])


class HorseProblem:

    def __init__(self, destination):
        self.other_horses = []
        self.destination = destination

    def add_horse(self, position, speed):
        self.other_horses.append(Horse(position, speed))

    def maximum_time(self):
        return max([horse.time_to_destination(self.destination)
                    for horse in self.other_horses])

    def speed_to_use(self):
        return self.destination / self.maximum_time()


num_cases = int(input())
for i in range(1, num_cases + 1):
    destination, n_horses = [int(x) for x in input().split(" ")]
    horse_problem = HorseProblem(destination)
    for _ in range(n_horses):
        position, speed = [int(x) for x in input().split(" ")]
        horse_problem.add_horse(position, speed)
    print("Case #{}: {}".format(i, horse_problem.speed_to_use()))
