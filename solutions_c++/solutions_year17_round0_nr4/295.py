#define STRINGIZE(x) #x
#define STRINGIZE2(x) STRINGIZE(x)
#define FP STRINGIZE2(FILEPATH)

#include <iostream>
#include <cstdio>
#include <cassert>
#include <string>
#include <vector>
using namespace std;

const int N = 100 + 3;

int n, k;
char a[N][N];

bool read() {
    if (scanf("%d%d", &n, &k) != 2) {
        return false;
    }
    
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            a[i][j] = '.';
        }
    }
    
    for (int i = 0; i < k; i++) {
        char ch;
        int r, c;
        assert(scanf(" %c%d%d", &ch, &r, &c) == 3);
        r--, c--;
        
        a[r][c] = ch;
    }
    
    return true;
}

struct edge {
    int to, f, c, rev;
    edge(int to, int f, int c, int rev): to(to), f(f), c(c), rev(rev) {}
};

const int V = 30 * 1000 + 13;

int S, T, d[V], ptr[V], q[V];
vector<edge> g[V];

void addEdge(int from, int to, int c) {
    edge f = { to, 0, c, int(g[to].size()) };
    edge b = { from, 0, 0, int(g[from].size()) };
    g[from].push_back(f);
    g[to].push_back(b);
}

bool bfs() {
    int qh=0, qt=0;
    q[qt++] = S;
    memset (d, -1, sizeof d);
    d[S] = 0;
    while (qh < qt && d[T] == -1) {
        int v = q[qh++];
        for (size_t i=0; i<g[v].size(); ++i) {
            edge& e = g[v][i];
            int to = e.to;
            if (d[to] == -1 && e.f < e.c) {
                q[qt++] = to;
                d[to] = d[v] + 1;
            }
        }
    }
    return d[T] != -1;
}

int dfs (int v, int flow) {
    if (!flow)  return 0;
    if (v == T)  return flow;
    for (; ptr[v]<(int)g[v].size(); ++ptr[v]) {
        edge& e = g[v][ptr[v]];
        int to = e.to;
        if (d[to] != d[v] + 1)  continue;
        int pushed = dfs (to, min (flow, e.c - e.f));
        if (pushed) {
            e.f += pushed;
            g[to][e.rev].f -= pushed;
            return pushed;
        }
    }
    return 0;
}

int dinic() {
    int flow = 0;
    for (;;) {
        if (!bfs())  break;
        memset (ptr, 0, sizeof ptr);
        while (int pushed = dfs (S, (int) 1e9))
            flow += pushed;
    }
    return flow;
}

void solve(int test) {
    printf("Case #%d: ", test + 1);
    
    vector<vector<char>> plus(n, vector<char>(n, false));
    vector<vector<char>> cross(n, vector<char>(n, false));
    
    // Rows and cols
    {
        for (int i = 0; i < V; i++) {
            g[i].clear();
        }
        
        S = n * n + 2 * n;
        T = S + 1;
        
        vector<char> saturatedRow(n, false);
        vector<char> saturatedCol(n, false);
        
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (a[i][j] == '.' || a[i][j] == '+') {
                    addEdge(n * n + i, i * n + j, 1);
                    addEdge(i * n + j, n * n + n + j, 1);
                } else {
                    saturatedRow[i] = true;
                    saturatedCol[j] = true;
                    cross[i][j] = true;
                }
            }
        }
        
        for (int i = 0; i < n; i++) {
            if (!saturatedRow[i]) {
                addEdge(S, n * n + i, 1);
            }
            if (!saturatedCol[i]) {
                addEdge(n * n + n + i, T, 1);
            }
        }
        
        dinic();
        
        for (int i = n * n; i < n * n + n; i++) {
            for (const auto &e : g[i]) {
                if (e.f > 0) {
                    int x = e.to / n;
                    int y = e.to % n;
                    cross[x][y] = true;
                }
            }
        }
    }
    
    // Diagonals
    {
        for (int i = 0; i < V; i++) {
            g[i].clear();
        }
        
        const int diagCount = 2 * n - 1;
        S = n * n + 2 * diagCount;
        T = S + 1;
        
        vector<char> saturatedMajorDiag(diagCount, false);
        vector<char> saturatedMinorDiag(diagCount, false);
        
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (a[i][j] == '.' || a[i][j] == 'x') {
                    addEdge(n * n + i + j, n * i + j, 1);
                    addEdge(n * i + j, n * n + diagCount + (i - j + n - 1), 1);
                } else {
                    saturatedMinorDiag[i + j] = true;
                    saturatedMajorDiag[i - j + n - 1] = true;
                    plus[i][j] = true;
                }
            }
        }
        
        for (int i = 0; i < diagCount; i++) {
            if (!saturatedMinorDiag[i]) {
                addEdge(S, n * n + i, 1);
            }
            if (!saturatedMajorDiag[i]) {
                addEdge(n * n + diagCount + i, T, 1);
            }
        }
        
        dinic();
        
        for (int i = n * n; i < n * n + diagCount; i++) {
            for (const auto& e : g[i]) {
                if (e.f > 0) {
                    int x = e.to / n;
                    int y = e.to % n;
                    plus[x][y] = true;
                }
            }
        }
    }
    
//    for (int i = 0; i < n; i++) {
//        for (int j = 0; j < n; j++) {
//            putchar(plus[i][j] ? '+' : '.');
//        }
//        puts("");
//    }
//    
//    for (int i = 0; i < n; i++) {
//        for (int j = 0; j < n; j++) {
//            putchar(cross[i][j] ? 'x' : '.');
//        }
//        puts("");
//    }
    
    int result = 0;
    vector<pair<char, pair<int, int>>> ans;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            int prev = 0;
            if (a[i][j] == 'x' || a[i][j] == '+') {
                prev = 1;
            } else if (a[i][j] == 'o') {
                prev = 2;
            }
            
            char newCh = '.';
            int cur = 0;
            if (plus[i][j] && cross[i][j]) {
                cur = 2;
                newCh = 'o';
            } else if (plus[i][j]) {
                cur = 1;
                newCh = '+';
            } else if (cross[i][j]) {
                cur = 1;
                newCh = 'x';
            }
            
            assert(cur >= prev);
            result += cur;
            if (cur > prev) {
                ans.push_back(make_pair(newCh, make_pair(i, j)));
            }
        }
    }
    
    printf("%d %d\n", result, (int) ans.size());
    for (int i = 0; i < ans.size(); i++) {
        printf("%c %d %d\n", ans[i].first, ans[i].second.first + 1, ans[i].second.second + 1);
    }
}

int main() {
    freopen(FP "input.txt", "rt", stdin);
    freopen(FP "output.txt", "wt", stdout);
    
    int testCount;
    cin >> testCount;
    
    for (int test = 0; test < testCount; test++) {
        assert(read());
        solve(test);
    }
    
    return 0;
}
