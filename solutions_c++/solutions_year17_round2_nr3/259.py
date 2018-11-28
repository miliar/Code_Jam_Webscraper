#include<iostream>
#include<algorithm>
#include<cstdio>
#include<cstring>
const int CITY = 105;
const int QUERY = 105;
const long long INF = 1LL << 60;
using namespace std;


class Horse {
public:
    int energy;
    int speed;
    Horse(){}
    Horse(int energy, int speed): energy(energy), speed(speed) {}
};


class Query {
public:
    int bgn;
    int end;
    Query(){}
    Query(int bgn, int end): bgn(bgn), end(end) {}
};


int nCity, nQuery;
Horse horse[CITY];
long long adj[CITY][CITY];
Query query[QUERY];

void read() {
    memset(adj, -1, sizeof(adj));
    
    cin >> nCity >> nQuery;
    
    for (int i = 0; i < nCity; ++i) {
        cin >> horse[i].energy >> horse[i].speed;
    }

    for (int i = 0; i < nCity; ++i) {
        for (int j = 0; j < nCity; ++j) {
            cin >> adj[i][j];
        }
    }

    for (int i = 0; i < nQuery; ++i) {
        cin >> query[i].bgn >> query[i].end;
        --query[i].bgn;
        --query[i].end;
    }
}


double dijkstra(int bgn, int end) {
    double cost[CITY];
    bool visited[CITY];
    
    for (int i = 0; i < nCity; ++i) {
        cost[i] = INF;
        visited[i] = false;
    }
    cost[bgn] = 0;

    for (int loop = 0; loop < nCity; ++loop) {
        int minCity = -1;
        double minV = INF;

        for (int i = 0; i < nCity; ++i) {
            if (!visited[i] && minV > cost[i]) {
                minCity = i;
                minV = cost[i];
            }
        }

        if (minCity == -1) break;
        visited[minCity] = true;
        
        for (int i = 0; i < nCity; ++i) {
            if (adj[minCity][i] == -1) continue;
            if (adj[minCity][i] > horse[minCity].energy) continue;
            double toAdd = 1.0 * adj[minCity][i] / horse[minCity].speed;
            cost[i] = min(cost[i], cost[minCity] + toAdd);
        }
    }
    
    return cost[end];
}

void work(int cases) {
    // warshall-floyd
    for (int i = 0; i < nCity; ++i)
        adj[i][i] = 0;
    
    for (int k = 0; k < nCity; ++k)
        for (int i = 0; i < nCity; ++i)
            for (int j = 0; j < nCity; ++j)
                if (adj[i][k] != -1 && adj[k][j] != -1) {
                    if (adj[i][j] == -1 || adj[i][j] > adj[i][k] + adj[k][j])
                        adj[i][j] = adj[i][k] + adj[k][j];
                }
    
    printf("Case #%d:", cases);
    for (int i = 0; i < nQuery; ++i) {
        printf(" %.10lf", dijkstra(query[i].bgn, query[i].end));
    }
    printf("\n");
}


int main() {
    int cases;
    cin >> cases;
    
    for (int i = 0; i < cases; ++i) {
        read();
        work(i + 1);
    }
    return 0;
}
