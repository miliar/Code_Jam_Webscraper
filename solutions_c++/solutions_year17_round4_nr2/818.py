#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>
#include <cstdio>
#include <cstring>
#include <string>
#include <set>
#include <map>
#include <queue>
#include <list>
#include <unordered_map>
#include <unordered_set>

#define pb push_back
#define mp make_pair

using namespace std;
using big = long long;

const int MOD = 1000000007;

const int inf = 0x3f3f3f3f;
using pii = pair<int, int>;


int n, C, m;

const int N = 1020, V = N * 8, E = V * V;

vector<pii> a;

int head[V], v[E], w[E], c[E], nxt[E], t;
int q[V], S, T, dis[V];
bool in[V];
bool vis[V];

inline void add(int x, int y, int z, int ww) {
	nxt[++t] = head[x];
	v[t] = y;
	c[t] = z;
	w[t] = ww;
	head[x] = t;
	nxt[++t] = head[y];
	v[t] = x;
	c[t] = 0;
	w[t] = -ww;
	head[y] = t;
}

bool spfa() {
	int h, tail;
	memset(dis, inf, sizeof(dis));
	in[q[h = tail = 1] = S] = true;
	dis[S] = 0;
	while (h <= tail) {
		int s = q[h++];
		in[s] = false;
		for (int i = head[s]; i; i = nxt[i]) {
			if (c[i] && dis[v[i]] > dis[s] + w[i]) {
				dis[v[i]] = dis[s] + w[i];
				if (!in[v[i]]) {
					in[q[++tail] = v[i]] = true;
				}
			}
		}
	}
	return dis[T] < inf;
}

int aug(int x, int sum) {
	if (x == T) {
		return sum;
	}
	int os = sum;
	vis[x] = true;
	for (int i = head[x]; i && sum; i = nxt[i]) {
		if (!vis[v[i]] && c[i] && dis[v[i]] == dis[x] + w[i]) {
			int tmp = aug(v[i], min(c[i], sum));
			sum -= tmp;
			c[i] -= tmp;
			c[i ^ 1] += tmp;
		}
	}
	if (os == sum) {
		dis[x] = -1;
	}
	return os - sum;
}

pair<bool, int> ck(int rides) {
	memset(head, 0, sizeof(head));
	t = 1;
	S = 0;
	T = C + n + 1;
	for (int i = 1; i <= C; ++i) {
		add(S, i, rides, 0);
	}
	for (const auto &p : a) {
		add(p.second, p.first + C, 1, 0);
	}
	for (int i = 1; i <= n; ++i) {
		add(i + C, T, rides, 0);
	}
	for (int i = 1; i <= n; ++i) {
		for (int j = 1; j < i; ++j) {
			add(C + i, C + j, inf, 1);
		}
	}
	int flow = 0, cost = 0;
	while (true) {
		if (!spfa()) {
			break;
		}
		memset(vis, false, sizeof(vis));
		int k = aug(S, inf);
		flow += k;
		cost += k * dis[T];
	}
//	cerr << flow << " " << m << " " << a.size() << endl;
	return {flow == m, cost};
}

pair<int, int> solve() {
	int s = 1, e = m;
	while (s <= e) {
		int mid = (s + e) >> 1;
		auto tmp = ck(mid);
		if (tmp.first) {
			e = mid - 1;
		} else {
			s = mid + 1;
		}
	}
	auto tmp = ck(s);
	return {s, tmp.second};
}

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int cas;
	scanf("%d", &cas);
	for (int cass = 1; cass <= cas; ++cass) {
		printf("Case #%d: ", cass);
		a.clear();
		cerr << "Case " << cass << endl;
		scanf("%d%d%d", &n, &C, &m);
		for (int i = 0; i < m; ++i) {
			int x, y;
			scanf("%d%d", &x, &y);
			a.emplace_back(x, y);
		}
//		cerr << a.size() << " ! " << m << endl;
//		sort(a.begin(), a.end());
		auto tmp = solve();
		printf("%d %d\n", tmp.first, tmp.second);
	}
}
