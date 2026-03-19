import heapq

graph = {
    "Delhi": {"Agra": 233, "Jaipur": 280, "Lucknow": 555},
    "Agra": {"Delhi": 233, "Kanpur": 290},
    "Jaipur": {"Delhi": 280, "Udaipur": 395},
    "Lucknow": {"Delhi": 555, "Kanpur": 90},
    "Kanpur": {"Agra": 290, "Lucknow": 90},
    "Udaipur": {"Jaipur": 395}
}

def dijkstra(graph, start):
    distances = {city: float('inf') for city in graph}
    distances[start] = 0

    pq = [(0, start)]

    while pq:
        current_distance, current_city = heapq.heappop(pq)

        for neighbor, weight in graph[current_city].items():
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))

    return distances

start_city = "Delhi"
result = dijkstra(graph, start_city)

print("Shortest distances from", start_city)
for city, dist in result.items():
    print(city, ":", dist, "km")
