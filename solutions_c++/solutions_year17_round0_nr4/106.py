#define _CRT_SECURE_NO_WARNINGS
#pragma comment(linker, "/STACK:10034217728")
#include <iostream>
#include <cstdio>
#include <vector>
#include <set>
#include <map>
#include <algorithm>
#include <cassert>
#include <utility>
#include <ctime>
#include <string>
#include <sstream>
#include <queue>
#include <cstring>
#include <cmath>

using namespace std;
typedef long long ll;
typedef long double ld;
#define ZERO(x) memset((x), 0, sizeof(x))
#define NEGATE(x) memset((x), 255, sizeof(x))
#define mp make_pair
#define mt(a, b, c) mp(a, mp(b, c))

map<pair<int, int>, int> M;

struct edge
{
	int to;
	int rev;
	int cap;
	int flow;
	edge(int _to, int _rev, int _cap, int _flow)
	{
		to = _to;
		rev = _rev;
		cap = _cap;
		flow = _flow;
	}
};

const int N = 920;
int s = N - 2, t = N - 1;

vector<edge> e[N];
int ptr[N];
bool was[N];
int dist[N];
vector<int> marked;

const int inf = 1e9;

void add_edge(int from, int to, int cap)
{
	if (marked[from] || marked[to]) return;
	e[from].push_back(edge(to, e[to].size(), cap, 0));
	M[mp(from, to)] = (int)e[from].size() - 1;
	e[to].push_back(edge(from, e[from].size() - 1, 0, 0));
}

bool bfs()
{
	ZERO(was);
	fill(dist, dist + N, inf);
	queue<int> q;
	q.push(s);
	was[s] = 1;
	dist[s] = 0;
	while (!q.empty())
	{
		int v = q.front();
		q.pop();
		for (int i = 0; i < e[v].size(); i++)
		{
			if (e[v][i].flow == e[v][i].cap) continue;
			int to = e[v][i].to;
			if (was[to]) continue;
			q.push(to);
			was[to] = 1;
			dist[to] = dist[v] + 1;
		}
	}
	return dist[t] < inf;
}

int dfs(int v, int push)
{
	if (push == 0)
		return 0;
	if (v == t)
		return push;
	for (int &i = ptr[v]; i < e[v].size(); i++)
	{
		edge& k = e[v][i];
		if (dist[v] + 1 != dist[k.to]) continue;
		if (k.cap == k.flow) continue;

		int p = dfs(k.to, min(push, -k.flow + k.cap));

		if (p > 0)
		{
			k.flow += p;
			e[k.to][k.rev].flow -= p;
			return p;
		}
	}
	return 0;
}

int dinic()
{
	int res = 0;
	while (bfs())
	{
		ZERO(ptr);
		int pushed = 0;
		while ((pushed = dfs(s, inf)) > 0)
			res += pushed;
	}
	return res;
}

vector<string> v;

enum VERTEX_TYPE {
	ROW,
	COLUMN,
	DIAGPLUS,
	DIAGMINUS
};

int n;

int get_vertex(int val, VERTEX_TYPE vt) {
	if (vt == ROW) {
		// 0 <= val < n
		return val;
	}
	if (vt == COLUMN) {
		// 0 <= val < n
		return val + n;
	}
	if (vt == DIAGPLUS) {
		// 0 <= val < 2 * n
		return val + n + n;
	}
	if (vt == DIAGMINUS) {
		// -n < val < n
		return val + n + n + 2 * n + n + 5;
	}
}

bool filled(int v_from, int v_to) {
	if (!M.count(mp(v_from, v_to))) return 0;
	edge& k = e[v_from][M[mp(v_from, v_to)]];
	return k.cap == k.flow;
}

struct D {
	int r, c;
	char s;
};

void check(vector<string> v) {
	vector<char> was_row(n, 0);
	vector<char> was_col(n, 0);
	set<int> diag_plus, diag_minus;
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			if (v[i][j] == 'x' || v[i][j] == 'o') {
				if (!(!was_row[i] && !was_col[j])) {
					assert(false);
				}
				was_row[i] = 1;
				was_col[j] = 1;
			}
			if (v[i][j] == '+' || v[i][j] == 'o') {
				assert(!diag_plus.count(i + j) && !diag_minus.count(i - j));
				diag_plus.insert(i + j);
				diag_minus.insert(i - j);
			}
		}
	}
}

int main()
{
#ifdef XXX
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif

	int T;
	cin >> T;
	for (int q = 0; q < T; q++) {
		for (int i = 0; i < N; i++) e[i].clear();
		M.clear();
		cin >> n;
		int m;
		cin >> m;
		marked.assign(N, 0);
		v.resize(n);
		for (int i = 0; i < n; i++) {
			v[i].assign(n, '.');
		}
		for (int i = 0; i < m; i++) {
			char d;
			cin >> d;
			int r, c;
			cin >> r >> c;
			r--, c--;
			v[r][c] = d;
		}
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < n; j++) {
				int from = get_vertex(i, ROW);
				int to = get_vertex(j, COLUMN);
				int cap = 1;
				if (v[i][j] == 'o' || v[i][j] == 'x') {
					cap = 0;
					marked[from] = marked[to] = 1;
				}
				add_edge(from, to, cap);
				from = get_vertex(i + j, DIAGPLUS);
				to = get_vertex(i - j, DIAGMINUS);
				cap = 1;
				if (v[i][j] == 'o' || v[i][j] == '+') {
					cap = 0;
					marked[from] = marked[to] = 1;
				}
				add_edge(from, to, cap);
			}
		}
		for (int i = 0; i < n; i++) {
			int from = s;
			int to = get_vertex(i, ROW);
			add_edge(from, to, 1);
			from = get_vertex(i, COLUMN);
			to = t;
			add_edge(from, to, 1);
		}
		for (int i = 0; i <= 2 * n; i++) {
			int from = s;
			int to = get_vertex(i, DIAGPLUS);
			add_edge(from, to, 1);
		}
		for (int i = -n; i <= n; i++) {
			int from = get_vertex(i, DIAGMINUS);
			int to = t;
			add_edge(from, to, 1);
		}
		dinic();
		vector<string> h = v;
		int score = 0;
		vector<D> ans;
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < n; j++) {
				int from = get_vertex(i, ROW);
				int to = get_vertex(j, COLUMN);
				char c = v[i][j];
				if (filled(from, to) && c != 'o') {
					if (c == '+') c = 'o';
					else c = 'x';
				}
				from = get_vertex(i + j, DIAGPLUS);
				to = get_vertex(i - j, DIAGMINUS);
				if (filled(from, to) && c != 'o') {
					if (c == '.') c = '+';
					else c = 'o';
				}
				h[i][j] = c;
				if (h[i][j] != v[i][j]) {
					ans.push_back({ i, j, c });
				}
				if (c != '.') score++;
				if (c == 'o') score++;
			}
		}
		//check(h);
		printf("Case #%d: ", q + 1);
		printf("%d %d\n", score, (int)ans.size());
		for (auto el : ans) {
			cout << el.s << " " << el.r + 1 << " " << el.c + 1 << "\n";
		}
	}

	return 0;
}