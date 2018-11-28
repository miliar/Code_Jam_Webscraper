#define _USE_MATH_DEFINES

#include <algorithm>
#include <array>
#include <bitset>
#include <cassert>
#include <climits>
#include <cmath>
#include <cstddef>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <deque>
#include <functional>
#include <iostream>
#include <iterator>
#include <limits>
#include <map>
#include <queue>
#include <set>
#include <string>
#include <utility>
#include <vector>

using namespace std;

typedef long long ll;
typedef long double ld;
typedef pair<int, int> pii;
typedef pair<ll, ll> pll;

const int INF = 1000 * 1000 * 1000 + 11;


typedef pair<int, int> coord_t;
const vector<coord_t> DS = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};
const map<coord_t, coord_t> DA = {
    {{-1, 0}, {0, 1}},
    {{1, 0}, {0, -1}},
    {{0, -1}, {1, 0}},
    {{0, 1}, {-1, 0}},
};

const map<coord_t, coord_t> DB = {
    {{-1, 0}, {0, -1}},
    {{1, 0}, {0, 1}},
    {{0, -1}, {-1, 0}},
    {{0, 1}, {1, 0}},
};

int N, M;
char FIELD[100][100];

coord_t add(const coord_t &a, const coord_t &b) {
    return {a.first + b.first, a.second + b.second};
}

inline bool ok(const coord_t &pos) {
    return pos.first >= 0 && pos.first < N && pos.second >= 0 && pos.second < M;
}

inline char GET(const coord_t &pos) {
    return FIELD[pos.first][pos.second];
}

map<coord_t, vector<int>> empty_cells;

bool model(coord_t pos, coord_t d, int num) {
    if (!ok(pos)) return true;
    
    char ch = GET(pos);
    if (ch == '#') return true;
    if (ch == '|' || ch == '-') return false;
    
    if (ch == '.') empty_cells[pos].push_back(num);
    if (ch == '/') d = DA.at(d);
    if (ch == '\\') d = DB.at(d);
    
    return model(add(pos, d), d, num);
}

inline int comp(int v, int n) {
    return v < n ? v + n : v - n;
}

void dfs_1(int n, const vector<vector<int>> &graph, vector<bool> &vis, vector<int> &top_sort) {
    vis[n] = true;
    for (int to : graph[n]) {
        if (!vis[to]) dfs_1(to, graph, vis, top_sort);
    }
    top_sort.push_back(n);
}

void dfs_2(int n, const vector<vector<int>> &graph, vector<int> &comp, int curr_comp) {
    comp[n] = curr_comp;
    for (int to : graph[n]) {
        if (!comp[to]) dfs_2(to, graph, comp, curr_comp);
    }
}


bool solve() {
    map<int, coord_t> shooters;
    empty_cells.clear();
    
    for (int i = 0; i != N; ++i) {
        for (int j = 0; j != M; ++j) {
            if (FIELD[i][j] == '.') {
                empty_cells[{i, j}] = vector<int>();
            } else if (FIELD[i][j] == '-' || FIELD[i][j] == '|') {
                int num = shooters.size();
                shooters[num] = {i, j};
            }
        }
    }
    
    int S = shooters.size();
    vector<vector<int>> graph(2 * S);
    
    for (const auto &shooter : shooters) {
        int num = shooter.first;
        if (!model(add(shooter.second, DS[0]), DS[0], num) || !model(add(shooter.second, DS[1]), DS[1], num)) {
            graph[num].push_back(comp(num, S));
        }
        num += shooters.size();
        if (!model(add(shooter.second, DS[2]), DS[2], num) || !model(add(shooter.second, DS[3]), DS[3], num)) {
            graph[num].push_back(comp(num, S));
        }
    }
    
    for (const auto &cell : empty_cells) {
        const auto &val = cell.second;
        
        
        if (val.empty()) return false;
        bool flag = false;
        
        set<int> t(val.begin(), val.end());
        for (int i = 0; i != S; ++i) {
            if (t.count(i) && t.count(i + S)) {
                flag = true;
            }
        }
        
        if (flag) continue;
        vector<int> vval(t.begin(), t.end());
        
        assert(vval.size() <= 2);
        
        if (vval.size() == 1) {
            graph[comp(vval[0], S)].push_back(vval[0]);
        } else {
            graph[comp(vval[0], S)].push_back(vval[1]);
            graph[comp(vval[1], S)].push_back(vval[0]);
        }
    }
    
    vector<vector<int>> tr_graph(2 * S);
    for (int i = 0; i != 2 * S; ++i) {
        for (int to : graph[i]) {
            tr_graph[to].push_back(i);
        }
    }
    
    vector<bool> visited(2 * S, false);
    vector<int> top_sort;
    vector<int> component(2 * S, 0);
    
    for (int i = 0; i != 2 * S; ++i) {
        if (!visited[i]) dfs_1(i, graph, visited, top_sort);
    }
    
    reverse(top_sort.begin(), top_sort.end());
    
    int last_comp = 0;
    for (int v : top_sort) {
        if (!component[v]) dfs_2(v, tr_graph, component, ++last_comp);
    }
    
    for (int i = 0; i != S; ++i) {
        if (component[i] == component[comp(i, S)]) {
            return false;
        }
        
        coord_t pos = shooters[i];
        FIELD[pos.first][pos.second] = (component[i] > component[comp(i, S)]) ? '|' : '-';
    }
    
    return true;
}


int main() {
    freopen("/Users/iskhakovt/Downloads/C-large.in", "r", stdin);
    
    ios_base::sync_with_stdio(false);
    
    int tests;
    cin >> tests;
    
    for (int test = 0; test != tests; ++test) {
        cout << "Case #" << test + 1 << ": ";
        
        cin >> N >> M;
        for (int i = 0; i != N; ++i) {
            string str;
            cin >> str;
            for (int j = 0; j != M; ++j) {
                FIELD[i][j] = str[j];
            }
        }
        
        bool res = solve();
        if (!res) {
            cout << "IMPOSSIBLE\n";
        } else {
            cout << "POSSIBLE\n";
            for (int i = 0; i != N; ++i) {
                for (int j = 0; j != M; ++j) {
                    cout << FIELD[i][j];
                }
                cout << "\n";
            }
        }
    }
    
    return 0;
}