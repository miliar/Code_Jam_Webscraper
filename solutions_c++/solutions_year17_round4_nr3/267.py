#include <algorithm>
#include <climits>
#include <cstdio>
#include <cstring>
#include <set>
#include <vector>
#include <utility>

const int DELTA_X[] = {0,  0, -1, 1};
const int DELTA_Y[] = {-1, 1,  0, 0};

const int N = 52;
const int V = N * N * 2;

char buffer[N];
char grid[N][N];
std::set<int> passed[N][N];
std::vector<int> graph[V];

bool is_beam(int x, int y)
{
    return grid[x][y] == '-' || grid[x][y] == '|';
}

int dfn[V], low[V], scc[V], dfn_count, scc_count;
std::vector<int> stack;

void dfs(int u)
{
    if (dfn[u] == -1) {
        int tmp = dfn[u] = low[u] = dfn_count ++;
        stack.push_back(u);
        for (auto&& v : graph[u]) {
            dfs(v);
            tmp = std::min(tmp, low[v]);
        }
        low[u] = tmp;
        if (dfn[u] == low[u]) {
            int w;
            do {
                w = stack.back();
                stack.pop_back();
                low[w] = INT_MAX;
                scc[w] = scc_count;
            } while (u != w);
            scc_count ++;
        }
    }
}

int main()
{
    int T;
    scanf("%d", &T);
    for (int t = 1; t <= T; ++ t) {
        int n, m;
        scanf("%d%d", &n, &m);
        for (int i = 0; i < n + 2; ++ i) {
            for (int j = 0; j < m + 2; ++ j) {
                grid[i][j] = '#';
            }
        }
        for (int i = 0; i < n; ++ i) {
            scanf("%s", buffer);
            memcpy(grid[i + 1] + 1, buffer, sizeof(*buffer) * m);
        }
        for (int i = 1; i <= n; ++ i) {
            for (int j = 0; j <= m; ++ j) {
                passed[i][j].clear();
            }
        }
        int var_cnt = 0;
        std::vector<std::pair<int, int>> pts;
        for (int i = 0; i < V; ++ i) {
            graph[i].clear();
        }
        for (int i = 1; i <= n; ++ i) {
            for (int j = 1; j <= m; ++ j) {
                if (is_beam(i, j)) {
                    pts.emplace_back(i, j);
                    for (int k = 0; k < 4; ++ k) {
                        int var = var_cnt;
                        int x = i;
                        int y = j;
                        int d = k;
                        bool invalid = false;
                        for (int _ = 0; _ < n * m && !invalid; ++ _) {
                            x += DELTA_X[d];
                            y += DELTA_Y[d];
                            if (grid[x][y] == '#') {
                                break;
                            }
                            passed[x][y].insert(var);
                            if (grid[x][y] == '/') {
                                d ^= 3;
                            } else if (grid[x][y] == '\\') {
                                d ^= 2;
                            } else if (is_beam(x, y)) {
                                if (x == i && y == j) {
                                    invalid |= (k >> 1) != (d >> 1);
                                } else {
                                    invalid = true;
                                }
                            }
                        }
                        if (invalid) {
                            graph[var].push_back(var ^ 1);
                        }
                        if (k & 1) {
                            var_cnt ++;
                        }
                    }
                }
            }
        }
        bool failed = false;
        for (int i = 1; i <= n; ++ i) {
            for (int j = 1; j <= m; ++ j) {
                if (grid[i][j] == '.') {
                    if (passed[i][j].size() == 1) {
                        int var = *passed[i][j].begin();
                        graph[var ^ 1].push_back(var);
                    } else if (passed[i][j].size() == 2) {
                        int var1 = *passed[i][j].begin();
                        int var2 = *passed[i][j].rbegin();
                        graph[var1 ^ 1].push_back(var2);
                        graph[var2 ^ 1].push_back(var1);
                    } else {
                        failed = true;
                    }
                }
            }
        }
        if (!failed) {
            stack.clear();
            dfn_count = scc_count = 0;
            memset(dfn, -1, sizeof(dfn));
            for (int i = 0; i < var_cnt; ++ i) {
                dfs(i);
            }
            for (int i = 0; i < var_cnt; ++ i) {
                failed |= scc[i] == scc[i ^ 1];
            }
        }
        printf("Case #%d: %s\n", t, failed ? "IMPOSSIBLE" : "POSSIBLE");
        if (!failed) {
            for (int i = 0; i < var_cnt; i += 2) {
                int x = pts[i >> 1].first;
                int y = pts[i >> 1].second;
                if (scc[i] < scc[i ^ 1]) {
                    grid[x][y] = '-';
                } else {
                    grid[x][y] = '|';
                }
            }
            for (int i = 1; i <= n; ++ i) {
                for (int j = 1; j <= m; ++ j) {
                    putchar(grid[i][j]);
                }
                puts("");
            }
        }
    }
}
