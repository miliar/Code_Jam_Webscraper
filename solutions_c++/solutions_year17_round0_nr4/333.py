#include<bits/stdc++.h>
using namespace std;

#define X first
#define Y second

#define debug(a) cerr << #a << " = " << (a) << endl;

typedef long long ll;
typedef pair<int, int> pii;
typedef vector<int> vi;
typedef vector<vi> vvi;

template<typename T> ostream& operator<<(ostream& o, vector<T>& v) {
    for (auto& a: v) o << a << ' ';
    return o;
}

typedef map<pii, int> mpii;
string PC = "+xo";

struct bipartite_matching {
    int L, R, p;  vi m, used, d; vvi adj; queue<int> q;
    bool bfs() {
        for (int v=0; v<R; v++) if (!used[v]) d[v] = p, q.push(v);
        while (!q.empty()) {
            int v = q.front(); q.pop();
            if (d[v] != d[R])
                for (int u : adj[v])
                    if (d[m[u]] < p)
                        d[m[u]] = d[v] + 1, q.push(m[u]);
        }
        return d[R] >= p;
    }
    int dfs(int v) {
        if (v == R) return 1;
        for (int u : adj[v])
            if (d[m[u]] == d[v] + 1 && dfs(m[u]))
                return m[u] = v, 1;
        d[v] = d[R];  return 0;
    }

    bipartite_matching(int l, int r) : L(l), R(r), d(r+1), adj(r) { }
    void add_edge(int u, int v) { adj[v].push_back(u); }
    pair<int, vi> match() {
        int res = 0;  m.assign(L, R), used.assign(R+1, 0);
        for (p=0; bfs(); p = d[R]+1)
            for (int v=0; v<R; v++)
                if (!used[v] && dfs(v)) used[v] = 1, res++;
        replace(m.begin(), m.end(), R, -1); return {res, m};
    }
};

void addc(mpii &ans, vvi& grid, char cc, int i, int j){
    int c = (int)PC.find(cc);
    if (grid[i][j] == c) return;
    grid[i][j] = c;
    ans[{i, j}] = c;
}

int score(const vvi& grid){
    int n = (int)grid.size();
    int res = 0;
    for (int i = 0; i < n; i++)
        for (int j = 0; j < n; j++){
            if (grid[i][j] >= 0) res++;
            if (grid[i][j] >= 2) res++;
        }
    return res;
}

void addplus(vvi& grid, mpii& ans){
    int n = (int)grid.size();
    int m = 2*n - 1;
    bipartite_matching bm(m, m);
    int m1 = 0, m2 = 0;
    vvi d1(n, vi(n)), d2(n, vi(n)); // belongs to
    vi vis1(m), vis2(m);
    map<pii, pii> mmap;

    for (int i = 0; i < n; i++){
        for (int j = 0; j < n; j++){
            if (i == 0 || j == 0) {
                int K = min(n - i, n - j);
                for (int k = 0; k < K; k++) {
                    d1[i+k][j+k] = m1;
                    if (grid[i+k][j+k] != -1 &&
                        grid[i+k][j+k] != (int)PC.find('x')){
                        vis1[m1] = 1;
                    }
                }
                m1++;
            }
            if (i == 0 || j == n-1) {
                int K = min(n - i, j + 1);
                for (int k = 0; k < K; k++) {
                    d2[i+k][j-k] = m2;
                    if (grid[i+k][j-k] != -1 &&
                        grid[i+k][j-k] != (int)PC.find('x')){
                        vis2[m2] = 1;
                    }
                }
                m2++;
            }
        }
    }

    for (int i = 0; i < n; i++)
        for (int j = 0; j < n; j++){
            mmap[{d1[i][j], d2[i][j]}] = {i, j};
            if (grid[i][j] == -1 && !vis1[d1[i][j]] && !vis2[d2[i][j]])
                bm.add_edge(d1[i][j], d2[i][j]);
        }

    auto res = bm.match().Y;
    for (int i = 0; i < m; i++) {
        if (res[i] != -1){
            pii p = mmap[{i, res[i]}];
            addc(ans, grid, '+', p.X, p.Y);
        }
    }
}

void addcross(vvi& grid, mpii& ans){
    int n = (int)grid.size();
    bipartite_matching bm(n, n);
    vi row(n), col(n);
    for (int i = 0; i < n; i++)
        for (int j = 0; j < n; j++)
            if (grid[i][j] >= (int)PC.find('x'))
                row[i] = 1, col[j] = 1;

    for (int i = 0; i < n; i++)
        for (int j = 0; j < n; j++)
            if (grid[i][j] == -1 && !row[i] && !col[j])
                bm.add_edge(i, j);

    auto res = bm.match().Y;
    for (int i = 0; i < n; i++) {
        if (res[i] != -1)
            addc(ans, grid, 'x', i, res[i]);
    }
}

bool addcirc(vvi& grid, mpii& ans){
    int n = (int)grid.size();
    int m = 2*n - 1;
    vi row(n), col(n);
    int m1 = 0, m2 = 0;
    vvi d1(n, vi(n)), d2(n, vi(n)); // belongs to
    vi vis1(m), vis2(m);

    for (int i = 0; i < n; i++)
        for (int j = 0; j < n; j++)
            if (grid[i][j] >= (int)PC.find('x'))
                row[i] += 1, col[j] += 1;

    for (int i = 0; i < n; i++){
        for (int j = 0; j < n; j++){
            if (i == 0 || j == 0) {
                int K = min(n - i, n - j);
                for (int k = 0; k < K; k++) {
                    d1[i+k][j+k] = m1;
                    if (grid[i+k][j+k] != -1 &&
                        grid[i+k][j+k] != (int)PC.find('x')){
                        vis1[m1] += 1;
                    }
                }
                m1++;
            }
            if (i == 0 || j == n-1) {
                int K = min(n - i, j + 1);
                for (int k = 0; k < K; k++) {
                    d2[i+k][j-k] = m2;
                    if (grid[i+k][j-k] != -1 &&
                        grid[i+k][j-k] != (int)PC.find('x')){
                        vis2[m2] += 1;
                    }
                }
                m2++;
            }
        }
    }

    for (int i = 0; i < n; i++)
        for (int j = 0; j < n; j++){
            if (grid[i][j] == (int)PC.find('o')) continue;
            int x = grid[i][j] == (int)PC.find('x');
            if ((row[i] - x) || (col[j] - x)) continue;
            int p = grid[i][j] == (int)PC.find('+');
            if ((vis1[d1[i][j]] - p) || (vis2[d2[i][j]] - p)) continue;
            addc(ans, grid, 'o', i, j);
            return true;
        }
    return false;
}

void solve(){
    int n, k; cin >> n >> k;
    vvi grid(n, vi(n, -1));
    for (int i = 0; i < n; i++) for (int j = 0; j < n; j++) grid[i][j] = -1;
    for (int i = 0; i < k; i++){
        char cc;
        int x, y, pc;
        cin >> cc >> x >> y;
        pc = (int)PC.find(cc);
        x--; y--;
        grid[x][y] = pc;
    }
    if (n == 1) {
        if (grid[0][0] == (int)PC.find('o')) cout << "2 0" << endl;
        else {
            cout << "2 1" << endl;
            cout << "o 1 1" << endl;
        }
        return;
    }
    vvi g1 = grid, g2 = grid;
    mpii a1, a2;
    addplus(g1, a1);
    addcross(g1, a1);
    while (addcirc(g1, a1));

    addcross(g2, a2);
    addplus(g2, a2);
    while (addcirc(g2, a2));

    int s1 = score(g1), s2 = score(g2);
    if (s1 < s2) {
        swap(s1, s2);
        swap(a1, a2);
        swap(g1, g2);
    }
    cout << s1 << ' ' << (int)a1.size() << endl;
    for (auto &it : a1) {
        cout << PC[it.Y] << ' ' << it.X.X + 1 << ' ' << it.X.Y + 1 << endl;
    }
}

int main() {
    ios::sync_with_stdio(0);  cin.tie(0);
    int tc; cin >> tc;
    for (int cs = 1; cs <= tc; cs++){
        cout << "Case #" << cs << ": ";
        solve();
    }
}
