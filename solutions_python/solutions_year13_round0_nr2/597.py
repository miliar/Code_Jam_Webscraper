import sys

class Pattern:
	pattern = []

	def __init__(self, width, height):
		self.width = width
		self.height = height
		self.pattern = [100] * width * height

	def set(self, x, y, value):
		self.pattern[x + y * self.width] = value

	def get(self, x, y):
		return self.pattern[x + y * self.width]

	def viable(self):
		if self.enclosed_squares():
			return False

		if self.enclosed_edge_squares():
			return False

		return True

	def enclosed_squares(self):
		for x in range(self.width):
			for y in range(self.height):
				val = self.get(x, y)

				horiz = False
				vert = False

				for i in range(self.width):
					if self.get(i, y) > val:
						horiz = True
						break

				for j in range(self.height):
					if self.get(x, j) > val:
						vert = True
						break

				if horiz and vert:
					return True

		return False

	def enclosed_edge_squares(self):
		return False

def convert_bool(b):
	if b:
		return 'YES'
	return 'NO'

def main():
	f = open(sys.argv[1], 'r')
	count = int(f.readline())
	for i in range(count):
		height, width = [int(x) for x in f.readline().split()]
		p = Pattern(width, height)

		for y in range(height):
			line = f.readline()
			values = [int(x) for x in line.split()]
			for x in range(width):
				p.set(x, y, values[x])

		print 'Case #' + str(i + 1) + ': ' + convert_bool(p.viable())

if __name__ == "__main__":
	main()