import heapq
import sys

def get_file_content(file_path):
    lines = []
    with open(file_path) as f:
        for line in f:
            lines.append(line.rstrip())
    return lines

def get_zeros(tab):
    zeros = []
    height = len(tab)
    width = len(tab[0])
    for i in range(height):
        for j in range(width):
            if tab[i][j] == '0':
                zeros.append((j,i))
    return zeros

def get_neighbors(point, board, visited):
    x, y = point
    neighbors = []
    if not (x + 1, y) in visited and (x + 1 < len(board[0])):
        neighbors.append((x + 1, y))
    if not (x - 1, y) in visited and (x - 1 >= 0):
        neighbors.append((x - 1, y))
    if not (x, y + 1) in visited and (y + 1 < len(board)):
        neighbors.append((x, y + 1))
    if not (x, y - 1) in visited and (y - 1 >= 0):
        neighbors.append((x, y - 1))
    return neighbors

def main():
    lines = get_file_content(sys.argv[1])
    zeros = get_zeros(lines)
    if len(zeros) != 2:
        print('ERROR: invalid file content')
        return
    root, end = zeros
    queue = [(0, root)]
    distances = {root: 0}
    visited = []
    prev = {}
    while queue:
        el = heapq.heappop(queue)[1]
        if (el == end):
            break
        visited.append(el)
        neighbors = get_neighbors(el, lines, visited)
        for n in neighbors:
            value = (int(lines[n[1]][n[0]]))
            new_dist = distances[el] + value
            if n not in distances.keys():
                distances[n] = new_dist
                prev[n] = el
                heapq.heappush(queue, (distances[n], n))
            elif distances[n] > new_dist:
                distances[n] = new_dist
                prev[n] = el

    path = [end]
    current = end
    while (current != root):
        current = prev[current]
        path.append(current)

    for y in range(len(lines)):
        line = ''
        for x in range(len(lines[0])):
            line += lines[y][x] if (x, y) in path else ' '
        print(line)

if __name__ == "__main__":
    main()
