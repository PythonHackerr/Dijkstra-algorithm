import argparse

INIT_ROAD_COST = -1

class Node:
    def __init__(self, i, j, cost):
        self.i = i
        self.j = j
        self.cost = cost
        self.connected_with = []
        self.road_cost = INIT_ROAD_COST
        self.road = []
        self.is_visited = False

    def __str__(self):
        return str(self.cost)

def get_file_content(file_name):
    try:
        with open(file_name, 'r', encoding='utf8') as fh:
            nodes_arr = [
                    [Node(i, j, int(dig)) for j, dig in enumerate(line) if dig.isdigit()]
                    for i, line in enumerate(fh.readlines())
                ]
            for i, sub_arr in enumerate(nodes_arr):
                for j, node in enumerate(sub_arr):
                    if i - 1 >= 0:
                        node.connected_with.append(nodes_arr[i - 1][j])
                    if i + 1 < len(nodes_arr):
                        node.connected_with.append(nodes_arr[i + 1][j])
                    if j - 1 >= 0:
                        node.connected_with.append(nodes_arr[i][j - 1])
                    if j + 1 < len(sub_arr):
                        node.connected_with.append(nodes_arr[i][j + 1])
            return nodes_arr
    except Exception as e:
        print(e)
        return []

def dijkstra(node):
    while node is not None:
        min_i = None
        for i in node.connected_with:
            if i.is_visited:
                continue
            tmp = node.road_cost + i.cost
            if i.road_cost == INIT_ROAD_COST or i.road_cost > tmp:
                i.road_cost = tmp
                i.road = node.road.copy()
                i.road.append(i)
            if min_i is None or (min_i.road_cost > i.road_cost):
                min_i = i
        node.is_visited = True
        node = min_i

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('file')
    args = parser.parse_args()
    nodes = get_file_content(args.file)
    zeros = []
    for sub_arr in nodes:
        for i in sub_arr:
            if i.cost == 0:
                zeros.append(i)
    if not len(zeros) == 2:
        raise Exception('Start and end points specified uncorrectly')
    start, end = zeros
    start.road_cost = 0
    start.road.append(start)
    dijkstra(start)

    for sub_arr in nodes:
        line = ''
        for el in sub_arr:
            line += str(el) if el in end.road else ' '
        print(line)

#command
#python main.py filename
if __name__ == "__main__":
    main()
