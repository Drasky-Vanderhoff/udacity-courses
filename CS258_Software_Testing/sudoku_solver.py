# SPECIFICATION:
#
# check_sudoku() determines whether its argument is a valid Sudoku
# grid. It can handle grids that are completely filled in, and also
# grids that hold some empty cells where the player has not yet
# written numbers.
#
# First, your code must do some sanity checking to make sure that its
# argument:
#
# - is a 9x9 list of lists
#
# - contains, in each of its 81 elements, a number in the range 0..9
#
# If either of these properties does not hold, check_sudoku must
# return None.
#
# If the sanity checks pass, your code should return True if all of
# the following hold, and False otherwise:
#
# - each number in the range 1..9 occurs only once in each row
#
# - each number in the range 1..9 occurs only once in each column
#
# - each number the range 1..9 occurs only once in each of the nine
#   3x3 sub-grids, or "boxe[ i for i in c if i == 0]s", that make up the board
#
# This diagram (which depicts a valid Sudoku grid) illustrates how the
# grid is divided into sub-grids:
#
# 5 3 4 | 6 7 8 | 9 1 2
# 6 7 2 | 1 9 5 | 3 4 8
# 1 9 8 | 3 4 2 | 5 6 7
# ---------------------
# 8 5 9 | 7 6 1 | 4 2 3
# 4 2 6 | 8 5 3 | 7 9 1
# 7 1 3 | 9 2 4 | 8 5 6
# ---------------------
# 9 6 1 | 5 3 7 | 0 0 0
# 2 8 7 | 4 1 9 | 0 0 0
# 3 4 5 | 2 8 6 | 0 0 0
#
# Please keep in mind that a valid grid (i.e., one for which your
# function returns True) may contain 0 multiple times in a row,
# column, or sub-grid. Here we are using 0 to represent an element of
# the Sudoku grid that the player has not yet filled in.

# check_sudoku should return None
ill_formed = [[5,3,4,6,7,8,9,1,2],
              [6,7,2,1,9,5,3,4,8],
              [1,9,8,3,4,2,5,6,7],
              [8,5,9,7,6,1,4,2,3],
              [4,2,6,8,5,3,7,9],  # <---
              [7,1,3,9,2,4,8,5,6],
              [9,6,1,5,3,7,2,8,4],
              [2,8,7,4,1,9,6,3,5],
              [3,4,5,2,8,6,1,7,9]]

# check_sudoku should return True
valid = [[5,3,4,6,7,8,9,1,2],
         [6,7,2,1,9,5,3,4,8],
         [1,9,8,3,4,2,5,6,7],
         [8,5,9,7,6,1,4,2,3],
         [4,2,6,8,5,3,7,9,1],
         [7,1,3,9,2,4,8,5,6],
         [9,6,1,5,3,7,2,8,4],
         [2,8,7,4,1,9,6,3,5],
         [3,4,5,2,8,6,1,7,9]]

# check_sudoku should return False
invalid = [[5,3,4,6,7,8,9,1,2],
           [6,7,2,1,9,5,3,4,8],
           [1,9,8,3,8,2,5,6,7],
           [8,5,9,7,6,1,4,2,3],
           [4,2,6,8,5,3,7,9,1],
           [7,1,3,9,2,4,8,5,6],
           [9,6,1,5,3,7,2,8,4],
           [2,8,7,4,1,9,6,3,5],
           [3,4,5,2,8,6,1,7,9]]

# check_sudoku should return True
easy = [[2,9,0,0,0,0,0,7,0],
        [3,0,6,0,0,8,4,0,0],
        [8,0,0,0,4,0,0,0,2],
        [0,2,0,0,3,1,0,0,7],
        [0,0,0,0,8,0,0,0,0],
        [1,0,0,9,5,0,0,6,0],
        [7,0,0,0,9,0,0,0,1],
        [0,0,1,2,0,0,3,0,6],
        [0,3,0,0,0,0,0,5,9]]

# check_sudoku should return True
hard = [[1,0,0,0,0,7,0,9,0],
        [0,3,0,0,2,0,0,0,8],
        [0,0,9,6,0,0,5,0,0],
        [0,0,5,3,0,0,9,0,0],
        [0,1,0,0,8,0,0,0,2],
        [6,0,0,0,0,4,0,0,0],
        [3,0,0,0,0,0,0,1,0],
        [0,4,0,0,0,0,0,0,7],
        [0,0,7,0,0,0,3,0,0]]

#
# GPL LICENSE
# -----------
#
# Copyright 2012 Alejandro Kondrasky <drasky.vanderhoff@gmail.com>
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
# MA 02110-1301, USA.
#


def valid_range(l):
    val_elems = set(range(1, 10))
    l_clean = [e for e in l if e != 0]
    return len(l_clean) == len(list(set(l_clean).intersection(val_elems)))


def check_sudoku(grid):
    if  type(grid) != list or False in [list == type(r) for r in grid] or\
        [[int] * 9] * 9 != [map(type, r) for r in grid] or\
        False in [set(range(10)).issuperset(set(r)) for r in grid]:
        return None  # Ill Formed
    sub_grids = dict((i, []) for i in range(9))
    for i in range(9):
        for h in [3, 6, 9]:  # Generate sub_grids
            if i in range(h - 3, h):
                sub_grids[h - 3].extend(grid[i][:3])
                sub_grids[h - 2].extend(grid[i][3:6])
                sub_grids[h - 1].extend(grid[i][6:9])
    g = grid + map(list, zip(*grid)) + sub_grids.values()
    return False if False in map(valid_range, g) else True


def update_sets(l):
    elems = set(range(1, 10)).difference(set(l))
    for i in range(9):
        if type(l[i]) == set:
            l[i] = l[i].pop() if len(l[i]) == 1 else l[i].intersection(elems)
        elif type(l[i]) == int:
            l[i] = elems if l[i] == 0 else elems.discard(l[i])
        else:  # pragma: no cover
            assert False
    return l


def solve_sudoku(grid):
    if not check_sudoku(grid):
        return False, grid
    rotated = False
    for i in range(9):
        grid[i] = update_sets(grid[i])
    print grid
    while set in [type(e) for r in grid for e in r]:
        print "bla"
        for i in range(9):
            grid[i] = update_sets(grid[i])  # Generate sets and results per row
        grid, rotated = map(list, zip(*grid)), not rotated
        print grid
    if rotated:
        grid = map(list, zip(*grid))
    return (True, grid) if check_sudoku(grid) else (False, grid)


#print solve_sudoku(ill_formed) # --> False
print solve_sudoku(valid)      # --> True
#print solve_sudoku(invalid)    # --> False
#print solve_sudoku(easy)       # --> True
#print solve_sudoku(hard)       # --> True

