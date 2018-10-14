def main():
	cases = int(input())
	for i in range(cases):
		bricks = int(input())
		naomi_blocks = list(map(float, input().split()))
		naomi_blocks_copy = naomi_blocks[:]
		ken_blocks = list(map(float, input().split()))
		ken_blocks_copy = ken_blocks[:]
		ken1 = Ken(ken_blocks)
		naomi1 = Naomi(naomi_blocks, "good", ken1)
		ken2 = Ken(ken_blocks_copy)
		naomi2 = Naomi(naomi_blocks_copy, "bad")
		first_game = simulate(naomi1, ken1)
		second_game = simulate(naomi2, ken2)
		print("Case #%d: %d %d" % (i+1, first_game, second_game))

def play(naomi, ken):
	naomi_brick = naomi.play()
	ken_brick = ken.play(naomi_brick)
	if naomi_brick > ken_brick:
		naomi.score += 1
	else:
		ken.score += 1

def simulate(naomi, ken):
	while ken.bricks and naomi.bricks:
			play(naomi, ken)
	return naomi.score


class Ken:
	def __init__(self, bricks):
		self.bricks = bricks
		self.score = 0

	def play(self, played_by_other):
		min_best_brick = 1.1
		for brick in self.bricks:
			if brick > played_by_other:
				if brick < min_best_brick:
					min_best_brick = brick
		if min_best_brick == 1.1:
			min_best_brick = min(self.bricks)

		self.bricks.remove(min_best_brick)
		return min_best_brick

		

class Naomi:
	def __init__(self, bricks, playstyle, ken = None):
		self.bricks = bricks
		if playstyle == "bad":
			self.play = self.bad
		else:
			self.play= self.good
		self.ken = ken
		self.score = 0

	def bad(self):
		max_to_return = max(self.bricks)
		self.bricks.remove(max_to_return)
		return max_to_return

	def good(self):
		to_beat = min(self.ken.bricks)
		current_winner = 1.1
		for brick in self.bricks:
			if brick > to_beat:
				if brick < current_winner:
					current_winner = brick

		if current_winner != 1.1:
			self.bricks.remove(current_winner)
			to_return = max(self.ken.bricks) + .00000001


		else:
			to_return = max(self.ken.bricks) - .00000001
			self.bricks.remove(min(self.bricks))

		return to_return

main()

