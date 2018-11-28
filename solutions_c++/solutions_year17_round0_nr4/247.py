#include <bits/stdc++.h>

using namespace std;
typedef long long ll;

const int N = 210;
int grid[N][N];
int new_grid[N][N];
int graph[N][N];
bool used[N];
int mt[N];

bool try_kuhn (int v, int len) {
	if (used[v])
        return false;
	used[v] = true;
	for (int to = 0; to < len; to++) {
        if (graph[v][to] == 0)
            continue;
		if (mt[to] == -1 || try_kuhn(mt[to], len)) {
			mt[to] = v;
			return true;
		}
	}
	return false;
}



void solve() {
    int n, m;
    cin >> n >> m;
    set<int> row;
    set<int> col;
    set<int> diag_l;
    set<int> diag_r;
    for (int i = 0; i < n; i++) {
        fill(grid[i], grid[i] + n, 0);
        fill(new_grid[i], new_grid[i] + n, 0);
        row.insert(i);
        col.insert(i);
    }
    for (int i = 0; i < 2 * n - 1; i++) {
        diag_l.insert(i);
        diag_r.insert(i);
        fill(graph[i], graph[i] + 2 * n - 1, 0);
    }
    for (int i = 0; i < m; i++) {
        string type;
        int a, b;
        cin >> type >> a >> b;
        a--; b--;
        if (type[0] == '+') {
            grid[a][b] = 1;
            diag_l.erase(a - b + n - 1);
            diag_r.erase(a + b);
        }
        if (type[0] == 'x') {
            grid[a][b] = 2;
            row.erase(a);
            col.erase(b);
        }
        if (type[0] == 'o') {
            grid[a][b] = 3;
            row.erase(a);
            col.erase(b);
            diag_l.erase(a - b + n - 1);
            diag_r.erase(a + b);
        }
        new_grid[a][b] = grid[a][b];
    }
    for (auto r = row.begin(),  c = col.begin(); r != row.end(); r++, c++) {
        new_grid[*r][*c] += 2;
    }
    for (auto l : diag_l) {
        for (auto r : diag_r) {
            if ((l + r + n + 1) % 2 == 0 && l + r >= n - 1 && r - l >= 1 - n && ((l - n + 1) + r) / 2 < n && (-(l - n + 1) + r) / 2 < n) {
                graph[l][r] = 1;
            }
        }
    }
    int len = 2 * n - 1;
    fill(mt, mt + len, -1);
    for (int i = 0; i < len; i++) {
        fill(used, used + len, false);
        try_kuhn(i, len);
    }
    for (int i = 0; i < len; i++) {
        if (mt[i] >= 0) {
            int l = (i - n + 1 + mt[i]) / 2;
            int r = (i - (mt[i] - n + 1)) / 2;
            new_grid[l][r] += 1;
        }
    }
    int cost = 0;
    int changes = 0;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            cost += (new_grid[i][j] + 1) / 2;
            if (new_grid[i][j] != grid[i][j])
                changes++;
        }
    }
    cout << cost << " " << changes << "\n";
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            if (new_grid[i][j] != grid[i][j]) {
                if (new_grid[i][j] == 1)
                    cout << "+ ";
                if (new_grid[i][j] == 2)
                    cout << "x ";
                if (new_grid[i][j] == 3)
                    cout << "o ";
                cout << i + 1 << " " << j + 1 << "\n";
            }
        }
    }
}

int main()
{
    ios_base::sync_with_stdio(0);
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int t;
    cin >> t;
    for (int i = 1; i <= t; i++) {
        cout << "Case #" << i << ": ";
        solve();
    }
    cin.tie(nullptr);
    return 0;
}
