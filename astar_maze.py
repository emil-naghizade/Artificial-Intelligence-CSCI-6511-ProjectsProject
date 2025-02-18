import heapq
import sys

# Function to read the maze file
def read_maze(file_path):
    with open(file_path, 'r') as f:
        return [list(map(int, line.strip().split())) for line in f]

# A* Search Algorithm
def astar_search(maze, start, end):
    rows, cols = len(maze), len(maze[0])
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Up, Down, Left, Right

    def heuristic(a, b):
        """Manhattan distance heuristic"""
        return abs(a[0] - b[0]) + abs(a[1] - b[1])

    # **Check if start or end points are walls**
    if maze[start[0]][start[1]] == 1 or maze[end[0]][end[1]] == 1:
        return "NO"

    # Priority queue: stores (f-score, g-score, (row, col))
    pq = [(heuristic(start, end), 0, start)]
    visited = set()
    g_score = {start: 0}

    while pq:
        _, cost, (r, c) = heapq.heappop(pq)

        if (r, c) == end:
            return "YES"

        if (r, c) in visited:
            continue
        visited.add((r, c))

        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and maze[nr][nc] == 0:
                new_cost = cost + 1
                if (nr, nc) not in g_score or new_cost < g_score[(nr, nc)]:
                    g_score[(nr, nc)] = new_cost
                    priority = new_cost + heuristic((nr, nc), end)
                    heapq.heappush(pq, (priority, new_cost, (nr, nc)))

    return "NO"


# Example usage
if __name__ == "__main__":
    if len(sys.argv) != 6:
        print("Usage: python astar.py <maze_file> <start_x> <start_y> <end_x> <end_y>")
        sys.exit(1)

    maze_file = sys.argv[1]  # Get maze file path from command line
    start = (int(sys.argv[2]), int(sys.argv[3]))  # Get start coordinates
    end = (int(sys.argv[4]), int(sys.argv[5]))  # Get end coordinates

    maze = read_maze(maze_file)
    result = astar_search(maze, start, end)
    print(result)
