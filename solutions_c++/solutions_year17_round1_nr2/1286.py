//
//  main.cpp
//  Ratatouille
//
//  Created by Rugen Heidbuchel on 15/04/2017.
//  Copyright © 2017 Rugen Heidbuchel. All rights reserved.
//

#include <iostream>
#include <vector>
#include <string>
#include <set>
#include <map>
#include <cmath>

// Shortcuts for "common" data types in contests
typedef long long ll;
typedef std::vector<int> vi;
typedef std::pair<int, int> ii;
typedef std::vector<ii> vii;
typedef std::set<int> si;
typedef std::map<std::string, int> msi;

// To simplify repetitions/loops, Note: define your loop style and stick with it!
#define REP(i, a, b) \
for (int i = int(a); i <= int(b); i++) // a to b, and variable i is local!
#define TRvi(c, it) \
for (vi::iterator it = (c).begin(); it != (c).end(); it++)
#define TRvii(c, it) \
for (vii::iterator it = (c).begin(); it != (c).end(); it++)
#define TRmsi(c, it) \
for (msi::iterator it = (c).begin(); it != (c).end(); it++)
#define INF 2000000000 // 2 billion

// If you need to recall how to use memset:
#define MEMSET_INF 127 // about 2B
#define MEMSET_HALF_INF 63 // about 1B
//memset(dist, MEMSET_INF, sizeof dist); // useful to initialize shortest path distances
//memset(dp_memo, -1, sizeof dp_memo); // useful to initialize DP memoization table
//memset(arr, 0, sizeof arr); // useful to clear array of integers

#ifndef MAXFLOW
#define MAXFLOW

/**
 This file contains functions to calculate the maximum flow in a graph using Ford-Fulkerson.
 It uses the Edmonds-Karp implementation.
 Since there will be negative flows in the graph during the calculation, we advise to use
 integer types. However, the algorithm itself will work with non-integer types like size_t
 as well, because 0 - 18446744073709551615 == -1. :) Quite cool... :p
 
 The adjacency list here is a vector containing maps to map a node number to an edge.
 This is because we need to be able to efficiently find the inverse edge.
 */

#include <vector>
#include <map>
#include <queue>

template <class T>
struct Edge {
    T capacity, flow = T();
    
    Edge() {}
    
    Edge(T cap) {
        capacity = cap;
    }
    
    T residualCapacity() {
        return capacity - flow;
    }
};

template <class T>
using AdjacencyList = std::vector<std::map<size_t, Edge<T>>>;

template <class T>
/**
 Adds an edge to the given graph. This method is handy if you don't want to add
 inverse edges manually.
 
 @param graph The graph to add the edge to.
 @param from The node the edge comes from.
 @param to The node the edge goes to.
 @param capacity The capacity of the edge.
 @param reverseCapacity The capacity of the reversed edge, defaults to zero.
 */
void addEdge(AdjacencyList<T> &graph, size_t from, size_t to, T capacity, T reverseCapacity = T()) {
    Edge<T> edge = {capacity};
    Edge<T> reverse = {reverseCapacity};
    graph[from][to] = edge;
    graph[to][from] = reverse;
}

template <class T>
/**
 Calculates the maximum flow in the given graph using the Ford-Fulkerson algorithm.
 It uses the Edmonds-Karp implementation (using breadth-first search to find paths).
 
 @param graph The graph to calculate the flow in. This will contain the flows when the
 algorithm is finished.
 @param source The source node.
 @param sink The sink node.
 @return The maximum total flow through the network.
 */
T fordFulkerson(AdjacencyList<T> &graph, size_t source, size_t sink) {
    T maxFlow = T();
    std::vector<Edge<T>> path(graph.size());
    while (true) {
        
        // Find path breadth first
        std::vector<size_t> P(graph.size(), graph.size());
        std::vector<T> M(graph.size(), T());
        M[source] = std::numeric_limits<T>::max();
        std::queue<size_t> Q;
        Q.push(source);
        while (!Q.empty()) {
            size_t node = Q.front(); Q.pop();
            for (std::pair<size_t, Edge<T>> entry: graph[node]) {
                size_t to = entry.first;
                Edge<T> &edge = entry.second;
                if (edge.residualCapacity() > 0 && P[to] == graph.size()) {
                    P[to] = node;
                    M[to] = std::min(M[node], edge.residualCapacity());
                    if (to != sink) {
                        Q.push(to);
                    } else {
                        std::queue<size_t>().swap(Q);
                        break;
                    }
                }
            }
        }
        
        // Check whether we found one
        T maxPathFlow = M[sink];
        if (maxPathFlow == T()) break;
        
        // Adjust flows
        maxFlow += maxPathFlow;
        size_t node = sink;
        while (node != source) {
            size_t parent = P[node];
            graph[parent][node].flow += maxPathFlow;
            graph[node][parent].flow -= maxPathFlow;
            node = parent;
        }
    }
    return maxFlow;
}

#endif


#pragma mark - MAIN

size_t T;
int N, P;

int lowestNumber(int amount, int recipeAmount) {
    return (int)std::ceil((double)amount / (1.1 * (double)recipeAmount));
}

int highestNumber(int amount, int recipeAmount) {
    return (int)((double)amount / (0.9 * (double)recipeAmount));
}

int main(int argc, const char * argv[]) {

    #ifdef USE_INPUT_FILE
    freopen("example_input.txt", "r", stdin);
    #endif
    
    std::cin >> T;
    for (size_t caseNumber = 0; caseNumber < T; caseNumber++) {
        
        std::cout << "Case #" << caseNumber + 1 << ": ";
        
        std::cin >> N >> P;
        std::vector<int> recipe(N);
        std::vector<std::vector<int>> packages(N, std::vector<int>(P));
        
        for (size_t i = 0; i < N; i++) {
            std::cin >> recipe[i];
        }
        
        for (size_t i = 0; i < N; i++) {
            for (size_t j = 0; j < P; j++) {
                std::cin >> packages[i][j];
            }
        }
        
        AdjacencyList<int> graph(N*P*2 + 2);
        
        for (size_t i = 0; i < P; i++) {
            addEdge(graph, N*P*2, 2*i, 1);
            addEdge(graph, (N-1)*P*2 + 2*i + 1, N*P*2+1, 1);
        }
        
        for (size_t i = 0; i < N; i++) {
            for (size_t j = 0; j < P; j++) {
                int x = packages[i][j], tx = recipe[i];
                int lx = lowestNumber(x, tx), hx = highestNumber(x, tx);
                if (hx >= lx) {
                    addEdge(graph, i*P*2 + 2*j, i*P*2 + 2*j + 1, 1);
                }
            }
        }
        
        for (size_t i = 0; i < N-1; i++) {
            for (size_t j = 0; j < P; j++) {
                int x = packages[i][j], tx = recipe[i], ty = recipe[i+1];
                int lx = lowestNumber(x, tx), hx = highestNumber(x, tx);
                if (hx < lx) continue;
                for (size_t k = 0; k < P; k++) {
                    int y = packages[i+1][k];
                    int ly = lowestNumber(y, ty), hy = highestNumber(y, ty);
                    if (hy < ly) continue;
                    if (lx <= hy && ly <= hx) {
                        addEdge(graph, i*P*2 + 2*j + 1, (i+1)*P*2 + 2*k, 1);
                    }
                }
            }
        }
        
        std::cout << fordFulkerson(graph, N*P*2, N*P*2+1) << "\n";
    }
    
    return 0;
}
