class Grid(object):
  count = 0

  def traverse(self, grid, m, n, path):
    x, y = path[-1]
    print("At %s, %s" % (x, y))
    if x + 1 < m and grid[x + 1][y] == 0:
      path.append((x + 1, y))
      self.traverse(grid, m, n, path)
      path.pop()
    if y + 1 < n and grid[x][y + 1] == 0:
      path.append((x, y + 1))
      self.traverse(grid, m, n, path)
      path.pop()
    if x + 1 == m and y + 1 == n:
      print('Reached')
      self.count += 1

  def count_paths(self, grid):
    """
    Count the unique paths in a grid, from upper left to bottom right.

    :param grid: The grid filled with 0s and 1s.
    :return: The number of unique paths.
    """
    if len(grid) == 0:
      return 0
    if grid[0][0] == 1:
      return 0

    m = len(grid)
    n = len(grid[0])
    path = [(0, 0)]
    self.traverse(grid, m, n, path)
    count = self.count
    self.count = 0
    return count

if __name__ == '__main__':
  test_grid_object = Grid()
  grid = [
    [0, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 1, 0, 0],
    [1, 0, 0, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 0, 0]
  ]
  count = test_grid_object.count_paths(grid)
  print(count)
