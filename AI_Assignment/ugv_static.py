import heapq
import random

SIZE = 10

def generate_grid(density):
    grid = [[0 for _ in range(SIZE)] for _ in range(SIZE)]
    for i in range(SIZE):
        for j in range(SIZE):
            if random.random() < density:
                grid[i][j] = 1
    return grid

def astar(grid, start, goal):
    def heuristic(a, b):
        return abs(a[0]-b[0]) + abs(a[1]-b[1])

    pq = []
    heapq.heappush(pq, (0, start))
    came_from = {}
    cost_so_far = {start: 0}

    while pq:
        _, current = heapq.heappop(pq)

        if current == goal:
            break

        for dx, dy in [(0,1),(1,0),(0,-1),(-1,0)]:
            next_node = (current[0]+dx, current[1]+dy)

            if 0 <= next_node[0] < SIZE and 0 <= next_node[1] < SIZE:
                if grid[next_node[0]][next_node[1]] == 1:
                    continue

                new_cost = cost_so_far[current] + 1

                if next_node not in cost_so_far or new_cost < cost_so_far[next_node]:
                    cost_so_far[next_node] = new_cost
                    priority = new_cost + heuristic(goal, next_node)
                    heapq.heappush(pq, (priority, next_node))
                    came_from[next_node] = current

    path = []
    node = goal
    while node in came_from:
        path.append(node)
        node = came_from[node]
    path.append(start)
    path.reverse()

    return path

grid = generate_grid(0.2)
start = (0, 0)
goal = (9, 9)

path = astar(grid, start, goal)

print("Path:", path)
print("Path length:", len(path))