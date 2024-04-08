class Grid():
	def __init__(self, x_size, y_size, fill):
		self.grid = []
		for i in range(x_size):
			new_row = []
			for x in range(y_size):
				new_row.append(fill)
			self.grid.append(new_row)

	def set(self, x, y, new_value):
		self.grid[x][y] = new_value

	def get(self, x, y):
		return self.grid[x][y]

	def set_dimension_x(self, num, fill):
		if len(self.grid) <= num:
			for _ in range(num - len(self.grid)):
				self.grid.append(fill)
		else:
			self.grid[0:-(len(self.grid) - num)]

	def set_dimension_y(self, num, fill):
		if len(self.grid[0]) <= num:
			for i in range(len(self.grid)):
				for x in range(num - len(self.grid[0])):
					self.grid[i].append(fill)
		else:
			for i in range(len(self.grid)):
				self.grid[i][0:-(len(self.frid)[i] - num)]

	def get_dimensions(self):
		return {
			x: len(self.grid),
			y: len(self.grid[0])
		}