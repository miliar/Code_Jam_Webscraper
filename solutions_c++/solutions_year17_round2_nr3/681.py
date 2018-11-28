#include <bits/stdc++.h>

#define MAX 101

using namespace std;

struct node{
    int index; 
    double cost;
    int horse, km;
};

int speed_horses[MAX], km_horses[MAX];
double dist[MAX][MAX];

struct graph{
    node nodes[MAX];
    int size;
};

void init(graph &g, int v){
    g.size = v;
    for (int i = 0; i < v; i++){
        g.nodes[i].index = i;
        g.nodes[i].cost = 0;
        g.nodes[i].horse = -1;
    }
}

bool operator<(const node &a, const node &b){
    if (a.cost == b.cost)
        return a.index < b.index;
    return a.cost < b.cost;
}

double dijkstra(graph &g, int a, int b = -1){
    set<node> q;
    vector< vector<bool> > mark(g.size, vector<bool>(g.size, false));
    g.nodes[a].horse = a;
    g.nodes[a].km = km_horses[a];
    q.insert(g.nodes[a]);
    while (!q.empty()){
        node actual = *q.begin();
        q.erase(q.begin());

        if (mark[actual.index][actual.horse]) continue;
        mark[actual.index][actual.horse] = true;

        if (actual.index == b)
            return actual.cost;

        for (int i = 0; i < g.size; i++){
            node tmp = g.nodes[i];
            if (dist[actual.index][tmp.index] == -1) continue;
            node aux = actual;
            aux.horse = aux.index;
            aux.km = km_horses[aux.index];
                if (!mark[tmp.index][actual.horse] && dist[actual.index][tmp.index] <= actual.km){
                    tmp.cost = actual.cost + dist[actual.index][tmp.index] / speed_horses[actual.horse];
                    tmp.horse = actual.horse;
                    tmp.km = actual.km - dist[actual.index][tmp.index];
                    q.insert(tmp);
                }
                if (!mark[tmp.index][aux.horse] && dist[actual.index][tmp.index] <= aux.km){
                    tmp.cost = actual.cost + dist[actual.index][tmp.index] / speed_horses[aux.horse];
                    tmp.horse = aux.horse;
                    tmp.km = aux.km - dist[actual.index][tmp.index];
                    q.insert(tmp);
                }
        }
    }
    return -1;
}

graph g;

int main(){
    int t, cases = 1;
    cout.precision(12);
    cin >> t;
    while (t--){
        int n, q;
        cin >> n >> q;

        init(g, n);

        for (int i = 0; i < n; i++){
            cin >> km_horses[i] >> speed_horses[i];
        }
        for (int i = 0; i < n; i++)
            for (int j = 0; j < n; j++)
                cin >> dist[i][j];

        cout << "Case #" << cases++ << ":";

        for (int i = 0; i < q; i++){
            int a, b;
            cin >> a >> b;
            cout << " " << dijkstra(g, a-1, b-1);
        }
        cout << endl;
    }
    return 0;
}
