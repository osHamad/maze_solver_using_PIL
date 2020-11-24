from PIL import Image
from math import sqrt
from node import Node


# to find the f cost, we add the h cost and the g cost
# the g cost is the distance between the current and neighbor nodes
# the h cost is the distance between the neighbor and the destination nodes
# in this case, we are using Euclidean Distance
def f_cost(current, neighbor, end):
    g = sqrt((current[1] - neighbor[1]) ** 2 + (current[0] - neighbor[0]) ** 2)
    h = sqrt((end[1] - neighbor[1]) ** 2 + (end[0] - neighbor[0]) ** 2)

    return g + h


# each node in opened nodes is examined and the node with the lowest f cost is returned
def new_lowest(current_node, open_nodes, end_node):
    try:
        lowest = open_nodes[0]
    except IndexError:
        print('An error occurred. Your maze is likely unsolvable.')
        return

    for node in open_nodes:
        if f_cost(current_node, node, end_node) < f_cost(current_node, lowest, end_node):
            lowest = node
    return lowest


# this for loop will loop through every pixel and find the start and end
# the start is marked with green and the end is marked with red
def find_start_end(maze_size, pix):
    maze_col, maze_row = maze_size
    for col in range(maze_col):
        for row in range(maze_row):
            if pix[col, row] == (0, 255, 0, 255):  # RGBA code for green
                start = (col, row)
            elif pix[col, row] == (255, 0, 0, 255):  # RGBA code for red
                end = (col, row)

    try:
        return start, end

    except UnboundLocalError:
        print('No start and/or end detected\nCheck green and red color values')


# creates a visible path using the path library
# default color is blue
def create_path(path, end, maze, pix, color=(0, 0, 255, 255)):
    came_from = end
    while True:
        if came_from != 'start':
            pix[came_from] = color
            came_from = path[came_from]
        else:
            return maze.save('solution.png')


def main():
    print('Input your image\'s name including the file type (example.png)')
    print('Make sure image is in directory')
    image_name = input('Image Name: ')
    try:
        maze = Image.open(image_name)
    except FileNotFoundError:
        print(f'There is no file named \'{image_name}\' in directory')
        return

    pix = maze.load()

    try:
        start, end = find_start_end(maze.size, pix)
    except TypeError:
        return

    # the opened nodes are all the neighbors of the current node
    # opened nodes are to be examined for the node with the lowest f cost
    opened_nodes = [start]
    closed_nodes = []
    path = {start: 'start'}
    current = Node(start, maze.size, pix)

    while True:
        if current.position == end:
            return create_path(path, end, maze, pix)

        # the current node is updated and is set to the node with the lowest f cost
        lowest_node = new_lowest(current.position, opened_nodes, end)
        try:
            current = Node(lowest_node, maze.size, pix, current.position)
        except TypeError:
            return

        # the nodes with the lowest f cost are appended to closed nodes
        if current.position not in closed_nodes:
            opened_nodes.remove(current.position)
            closed_nodes.append(current.position)

        # the neighbors of the current node are updated and appended to opened nodes
        # each neighbor and its parent is added to a dictionary
        current.update_neighbors()
        for node in current.neighbors:
            if node not in opened_nodes and node not in closed_nodes:
                opened_nodes.append(node)
                path[node] = current.position


if __name__ == '__main__':
    main()
