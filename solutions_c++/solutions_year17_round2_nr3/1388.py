#include <cstdio>
#include <queue>
#include <string>
#include <cstring>
#include <cmath>
#include <set>
#include <vector>
#include <list>
#include <iostream>
#include <map>
#include <algorithm>

using namespace std;

typedef long long ll;
typedef pair<int, int> P;

//int dir[] = { 0, -1, 0, 1, 0 };
const int MAX_NUM = 100;
const double INF = 1e20;
int T = 0, N, Q;

int dist[MAX_NUM], speed[MAX_NUM];
int graph[MAX_NUM][MAX_NUM] = {};
int u, v;

double res[MAX_NUM] = {};

double solve() {
    fill_n(res, N, INF);
    res[N-1] = 0.0;
    
    for (int i = N-2; 0 <= i; i--) {
        double curr = 0;
        for (int j = i+1; j < N; j++) {
            curr += graph[j-1][j];
            if (curr <= dist[i]) {
                res[i] = min(res[i], curr / speed[i] + res[j]);
            }
        }
    }

    return res[0];
}

int main() {
    freopen("1c.in", "r", stdin);
    scanf("%d\n", &T);
    
    for (int t = 1; t <= T; t++) {
        printf("Case #%d:", t);
        
        scanf("%d %d", &N, &Q);
        for (int i = 0; i < N; i++) {
            scanf("%d %d\n", &dist[i], &speed[i]);
        }
        
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                scanf("%d", &graph[i][j]);
            }
        }
        
        for (int q = 0; q < Q; q++) {
            scanf("%d %d\n", &u, &v);
            u--; v--;
            printf(" %f", solve());
        }
        printf("\n");
        
    }
    
    return 0;
}
