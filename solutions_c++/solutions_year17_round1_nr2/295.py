#include <bits/stdc++.h>
#define REP(i, a, b) for (int i = a; i <= b; ++i)
#define PER(i, a, b) for (int i = a; i >= b; --i)
#define RVC(i, S) for (int i = 0; i < S.size(); ++i)
#define mp make_pair
#define pb push_back
#define fi first
#define se second
#define debug(...) fprintf(stderr, __VA_ARGS__)
using namespace std;

typedef pair<int, int> pii;
typedef vector<int> VI;
typedef long long LL;

inline int read(){
	int x = 0, ch = getchar(), f = 1;
	while (!isdigit(ch)){if (ch == '-') f = -1; ch = getchar();}
	while (isdigit(ch)) x = x * 10 + ch - '0', ch = getchar();
	return x * f;
}

const int N = 55;
int n, m, need[N], Q[N][N];
int lb[N][N], rb[N][N], in[N][N], out[N][N], idx;

const int M = 100005, INF = 0x3f3f3f3f;

struct Edge{int to, c, nxt; };

namespace Network{
	int m, s, t, fr[N * N], vis[N * N], cur[N * N], d[N * N];
	Edge E[M];
	void init(){
		m = 0;
		memset(fr, -1, sizeof fr);
	}
	inline void addedge(int x, int y, int c){
		// debug("link %d %d\n", x, y);
		E[m++] = (Edge){y, c, fr[x]}; fr[x] = m - 1;
		E[m++] = (Edge){x, 0, fr[y]}; fr[y] = m - 1;
	}
	int bfs(){
		queue<int> q;
		memset(vis, 0, sizeof vis);
		memcpy(cur, fr, sizeof cur);
		d[s] = 0; vis[s] = 1;
		q.push(s);
		while (!q.empty()){
			int h = q.front(); q.pop();
			for (int i = fr[h]; i != -1; i = E[i].nxt)
				if (E[i].c && !vis[E[i].to]){
					vis[E[i].to] = 1;
					d[E[i].to] = d[h] + 1;
					q.push(E[i].to);
				}
		}
		return vis[t];
	}
	int dfs(int x, int a){
		if (x == t || a == 0) return a;
		int fl = 0, f;
		for (int &i = cur[x]; i != -1; i = E[i].nxt)
			if (d[E[i].to] == d[x] + 1 && (f = dfs(E[i].to, min(a, E[i].c))) > 0){
				E[i].c -= f; E[i ^ 1].c += f;
				fl += f; a -= f;
				if (!a) break;
			}
		return fl;
	}
	int maxflow(int _s, int _t){
		s = _s; t = _t;
		int fl = 0;
		while (bfs()) fl += dfs(s, INF);
		return fl;
	}
}

void solve(){
	n = read(), m = read();
	REP(i, 1, n) need[i] = read();
	idx = 0;
	REP(i, 1, n) REP(j, 1, m){
		Q[i][j] = read();
		in[i][j] = ++idx;
		out[i][j] = ++idx;
	}
	REP(i, 1, n) REP(j, 1, m){
		double r = (double)Q[i][j] / 0.9 / need[i];
		double l = (double)Q[i][j] / 1.1 / need[i];
		// 0.9 * k * need[i] <= Q[i][j] <= 1.1 * k * need[i]
		// l <= k <= r
		lb[i][j] = (int)ceil(l);
		rb[i][j] = (int)floor(r);
		if (lb[i][j] > rb[i][j]){
			lb[i][j] = rb[i][j] = 0;
		}
		// debug("%d, %d: %.2lf, %.2lf\n", i, j, l, r);
		// debug("%d, %d: [%d, %d]\n", i, j, lb[i][j], rb[i][j]);
	}
	Network::init();
	int S = 0, T = 2 * n * m + 1;
	REP(i, 1, n) REP(j, 1, m){
		Network::addedge(in[i][j], out[i][j], 1);
	}
	REP(i, 1, m){
		if (rb[1][i] > 0){
			Network::addedge(S, in[1][i], 1);
		}
	}
	REP(i, 1, n - 1) REP(j, 1, m) REP(k, 1, m){
		if (max(lb[i][j], lb[i + 1][k])
			<= min(rb[i][j], rb[i + 1][k])
			&& min(rb[i][j], rb[i + 1][k]) > 0){
			// debug("%d %d  to  %d %d\n", i, j, i + 1, k);
			Network::addedge(out[i][j], in[i + 1][k], 1);
		}
	}
	REP(i, 1, m) if (rb[n][i] > 0)
		Network::addedge(out[n][i], T, 1);
	printf("%d\n", Network::maxflow(S, T));
}

int main(){
	int T = read();
	REP(kas, 1, T){
		printf("Case #%d: ", kas);
		solve();
	}
	return 0;
}