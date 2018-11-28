#include <bits/stdc++.h>

using namespace std;

const int N = (int)12300;
const int inf = (int)1e9 + 10;

int cases;

struct edge {
	int a, b, cap, flow;
};

int s, t, d[N], ptr[N], q[N];
vector<edge> e;
vector<int> g[111001];

int n, p;
int r[N], qq[N][N];

int res;

void add_edge (int a, int b, int cap) {
	edge e1 = { a, b, cap, 0 };
	edge e2 = { b, a, 0, 0 };
	g[a].push_back ((int) e.size());
	e.push_back (e1);
	g[b].push_back ((int) e.size());
	e.push_back (e2);
}

bool bfs() {
	int qh=0, qt=0;
	q[qt++] = s;
	memset (d, -1, (n + 2) * (p + 2) * sizeof d[0]);
	d[s] = 0;
	while (qh < qt && d[t] == -1) {
		int v = q[qh++];
		for (size_t i=0; i<g[v].size(); ++i) {
			int id = g[v][i],
				to = e[id].b;
			if (d[to] == -1 && e[id].flow < e[id].cap) {
				q[qt++] = to;
				d[to] = d[v] + 1;
			}
		}
	}
	return d[t] != -1;
}

int dfs (int v, int flow) {
	if (!flow)  return 0;
	if (v == t)  return flow;
	for (; ptr[v]<(int)g[v].size(); ++ptr[v]) {
		int id = g[v][ptr[v]],
			to = e[id].b;
		if (d[to] != d[v] + 1)  continue;
		int pushed = dfs (to, min (flow, e[id].cap - e[id].flow));
		if (pushed) {
			e[id].flow += pushed;
			e[id^1].flow -= pushed;
			return pushed;
		}
	}
	return 0;
}

int dinic() {
	int flow = 0;
	for (;;) {
		if (!bfs())  break;
		memset (ptr, 0, (n + 2) * (p + 2) * sizeof ptr[0]);
		while (int pushed = dfs (s, inf))
			flow += pushed;
	}
	return flow;
}




void read_input() {
    cin >> n >> p;
    for (int i = 0; i < n; ++i) cin >> r[i];
    for (int i = 0; i < n; ++i)
        for (int j = 0; j < p; ++j)
            cin >> qq[i][j];
}

bool check(int i, int j, int k) {
    return (9LL * k * r[i] <= 10LL * qq[i][j] && 10LL * qq[i][j] <= 11LL * k * r[i]);
}

int getCntMin(int i, int j) {
    int k = (10LL * qq[i][j]) / (11LL * r[i]);
    for (int d = -3; d <= 3; ++d) {
        int kk = max(0, k + d);
        if (check(i, j, kk)) return kk;
    }
    return -1;
}

int getCntMax(int i, int j) {
    int k = (10LL * qq[i][j]) / (9LL * r[i]);
    for (int d = -3; d <= 3; ++d) {
        int kk = max(0, k - d);
        if (check(i, j, kk)) return kk;
    }
    return -1;
}

void solve() {
    for (int i = 1; i < n; ++i) {
        for (int j = 0; j < p; ++j) {
            int cnt_prev_min = getCntMin(i - 1, j);
            int cnt_prev_max = getCntMax(i - 1, j);
            if (cnt_prev_min == -1) continue;
            for (int jj = 0; jj < p; ++jj) {
                int cnt_cur_min = getCntMin(i, jj);
                int cnt_cur_max = getCntMax(i, jj);
                if (cnt_cur_min == -1) continue;
                if (cnt_prev_max < cnt_cur_min) continue;
                if (cnt_cur_max < cnt_prev_min) continue;
                add_edge((i - 1) * p + j + 1, i * p + jj + 1, 1);
            }
        }
    }
    for (int j = 0; j < p; ++j) {
        int cnt1 = getCntMin(n - 1, j);
        if (cnt1 != -1)
            add_edge(p * (n - 1) + j + 1, p * n + 2, 1);
        int cnt2 = getCntMin(0, j);
        if (cnt2 != -1)
            add_edge(0, j + 1, 1);
    }
    s = 0;
    t = n * p + 2;
    res = dinic();
}


void write_output(int test) {
    cout << "Case #" << test << ": " << res << endl;
}

void clear_data() {
    for (int i = 0; i < (n + 2) * (p + 2); ++i) g[i].clear();
    e.clear();
    for (int i = 0; i < (n + 2) * (p + 2); ++i) d[i] = ptr[i] = q[i] = 0;
}

int main() {
    ios_base::sync_with_stdio(false);

    freopen("B-large.in", "r", stdin);
    freopen("B-large.out", "w", stdout);

    cin >> cases;
    for (int test = 1; test <= cases; ++test) {
        read_input();
        solve();
        write_output(test);
        clear_data();
    }
    return 0;
}
