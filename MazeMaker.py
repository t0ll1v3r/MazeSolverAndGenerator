import random
from collections import deque

def MazeMaker(n, filename="mazeCustom.txt"):
    # initialize maze with 0's (walls)
    maze = [[0 for _ in range(n)] for _ in range(n)]
    
    # carve out random paths starting from (0, 0)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    visited = [[False] * n for _ in range(n)]
    stack = [(0, 0)]
    visited[0][0] = True
    maze[0][0] = 1

    while stack:
        x, y = stack[-1]
        valid_neighbors = []
        for dx, dy in directions:
            new_x, new_y = x + dx, y + dy
            if 0 <= new_x < n and 0 <= new_y < n and not visited[new_x][new_y]:
                # checks that there are at least two cells between visited cells to create a true path
                if sum(0 <= new_x + ddx < n and 0 <= new_y + ddy < n and visited[new_x + ddx][new_y + ddy] for ddx, ddy in directions) <= 1:
                    valid_neighbors.append((new_x, new_y))

        if valid_neighbors:
            new_x, new_y = random.choice(valid_neighbors)
            visited[new_x][new_y] = True
            maze[new_x][new_y] = 1
            stack.append((new_x, new_y))
        else:
            stack.pop()

    # ensure start and end are set
    maze[0][0] = 1
    maze[n-1][n-1] = 1

    # write the valid maze to file
    with open(filename, "w") as f:
        for row in maze:
            f.write("".join(map(str, row)) + "\n")

if __name__ == "__main__":
    n = 100  # size of maze
    MazeMaker(n)
    print(f"A {n}x{n} maze has been generated and saved to 'mazeCustom.txt'.")

"""
 ______________$$$$$$$$$$____________________
 _____________$$__$_____$$$$$________________
 _____________$$_$$__$$____$$$$$$$$__________
 ____________$$_$$__$$$$$________$$$_________
 ___________$$_$$__$$__$$_$$$__$$__$$________
 ___________$$_$$__$__$$__$$$$$$$$__$$_______
 ____________$$$$$_$$_$$$_$$$$$$$$_$$$_______
 _____________$$$$$$$$$$$$$_$$___$_$$$$______
 ________________$$_$$$______$$$$$_$$$$______
 _________________$$$$_______$$$$$___$$$_____
 ___________________________$$_$$____$$$$____
 ___________________________$$_$$____$$$$$___
 __________________________$$$$$_____$$$$$$__
 _________________________$__$$_______$$$$$__
 ________________________$$$_$$________$$$$$_
 ________________________$$$___________$$$$$_
 _________________$$$$___$$____________$$$$$$
 __$$$$$$$$____$$$$$$$$$$_$____________$$$_$$
 _$$$$$$$$$$$$$$$______$$$$$$$___$$____$$_$$$
 $$________$$$$__________$_$$$___$$$_____$$$$
 $$______$$$_____________$$$$$$$$$$$$$$$$$_$$
 $$______$$_______________$$_$$$$$$$$$$$$$$$_
 $$_____$_$$$$$__________$$$_$$$$$$$$$$$$$$$_
 $$___$$$__$$$$$$$$$$$$$$$$$__$$$$$$$$$$$$$__
 $$_$$$$_____$$$$$$$$$$$$________$$$$$$__$___
 $$$$$$$$$$$$$$_________$$$$$______$$$$$$$___
 $$$$_$$$$$______________$$$$$$$$$$$$$$$$____
 $$__$$$$_____$$___________$$$$$$$$$$$$$_____
 $$_$$$$$$$$$$$$____________$$$$$$$$$$_______
 $$_$$$$$$$hg$$$____$$$$$$$$__$$$____________
 $$$$__$$$$$$$$$$$$$$$$$$$$$$$$______________
 $$_________$$$$$$$$$$$$$$$__________________
"""
