//Template
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <algorithm>
#include <climits>
#include <cmath>
#include <utility>
#include <set>
#include <map>
#include <queue>
#include <ios>
#include <iomanip>
#include <ctime>
#include <numeric>
#include <functional>
#include <fstream>
#include <string>
#include <vector>
#include <bitset>
#include <cstdarg>
#include <complex>
using namespace std;

typedef long long ll;
typedef unsigned int uint;
typedef unsigned long long ull;
typedef long double ld;
#define pair(x, y) make_pair(x, y)
#define runtime() ((double)clock() / CLOCKS_PER_SEC)

inline int read() {
	static int r, sign;
	static char c;
	r = 0, sign = 1;
	do c = getchar(); while (c != '-' && (c < '0' || c > '9'));
	if (c == '-') sign = -1, c = getchar();
	while (c >= '0' && c <= '9') r = r * 10 + (int)(c - '0'), c = getchar();
	return sign * r;
}

template <typename T>
inline void print(T *a, int n) {
	for (int i = 1; i < n; ++i) cout << a[i] << " ";
	cout << a[n] << endl;
}
#define PRINT(_l, _r, _s, _t) { cout << #_l #_s "~" #_t #_r ": "; for (int _i = _s; _i != _t; ++_i) cout << _l _i _r << " "; cout << endl; }

#define NODE 10000
#define EDGE 20000000
#define INFI 12345678

struct edge {
	int next, node, w, c;
} e[EDGE << 1 | 1];
int head[NODE + 1], tot = 1, d[NODE + 1], f[NODE + 1], q[NODE + 1], S, T;
bool inq[NODE + 1];

inline void addedge(int a, int b, int w, int c) {
	e[++tot].next = head[a];
	head[a] = tot, e[tot].node = b, e[tot].w = w, e[tot].c = c;
	e[++tot].next = head[b];
	head[b] = tot, e[tot].node = a, e[tot].w = 0, e[tot].c = -c;
	// cout << a << " " << b << " " << w << " " << c << endl;
	// cout << a << "->" << b << "[label=\"" << w << ", " << c << "\"]" << endl;
}

inline int inc(int &x) {
	return x = x + 1 == T ? 0 : x + 1;
}

bool SPFA(int S, int T) {
	int h = 0, t = 0;
	for (int i = S; i <= T; ++i) d[i] = INFI;
	q[inc(t)] = S, inq[S] = true, d[S] = 0;
	while (h != t) {
		int cur = q[inc(h)];
		inq[cur] = false;
		for (int i = head[cur]; i; i = e[i].next) {
			if (!e[i].w) continue;
			int node = e[i].node;
			if (d[node] > d[cur] + e[i].c) {
				d[node] = d[cur] + e[i].c;
				f[node] = i;
				if (!inq[node])
					inq[node] = true, q[inc(t)] = node;
			}
		}
	}
	return d[T] != INFI;
}

inline pair<int, int> costFlow(int S, int T) {
	int w, ret = 0, flow = 0;
	while (SPFA(S, T)) {
		w = INFI;
		for (int x = T; x != S; x = e[f[x] ^ 1].node)
			w = min(w, e[f[x]].w);
		for (int x = T; x != S; x = e[f[x] ^ 1].node)
			e[f[x]].w -= w, e[f[x] ^ 1].w += w;
		ret += w * d[T];
		flow += w;
	}
	return make_pair(ret, flow);
}

const int N = 1000;
int Case = 0;

int n, m, c;
pair<int, int> ticket[N + 1];

inline int check(int times) {
	memset(head, 0, sizeof head);
	tot = 1;
	for (int i = 1; i <= times; ++i)
		addedge(S, i, n, 0);
	for (int i = 1; i <= times; ++i)
		for (int j = 1; j <= c; ++j)
			addedge(i, times + j, 1, 0);
	for (int i = 1; i <= c; ++i)
		for (int j = 1; j <= m; ++j)
			if (ticket[j].second == i)
				addedge(times + i, times + c + j, 1, 0);
	for (int i = 1; i <= m; ++i) {
		addedge(times + c + i, times + c + m + ticket[i].first, 1, 0);
		if (ticket[i].first > 1)
			addedge(times + c + i, times + c + m + n + ticket[i].first - 1, 1, 1);
	}
	T = times + c + m + 2 * n + 1;
	for (int i = 1; i <= n; ++i)
		addedge(times + c + m + i, T, times, 0);
	for (int i = 1; i <= n; ++i)
		addedge(times + c + m + n + i, times + c + m + i, INFI, 0);
	for (int i = 2; i <= n; ++i)
		addedge(times + c + m + n + i, times + c + m + n + i - 1, INFI, 0);
	int cost, flow;
	tie(cost, flow) = costFlow(S, T);
	// cout << endl;
	if (flow >= m) return cost;
	return -1;
}

int main(int argc, char *argv[]) {
#ifdef KANARI
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif

	int T;
	cin >> T;
	while (T--) {
		cin >> n >> c >> m;
		for (int i = 1; i <= m; ++i) {
			int x, y;
			cin >> x >> y;
			ticket[i] = make_pair(x, y);
		}

		int l = 1, r = m;
		while (l < r) {
			int mid = (l + r) >> 1;
			int val = check(mid);
			if (val != -1) r = mid;
			else l = mid + 1;
		}
		int ans = l, val = check(ans);
		cout << "Case #" << ++Case << ": " << ans << " " << val << endl;
		cerr << Case << endl;
	}

	fclose(stdin);
	fclose(stdout);
	return 0;
}
