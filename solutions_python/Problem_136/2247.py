import csv

class CookieClicker:
	def __init__(self, C, F, X):
		self.farm_cost = C
		self.farm_rate = F
		self.goal = X
		self.cookie_rate = 2.0
		self.time_elapsed = 0.0
		self.reached_goal = False

	def add_time(self, time):
		self.time_elapsed += time

	def buy_farm(self, time_to_buy):
		self.cookie_rate += self.farm_rate
		self.add_time(time_to_buy)

	def buy_or_wait(self):
		time_to_buy = self.farm_cost / self.cookie_rate
		time_to_goal_if_wait = self.goal / self.cookie_rate

		time_to_goal_if_buy = time_to_buy + (self.goal / (self.cookie_rate + self.farm_rate))

		if time_to_goal_if_buy < time_to_goal_if_wait:
			self.buy_farm(time_to_buy)
		else:
			self.add_time(time_to_goal_if_wait)
			self.reached_goal = True

	def print_details(self):
		print "farm_cost:", self.farm_cost
		print "farm_rate:", self.farm_rate
		print "goal:", self.goal
		print "cookie_rate:", self.cookie_rate
		print "time_elapsed:", self.time_elapsed

def main():

	with open('B-large.in', 'rb') as f:
		reader = csv.reader(f, delimiter=' ')

		num_test_cases = int(reader.next()[0])

		for x in range(0, num_test_cases):
			row = map(float, reader.next())

			cookie_clker = CookieClicker(row[0], row[1], row[2])

			while not cookie_clker.reached_goal:
				cookie_clker.buy_or_wait()
				
			print "Case #" + str(x+1) + ": " + str(round(cookie_clker.time_elapsed, 7))


if __name__ == "__main__":
    main()