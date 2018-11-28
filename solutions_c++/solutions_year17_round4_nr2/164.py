// In the name of God

#include <iostream>
#include <algorithm>
#include <fstream>
#include <vector>
#include <deque>
#include <assert.h>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <stdio.h>
#include <string.h>
#include <utility>
#include <math.h>
#include <bitset>
#include <iomanip>
#include <complex>

using namespace std;

#define rep(i, a, b) for (int i = (a), i##_end_ = (b); i < i##_end_; ++i)
#define debug(...) fprintf(stderr, __VA_ARGS__)
#define mp make_pair
#define x first
#define y second
#define pb push_back
#define SZ(x) (int((x).size()))
#define ALL(x) (x).begin(), (x).end()

template<typename T> inline bool chkmin(T &a, const T &b) { return a > b ? a = b, 1 : 0; }
template<typename T> inline bool chkmax(T &a, const T &b) { return a < b ? a = b, 1 : 0; }
template<typename T> inline bool smin(T &a, const T &b)   { return a > b ? a = b : a;    }
template<typename T> inline bool smax(T &a, const T &b)   { return a < b ? a = b : a;    }

typedef long long LL;
const int oo = (int) 1e9;
	const int max0 = 100000, max1 = 100000;

int q[max0 + 5];
bool vis[max0 + 5];
struct network_flow {
	struct edge
	{
		int id, g, nxt;

		edge() { }
		edge(int _id, int _g, int _nxt): id(_id), g(_g), nxt(_nxt) { }

	};

	int st[max0 + 5], en = 0;
	edge e[max1 + 5];

	inline void add_edge(int x, int y, int z)
	{
		e[en] = edge(y, z, st[x]), st[x] = en++;
	}

	inline void add_biedge(int x, int y, int z) { add_edge(x, y, z), add_edge(y, x, 0); }

	int S, T, N;

	int dis[max0 + 5];
	network_flow() {
		N = S = T = 0;
		memset(st, -1, sizeof st);
	}
	inline bool bfs()
	{
//		cout << " hmm" << endl;
		int head = 0, rear = 0;
		memset(dis, -1, sizeof(dis[0]) * N);
		memset(vis, 0, sizeof(vis[0]) * N);
		vis[q[rear++] = S] = 1;
		dis[S] = 0;
		while (head != rear)
		{
			int x = q[head++];
			for (int i = st[x]; i != -1; i = e[i].nxt)
			{
				if (!e[i].g) continue;
				int y = e[i].id;
				if (!vis[y])
				{
					dis[y] = dis[x] + 1;
					if (y == T) return 1;
					q[rear++] = y;
					vis[y] = 1;
				}
			}
		}
		return 0;
	}

	int cur[max0 + 5];

	inline int dfs(int x, int flow)
	{
		if (x == T) return flow;
		int res = flow;
		for (int &i = cur[x]; i != -1; i = e[i].nxt)
		{
			if (!e[i].g) continue;
			int y = e[i].id;
			if (dis[y] == dis[x] + 1)
			{
				int F = dfs(y, min(e[i].g, res));
				res -= F;
				e[i].g -= F;
				e[i ^ 1].g += F;
				if (res <= 0) return flow;
			}
		}
		dis[x] = -1;
		return flow - res;
	}

	int work()
	{
		if (S == T) return oo;
		int ret = 0;
		for ( ; bfs(); )
		{
			for (int i = 0; i < N; ++i) cur[i] = st[i];
			ret += dfs(S, oo);
		}
		return ret;
	}

};
const int N = 1e5 + 5;
vector<pair<pair<int, int>, int>> ed_add[2];
int n, c, m, got[N], md[N], cnt[N], lead[N];
int check(int lim, int to_check) {
//	cout << " hi " << lim << ' ' << to_check << endl;
	network_flow cur;
	cur.S = cur.N++;
	cur.T = cur.N++;
	for (int j = 0; j < n; ++j) {
		lead[j] = cur.N++;
		md[j] = cur.N++;
		if (j >= 1) cur.add_biedge(md[j], md[j - 1], oo);
		cur.add_biedge(lead[j], cur.T, lim);
		cur.add_biedge(md[j], lead[j], oo);
	}
	for (int j = 0; j < n; ++j) {
		int num = got[j];
		int nw = cur.N++;
		cur.add_biedge(cur.S, nw, num);
		cur.add_biedge(nw, lead[j], num);
		if (to_check) {
			cur.add_biedge(nw, md[j], num);
		}
	}
//	cout << " end " << endl;
	return cur.work();	
}
int main() {
	int tc;
	cin >> tc;
	for (int tt = 1; tt <= tc; ++tt) {
		cout << "Case #" << tt << ": ";
		cin >> n >> c >> m;
		for (int j = 0; j < n; ++j) got[j] = 0;
		for (int j = 0; j < 2; ++j) ed_add[j].clear();
		for (int j = 0; j < c; ++j) cnt[j] = 0;
		for (int j = 0; j < m; ++j) {
			int pos, own;
			cin >> pos >> own;
			--pos;
			--own;
			++got[pos];
			++cnt[own];
		}
		int bl = 0, br = m + 1;
		for (int j = 0; j < c; ++j) bl = max(bl, cnt[j]);
		--bl;
		while (bl < br - 1) {
			int bm = bl + br >> 1;
			if (check(bm, 1) == m) {
				br = bm;
			} else {
				bl = bm;
			}
		}
		cout << br << ' ' << m - check(br, 0) << endl;
	}
}

















