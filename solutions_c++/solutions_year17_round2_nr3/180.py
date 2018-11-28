#include <bits/stdc++.h>
using namespace std;
using ld = long double;

struct Edge {
    int a, len;
    Edge(int a, int len) : a(a), len(len) {}
};

const int maxN = 128;
vector<Edge> nbh[maxN];
int n;

const ld inf = 1e12;
const ld eps = 1e-8;

int V[maxN];
int E[maxN];

inline void print(ld x) {
    printf("%.8lf ", (double) x);
}

inline bool eq(ld a, ld b) {
    return abs(a - b) < eps;
}

struct Lvertex {
    int v, e;
    ld dis;
    Lvertex(int v, int e, ld dis) : v(v), e(e), dis(dis) {}

    bool operator < (Lvertex const& o) const {
        return dis > o.dis;
    }
};

void limited_dijkstra(int v, int e, ld vel, ld* dis) {
//     printf("DIJKSTRA ==== %d E:%d, v: ", v, e);
//     print(vel);
//     puts("");
    for(int i = 1; i <= n; ++i) dis[i] = inf;
    dis[v] = 0;
    priority_queue<Lvertex> q;
    q.emplace(v, e, 0);

    Lvertex lv(0, 0, 0);
    while(!q.empty()) {
        lv = q.top();
        q.pop();
        if(!eq(dis[lv.v], lv.dis)) continue;
        
//         printf("v: %d e: %d dis: ", lv.v, lv.e);
//         print(lv.dis);
//         puts("");

        for(Edge const& e : nbh[lv.v]) {
            if(lv.dis + e.len / vel < dis[e.a] && e.len <= lv.e) {
                dis[e.a] = lv.dis + e.len / vel;
                q.emplace(e.a, lv.e - e.len, dis[e.a]);
            }
        }
    }
    /*
    printf("lens from %d:", v);
    for(int i = 1; i <= n; ++i) {
        printf("%d: ", i);
        print(dis[i]);
    }
    printf("\n");*/
}

ld tim[maxN][maxN];

ld dis[maxN];
bool B[maxN];
void dijkstra(int v) {
//     printf("DIJKSTRA from %d\n", v);
    for(int i = 0; i <= n; ++i) {
        dis[i] = inf;
        B[i] = 0;
    }
    dis[v] = 0;
    int minv = v;
    for(int i = 0; i < n; ++i) {
//         printf("-- %d -- ", v);
//         print(dis[v]);
//         puts("");

        B[v] = 1;
        minv = 0;
        for(int a = 1; a <= n; ++a) {
//             printf("%d -> %d ", v, a);
//             print(tim[v][a]);
//             print(dis[a]);
            dis[a] = min(dis[a], dis[v] + tim[v][a]);
            if(!B[a] && dis[minv] > dis[a]) minv = a;
//             printf("minv = %d\n", minv);
//             puts("");
        }
        v = minv;
    }
}


void prog() {
    int q;
    scanf("%d%d", &n, &q);
    for(int i = 1; i <= n; ++i) scanf("%d%d", E+i, V+i);
    for(int i = 1; i <= n; ++i) nbh[i].clear();
    for(int i = 1; i <= n; ++i) for(int c, j = 1; j <= n; ++j) {
        scanf("%d", &c);
        if(i != j && c >= 0)
            nbh[i].emplace_back(j, c);
    }
    for(int i = 1; i <= n; ++i) limited_dijkstra(i, E[i], V[i], tim[i]);
    
    for(int a, b, i = 0; i < q; ++i) {
        scanf("%d%d", &a, &b);
        dijkstra(a);
        assert(dis[b] < inf);
        print(dis[b]);
    }
    printf("\n");
}

int main() {
    int _t;
    scanf("%d", &_t);
    for(int i = 1; i <= _t; ++i) {
        printf("Case #%d: ", i);
        fprintf(stderr, "test %d... ", i);
        prog();
        fprintf(stderr, "OK\n");
    }
}