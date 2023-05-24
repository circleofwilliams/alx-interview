def island_perimeter(grid):
	'''
		Finding the perimeter of the land area in an island.
		arg: grid
		return: the perimeter
	'''
	grid = grid[1 : -1]
  for i in range(len(grid)):
		grid[i] = grid[i][1 : -1]
	grid = sorted(grid, reverse=True)
  length = len(grid)

	g = [x for x in grid[0] if x == 1]
	distance = len(g)

	return 2 * (length + distance)
