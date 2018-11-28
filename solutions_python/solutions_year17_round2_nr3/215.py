import matplotlib.pyplot as plt
import networkx as nx

with open("C-small-attempt0.in", "r") as inp:
    with open("C-small-attempt0.out", "w") as outp:
        cases = int(inp.readline())
        for i in range(cases):
            cities, stops = [int(x) for x in inp.readline().split()]
            horse_dist = []
            horse_speed = []
            dist_next = []
            for j in range(cities):
                dist, speed = [int(x) for x in inp.readline().split()]
                horse_dist.append(dist)
                horse_speed.append(speed)
            for j in range(cities):
                dest_graph = inp.readline().split()
                if j < cities-1:
                    dist_next.append(int(dest_graph[j+1]))
            origin, dest = [int(x) for x in inp.readline().split()]

            horse_max_city = []
            for j in range(len(horse_dist)-1):
                k = j
                curr_dist = horse_dist[j]
                while k < cities-1 and curr_dist >= dist_next[k]:
                    curr_dist -= dist_next[k]
                    k += 1
                horse_max_city.append(k)

            city_map = nx.Graph()
            for j in range(len(horse_max_city)):
                acc_time = 0
                for k in range(j, horse_max_city[j]):
                    acc_time += dist_next[k] / horse_speed[j]
                    city_map.add_edge(j, k+1, distance=acc_time)
            shortest_dist = nx.dijkstra_path_length(city_map, 0, cities-1, 'distance')
            outp.write("Case #" + str(i+1) + ": " + str(shortest_dist) + "\n")
