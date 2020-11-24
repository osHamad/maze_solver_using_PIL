class Node:
    def __init__(self, node, maze_size, pix, parent=None):
        self.position = node
        self.node_col, self.node_row = node
        self.maze_col, self.maze_row = maze_size
        self.pix = pix
        self.parent = parent
        self.neighbors = []

    def is_blocked(self, node):
        return self.pix[node] == (0, 0, 0, 255)  # RGBA code for black

    def in_range(self, node):
        col, row = node
        return self.maze_col - 1 >= col >= 0 and self.maze_row - 1 >= row >= 0

    def update_neighbors(self):
        # setting the positions of the neighbor nodes for each direction
        # since out line can move any direction we must include diagonal neighbors
        right = (self.node_col + 1, self.node_row)
        left = (self.node_col - 1, self.node_row)
        up = (self.node_col, self.node_row - 1)
        down = (self.node_col, self.node_row + 1)
        top_left = (self.node_col - 1, self.node_row - 1)
        top_right = (self.node_col + 1, self.node_row - 1)
        bottom_left = (self.node_col - 1, self.node_row + 1)
        bottom_right = (self.node_col + 1, self.node_row + 1)

        # looping through all possible neighbors
        # if the neighbor node is valid, it is appended to neighbors
        neighbors = [right, left, up, down, top_left, top_right, bottom_left, bottom_right]
        for node in neighbors:
            if self.in_range(node) and not self.is_blocked(node):
                self.neighbors.append(node)
