import unittest
from astar_maze import astar_search  # Import the A* function from main script

class TestAStarSearch(unittest.TestCase):

    def setUp(self):
        """Set up a sample maze (10x10 for simplicity)."""
        self.maze = [
            [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
            [0, 1, 0, 1, 0, 1, 1, 1, 0, 0],
            [0, 1, 0, 1, 0, 1, 0, 0, 0, 1],
            [0, 0, 0, 0, 0, 1, 0, 1, 1, 0],
            [1, 1, 1, 1, 0, 1, 0, 0, 0, 0],
            [0, 0, 0, 1, 0, 0, 0, 1, 1, 0],
            [0, 1, 0, 1, 1, 1, 0, 1, 0, 0],
            [0, 1, 0, 0, 0, 1, 0, 1, 0, 1],
            [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
            [1, 1, 0, 1, 1, 1, 1, 1, 0, 0]
        ]

    def test_path_exists(self):
        """Test if a valid path exists"""
        start, end = (0, 0), (2, 2)
        self.assertEqual(astar_search(self.maze, start, end), "YES")

    def test_no_path_exists(self):
        """Test when no path exists due to obstacles"""
        start, end = (1, 2), (7, 9)  # Blocked by walls
        self.assertEqual(astar_search(self.maze, start, end), "NO")

    def test_same_start_end(self):
        """Test when start and end points are the same"""
        start, end = (4, 4), (4, 4)
        self.assertEqual(astar_search(self.maze, start, end), "YES")

    def test_start_or_end_in_wall(self):
        """Test when the start or end point is inside a wall"""
        start, end = (4, 0), (9, 9)  # Start is inside a wall
        self.assertEqual(astar_search(self.maze, start, end), "NO")

    def test_large_maze(self):
        """Test performance with a larger 81x81 open maze (no walls)"""
        large_maze = [[0] * 81 for _ in range(81)]  # No obstacles
        start, end = (0, 0), (80, 80)
        self.assertEqual(astar_search(large_maze, start, end), "YES")

if __name__ == '__main__':
    unittest.main()
