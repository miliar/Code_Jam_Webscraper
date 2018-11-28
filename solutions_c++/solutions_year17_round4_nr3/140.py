#include <cmath>
#include <cstdio>
#include <cctype>
#include <cstdlib>
#include <climits>
#include <cstring>
#include <vector>
#include <string>
#include <iostream>
#include <cassert>
#include <algorithm>

using namespace std;

const int N = 50 + 5;
const int dx[] = {1, 0, -1, 0};
const int dy[] = {0, 1, 0, -1};
const int d0[] = {3, 2, 1, 0};
const int d1[] = {1, 0, 3, 2};

int n, m;
char a[N][N];
vector<int> have[N][N];
vector<int> adj[N * N];
int tot;
pair<int, int> where[N * N];

bool go(int x, int y, int d, int dye = -1)
{
    if (x < 0 || x >= n || y < 0 || y >= m) return true;
    if (a[x][y] == '#') return true;
    if (a[x][y] == '-' || a[x][y] == '|') return false;

    if (dye != -1) have[x][y].push_back(dye);
    if (a[x][y] == '/') {
        int nd = d0[d];
        if (go(x + dx[nd], y + dy[nd], nd, dye)) return true;
        return false;
    }
    if (a[x][y] == '\\') {
        int nd = d1[d];
        if (go(x + dx[nd], y + dy[nd], nd, dye)) return true;
        return false;
    }
    if (go(x + dx[d], y + dy[d], d, dye)) return true;
    return false;
}

int cid;
int low[N * N], dfn[N * N], tid;
int belong[N * N];
int stack[N * N], top, instack[N * N];

int tarjan(int u)
{
    low[u] = dfn[u] = tid ++;
    instack[u] = true; stack[++ top] = u;

    for(auto v: adj[u]) {
        if (dfn[v] < 0) {
            low[u] = min(low[u], tarjan(v));
        } else if (instack[v]) {
            low[u] = min(low[u], dfn[v]);
        }
    }

    if (low[u] >= dfn[u]) {
        int v;
        do {
            v = stack[top --];
            instack[v] = false;
            belong[v] = cid;
        } while (v != u);
        cid ++;
    }

    return low[u];
}

void SAT()
{
    tid = 0;
    top = 0;
    cid = 0;

    for(int i = 0; i < tot; ++ i) {
        low[i] = dfn[i] = -1;
        instack[i] = 0;
    }

    for(int i = 0; i < tot; ++ i) {
        if (dfn[i] < 0) {
            tarjan(i);
        }
    } 

    for(int i = 0; i < tot; i += 2) {
        int u = i;
        int v = i + 1;
        if (belong[u] == belong[v]) {
            puts("IMPOSSIBLE");
            return;
        }
        if (belong[u] > belong[v]) u = v;
        int x = where[i / 2].first;
        int y = where[i / 2].second;

        a[x][y] = u % 2 ? '|' : '-';
    }

    puts("POSSIBLE");
    for(int i = 0; i < n; ++ i) {
        puts(a[i]);
    }
}

void solve()
{
    cin >> n >> m;
    for(int i = 0; i < n; ++ i) {
        scanf("%s", a[i]);
        for(int j = 0; j < m; ++ j) have[i][j].clear();
    }
    tot = 0;
    for(int i = 0; i < n; ++ i) {
        for(int j = 0; j < m; ++ j) {
            if (a[i][j] == '-' || a[i][j] == '|') {
                where[tot / 2] = make_pair(i, j);
                int u = tot ++; //-
                adj[u].clear();
                int v = tot ++; //|
                adj[v].clear();

                if (go(i + dx[1], j + dy[1], 1) && go(i + dx[3], j + dy[3], 3)) {
                    go(i + dx[1], j + dy[1], 1, u);
                    go(i + dx[3], j + dy[3], 3, u);
                } else {
                    adj[u].push_back(v);
                }
                if (go(i + dx[2], j + dy[2], 2) && go(i + dx[0], j + dy[0], 0)) {
                    go(i + dx[2], j + dy[2], 2, v);
                    go(i + dx[0], j + dy[0], 0, v);
                } else {
                    adj[v].push_back(u);
                }
            }
        }
    }

    for(int i = 0; i < n; ++ i) {
        for(int j = 0; j < m; ++ j) {
            if (a[i][j] == '.') {
                if (have[i][j].empty()) {
                    puts("IMPOSSIBLE");
                    return;
                }
                if (have[i][j].size() == 1) {
                    int u = have[i][j][0];
                    adj[u ^ 1].push_back(u);
                } else {
                    assert(have[i][j].size() == 2);
                    int u = have[i][j][0];
                    int v = have[i][j][1];
                    adj[u ^ 1].push_back(v);
                    adj[v ^ 1].push_back(u);
                }
            }
        }
    }

    /*
    for(int i = 0; i < tot; ++ i) {
        for(auto j: adj[i]) {
            cout << i << ' ' << j << endl;
        }
    }
    */

    SAT();
}

int main()
{
	freopen("C-small-attempt0.in", "r", stdin); freopen("C-small-attempt0.out", "w", stdout);
	//freopen("C-small-attempt1.in", "r", stdin); freopen("C-small-attempt1.out", "w", stdout);
	//freopen("C-small-attempt2.in", "r", stdin); freopen("C-small-attempt2.out", "w", stdout);
	//freopen("C-large.in", "r", stdin); freopen("C-large.out", "w", stdout);
	int test_case;
	cin >> test_case;
	for(int i = 0; i < test_case; ++ i) {
		printf("Case #%d: ", i + 1);
		cerr << "Start: " << i << endl;
		solve();
	}
	return 0;
}
