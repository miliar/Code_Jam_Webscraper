#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef pair<int, int> pi;
#define mp make_pair    
const int MAXN = 205;
/* Bipartite maching library from https://noiref.codecla.ws/, written by myself */
struct AugPath {
    int A, B;   //size of left, right groups
    vector<vector<int> > G; //size A
    vector<bool> visited;   //size A
    vector<int> P;          //size B
    
    AugPath(int _A, int _B): A(_A), B(_B), G(_A), P(_B, -1) {}
    
    void AddEdge(int a, int b) {    //a from left, b from right
        G[a].push_back(b);
    }
    bool Aug(int x) {
        if (visited[x]) return 0;
        visited[x] = 1;
        /* Greedy heuristic */
        for (auto it:G[x]) {
            if (P[it] == -1) {
                P[it] = x;
                return 1;
            }
        }
        for (auto it:G[x]) {
            if (Aug(P[it])) {
                P[it] = x;
                return 1;
            }
        }
        return 0;
    }
    int MCBM() {
        int matchings = 0;
        for (int i = 0; i < A; ++i) {
            visited.resize(A, 0);
            matchings += Aug(i);
            visited.clear();
        }
        return matchings;
    }
    vector<pair<int, int> > GetMatchings() {
        vector<pair<int, int> > matchings;
        for (int i = 0; i < B; ++i) {
            if (P[i] != -1) matchings.emplace_back(P[i], i);
        }
        return matchings;
    }
};
int N, M, TC;
bitset<MAXN> gxA, gxB, gpA, gpB, gx[MAXN], gp[MAXN];
char typ[5], g[MAXN][MAXN];
int main() {
    scanf("%d", &TC);
    for (int Txn = 1; Txn <= TC; ++Txn) {
        scanf("%d%d", &N, &M);
        memset(g, 0, sizeof g);
        int ans = 0;
        for (int i = 0,x, y; i < M; ++i) {
            scanf("%s%d%d", typ, &x, &y);
            --x, --y;
            if (typ[0] == 'o' || typ[0] == 'x') gx[x][y] = gxA[x] = gxB[y] = 1, ++ans;
            if (typ[0] == 'o' || typ[0] == '+') gp[x][y] = gpA[x+y] = gpB[x-y+N] = 1, ++ans;
            g[x][y] = typ[0];
        }
        AugPath ap(N, N);
        for (int i = 0; i < N; ++i) {
            if (gxA[i]) continue;
            for (int j = 0; j < N; ++j) {
                if (gxB[j]) continue;
                ap.AddEdge(i, j);
            }
        }
        
        ans += ap.MCBM();
        auto res = ap.GetMatchings();
        for (auto it:res) gx[it.first][it.second] = 1;
        
        ap = AugPath(N*2, N*2);
        for (int i = 0; i < N; ++i) {
            for (int j = 0; j < N; ++j) {
                if (gpA[i+j] || gpB[i-j+N]) continue;
                ap.AddEdge(i+j, i-j+N);
            }
        }
        ans += ap.MCBM();
        res = ap.GetMatchings();
        for (auto it:res) gp[(it.first+it.second-N)/2][(it.first-it.second+N)/2] = 1;
        
        vector<pi> pos;
        for (int i = 0; i < N; ++i) {
            for (int j = 0; j < N; ++j) {
                char t;
                if (gx[i][j] && gp[i][j]) t = 'o';
                else if (gx[i][j]) t = 'x';
                else if (gp[i][j])  t = '+';
                else continue;
                if (t != g[i][j]) {
                    pos.emplace_back(i, j);
                    g[i][j] = t;
                }
            }
        }
        
        printf("Case #%d: ", Txn);
        printf("%d %d\n", ans, pos.size());
        for (auto it:pos) printf("%c %d %d\n", g[it.first][it.second], it.first+1, it.second+1);
        
        gxA.reset();
        gxB.reset();
        gpA.reset();
        gpB.reset();
        for (int i = 0; i < N; ++i) gx[i].reset(), gp[i].reset();
    }
}