#include <iostream>
#include <string>
#include <vector>
#include <sstream>
#include <queue>
#include <algorithm>
#include <iomanip>
#include <map>
#include <set>
#include <math.h>
#include <stack>
#include <deque>
#include <numeric>
#include <cstring>
#include <cstdio>
#include <list>
#include <cstdlib>
#include <bitset>
#include <ctime>

#define all(v) (v).begin(),(v).end()
using namespace std;
typedef long long ll;
typedef unsigned long long ull;
typedef long double ld;
const ld epsylon = 1e-9;
const ld inf = 1e30;

int n, q;
ld energy[100],speed[100];
int d[100][100];
pair<int,int> uv[100];

ld graph[100][100];
bool vis[100];
ld dijkstraMem[100][100];


void dijkstra(int from) {
    ld dist[100];
    bool sptSet[100];
    memset(sptSet,0,sizeof(sptSet));

    for (int i = 0; i < n; ++i) {
        dist[i] = inf;
    }
    dist[from] = 0;
    for (int cnt = 0; cnt < n-1;++cnt) {
        ld mn = inf; int min_index = -1;

        for (int v = 0; v < n; v++)
            if (sptSet[v] == false && dist[v] <= mn)
                mn = dist[v], min_index = v;
        int u = min_index;
        sptSet[u] = true;

        for (int v = 0; v < n; v++)
            if (!sptSet[v] && graph[u][v] > -1.0 && dist[u] < inf
                && dist[u]+graph[u][v] < dist[v])
                dist[v] = dist[u] + graph[u][v];
    }
    for (int i = 0; i < n; ++i) {
        dijkstraMem[from][i] = dist[i];
    }
}

void bfs(int horse) {
    memset(vis,0,sizeof(vis));
    queue<pair<int, ld> > que;
    vis[horse] = 1;
    que.push(make_pair(horse, energy[horse]));
    while (!que.empty()) {
        int curCity = que.front().first;
        ld leftEnergy = que.front().second;
        que.pop();
        if (curCity != horse) {
            graph[horse][curCity] = (energy[horse]-leftEnergy)/speed[horse];
        }

        for (int nextCity = 0; nextCity < n; ++nextCity) {
            if (!vis[nextCity]
                    && d[curCity][nextCity] > -1
                    && d[curCity][nextCity] <= leftEnergy) {
                vis[nextCity] = 1;
                que.push(make_pair(nextCity, leftEnergy - d[curCity][nextCity]));
            }
        }
    }
}

void solve() {
    fill(&graph[0][0], &graph[99][100], -1.0);
    scanf("%d %d",&n,&q);
    memset(d, -1, sizeof(d));
    for (int i = 0; i < n; ++i) {
        scanf("%Lf %Lf", &energy[i], &speed[i]);
    }
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) {
            scanf("%d",&d[i][j]);
        }
    }
    for (int i = 0; i < q; ++i) {
        scanf("%d %d", &(uv[i].first), &(uv[i].second));
        uv[i].first--;uv[i].second--;
    }
    for (int i = 0; i < n; ++i) {
        bfs(i);
    }
    for (int i = 0; i < n; ++i) {
        dijkstra(i);
    }
    for (int i = 0; i < q-1; ++i) {
        printf("%Lf ", dijkstraMem[uv[i].first][uv[i].second]);
    }
    int i = q-1;
    printf("%Lf", dijkstraMem[uv[i].first][uv[i].second]);
}

int main() {
    freopen("/XCodeProjects/codejam2017/q-round/codejam-q/DerivedData/codejam-q/Build/Products/Debug/c.in", "r", stdin);
    freopen("/XCodeProjects/codejam2017/q-round/codejam-q/DerivedData/codejam-q/Build/Products/Debug/c.out", "w", stdout);

    int tests;
    scanf("%d\n", &tests);

    for (int test = 1; test <= tests; ++test) {

        printf("Case #%d: ", test);
        solve();
        printf("\n");
    }
    
    return 0;
}