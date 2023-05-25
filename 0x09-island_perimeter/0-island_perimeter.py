#!/usr/bin/python3

'''
A function to find the perimeter of an island
'''


def island_perimeter(grid):
    '''
        finding the perimeter of an island in a grid
        arg: grid
        return: perimeter
    '''
    if 1 in grid[0] or 1 in grid[-1]:
        return None

    grid_dup = []
    for row in grid:
        if 1 in row:
            grid_dup.append(row)
            
    for i in range(len(grid_dup)):
        grid_dup[i] = grid_dup[i][1:-1]
    
    if len(grid_dup) != 0:
        grid_dup = sorted(grid_dup, reverse=True)
        length = len(grid_dup)
        g = [x for x in grid_dup[0] if x == 1]
        distance = len(g)
        return 2 * (length + distance)
        
    else: return 0
