#include <bits/stdc++.h>
#define SZ(x) ((int) (x).size())
using namespace std;

const string BAD = "IMPOSSIBLE", OK = "POSSIBLE";

struct State {
    int x, y, dir;
    State() = default;
    State(int _x, int _y, int _dir):
        x(_x), y(_y), dir(_dir) {}
};

class TwoSatSolver {
public:
    TwoSatSolver(int _n):
        G(vector<vector<int>>(2 * _n)),
        Gt(vector<vector<int>>(2 * _n)),
        used(vector<bool>(2 * _n)),
        value(vector<int>(2 * _n, 0)),
        nodes(vector<int>()),
        n(_n) {}

    void addEdge(int from, int to) {
        G[from].push_back(to);
        Gt[to].push_back(from);
    }

    void addRelation(int x, int y) {
        addEdge(non(x), y);
        addEdge(non(y), x);
    }

    int non(int x) {
        return x >= n ? x - n: x + n;
    }

    vector<int> solve() {
        for (int i = 0; i < 2 * n; ++i) {
            if (!used[i]) {
                dfs1(i);
            }
        }
        for (int i = 2 * n - 1; i >= 0; --i) {
            int node = nodes[i];
            if (used[node] && used[non(node)]) {
                if (dfs2(node) == -1) {
                    return vector<int>(1, -1);
                }
            }
        }
        return value;
    }
private:
    vector<vector<int>> G, Gt;
    vector<bool> used;
    vector<int> value;
    vector<int> nodes;
    int n;

    void dfs1(int node) {
        used[node] = true;
        for (int to: G[node]) {
            if (!used[to]) {
                dfs1(to);
            }
        }
        nodes.push_back(node);
    }
    int dfs2(int node) {
        used[node] = false;
        if (value[node]) {
            return -1;
        }
        value[non(node)] = 1;
        value[node] = 0;
        for (int to: Gt[node]) {
            if (used[to]) {
                if (dfs2(to) == -1) {
                    return -1;
                }
            }
        }
        return 0;
    }
};

const int dx[] = {-1, 0, 1, 0};
const int dy[] = {0, 1, 0, -1};

pair<bool, vector<pair<int, int>>> tryConf(const vector<string>& a,
             const vector<State>& start) {
    int n = SZ(a), m = SZ(a[0]);
    queue<State> q;
    vector<vector<vector<bool>>> 
        used(n, vector<vector<bool>>(m, vector<bool>(4, false)));
    for (const State& s: start) {
        q.push(s);
        used[s.x][s.y][s.dir] = true;
    }
    vector<pair<int, int>> acc;
    while (!q.empty()) {
        State s = q.front();
        q.pop();
        
        if (a[s.x][s.y] == '.') {
            acc.push_back(make_pair(s.x, s.y));
        }
        if (a[s.x][s.y] == '/') {
            if (s.dir == 0) {
                s.dir = 1;
            } else if (s.dir == 1) {
                s.dir = 0;
            } else if (s.dir == 2) {
                s.dir = 3;
            } else {
                s.dir = 2;
            }
        } else if (a[s.x][s.y] == '\\') {
            if (s.dir == 0) {
                s.dir = 3;
            } else if (s.dir == 3) {
                s.dir = 0;
            } else if (s.dir == 1) {
                s.dir = 2;
            } else {
                s.dir = 1;
            }
        }
        int nx = s.x + dx[s.dir];
        int ny = s.y + dy[s.dir];
        if (0 <= nx && nx < n && 0 <= ny && ny < m) {
            if (a[nx][ny] == '-' || a[nx][ny] == '|') {
                return make_pair(false, vector<pair<int, int>>());
            }
            if (!used[nx][ny][s.dir] && a[nx][ny] != '#') {
                used[nx][ny][s.dir] = true;
                q.push(State(nx, ny, s.dir));
            }
        }
    }
    sort(acc.begin(), acc.end());
    acc.erase(unique(acc.begin(), acc.end()), acc.end());
    return make_pair(true, acc);
}

void solve() {
    int n, m;
    cin >> n >> m;
    vector<string> a(n);
    for (int i = 0; i < n; ++i) {
        cin >> a[i];
    }
    vector<vector<int>> acc1(n, vector<int>(m, -1));
    vector<vector<int>> acc2(n, vector<int>(m, -1));
    int cntVariables = 0;
    vector<vector<int>> index(n, vector<int>(m, - 1));
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < m; ++j) {
            if (a[i][j] == '|' || a[i][j] == '-') {
                index[i][j] = cntVariables++;
            }
        }
    }
    TwoSatSolver t(cntVariables);
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < m; ++j) {
            if (a[i][j] == '|' || a[i][j] == '-') {
                bool can1;
                vector<pair<int, int>> ac1;
                tie(can1, ac1) = tryConf(a, {State(i, j, 0), State(i, j, 2)}); // |
                bool can2;
                vector<pair<int, int>> ac2;
                tie(can2, ac2) = tryConf(a, {State(i, j, 1), State(i, j, 3)}); // -
                if (!can1 && !can2) {
                    cout << BAD << '\n';
                    return;
                }
                if (!can1) {
                    t.addRelation(index[i][j] + cntVariables,
                            index[i][j] + cntVariables);
                } else if (!can2) {
                    t.addRelation(index[i][j], index[i][j]);
                }
                for (const pair<int, int>& p: ac1) {
                    if (acc1[p.first][p.second] == -1) {
                        acc1[p.first][p.second] = index[i][j];
                    } else {
                        acc2[p.first][p.second] = index[i][j];
                    }
                }
                for (const pair<int, int>& p: ac2) {
                    if (acc1[p.first][p.second] == -1) {
                        acc1[p.first][p.second] = cntVariables + index[i][j];
                    } else {
                        acc2[p.first][p.second] = cntVariables + index[i][j];
                    }
                }
            }
        }
    }
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < m; ++j) {
            if (a[i][j] == '.') {
                if (acc1[i][j] == -1) {
                    cout << BAD << '\n';
                    return;
                } else if (acc2[i][j] == -1) {
                    t.addRelation(acc1[i][j], acc1[i][j]);
                } else {
                    t.addRelation(acc1[i][j], acc2[i][j]);
                }
            }
        }
    }
    vector<int> values = t.solve();
    if (SZ(values) > 0 && values[0] == -1) {
        cout << BAD << '\n';
    } else {
        cout << OK << '\n';
        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < m; ++j) {
                if (index[i][j] != -1) {
                    int x = index[i][j];
                    if (values[x]) {
                        a[i][j] = '|';
                    } else {
                        a[i][j] = '-';
                    }
                }
            }
            cout << a[i] << '\n';
        }
    }
}

int main() {
    #ifdef LOCAL_RUN
    freopen("task.in", "r", stdin);
    freopen("task.out", "w", stdout);
    //freopen("task.err", "w", stderr);
    #endif // ONLINE_JUDGE
    ios::sync_with_stdio(false);
    cin.tie(0);

    int T;
    cin >> T;

    for (int t = 1; t <= T; ++t) {
        cout << "Case #" << t << ": ";
        solve();
    }
}
