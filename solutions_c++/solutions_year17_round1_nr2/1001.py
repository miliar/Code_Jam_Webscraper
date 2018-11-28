//TAG : 
#include<bits/stdc++.h>
using namespace std;
#define rep(i,n)	for(int (i)=0;(i)<(n);(i)++)
#define repd(i,n)	for(int (i)=(n)-1;(i)>=0;(i)--)
#define REP(i,j,n)  for(int (i)=(j),_n=(n); (i) < _n; (i)++)
#define FOR(i,a,b)  for(int _b=(b), (i)=(a); (i) <= _b; (i)++)
#define FORD(i,a,b) for(int i=(a),_b=(b);i>=_b;i--)
#define ALL(c) (c).begin(), (c).end()
#define SORT(c) sort(ALL(c))
#define CLEAR(x) memset((x),0,sizeof(x))
#define REVERSE(c) reverse(ALL(c))
#define UNIQUE(c) SORT(c),(c).resize(unique(ALL(c))-(c).begin())
#define X first
#define Y second
#define MP make_pair
#define MT make_tuple
#define EPS 	(1e-9)
typedef pair<int, int>	pii;
typedef vector<pii>		vii;
typedef vector<int>		vi;
typedef unsigned int	uint;
typedef long long		ll;
typedef unsigned long long	ull;
template<typename T> void check_max(T& a, T b) { if (a < b) a = b; }
template<typename T> void check_min(T& a, T b) { if (a > b) a = b; }
#ifdef _MSC_VER
#include "builtin_gcc_msvc.h"
#define gets	gets_s
#else
#define popcnt(x)	__builtin_popcount(x)
#define ctz(x)		__builtin_ctz(x)
#define clz(x)		__builtin_clz(x)
#define popcntll(x)	__builtin_popcountll(x)
#define ctzll(x)	__builtin_ctzll(x)
#define clzll(x)	__builtin_clzll(x)
#endif

const int MX = 50;
int R[MX], Q[MX][MX];
int lo[MX][MX], hi[MX][MX];
vi g[MX*MX + 2];
bitset<MX*MX + 2> vis;
int par[MX*MX + 2];
int flow[MX*MX + 2][MX*MX + 2];
int main()
{
	int TC;
	scanf("%d", &TC);
	FOR(T, 1, TC)
	{
		int N, P; scanf("%d%d", &N, &P);
		rep(i, N)scanf("%d", &R[i]);
		rep(i, N)rep(j, P) {
			scanf("%d", &Q[i][j]);
			lo[i][j] = (Q[i][j] * 10 + 11 * R[i] - 1) / (11 * R[i]);//ceil
			hi[i][j] = Q[i][j] * 10 / (9 * R[i]);//floor
		}
		rep(i, N*P + 2)g[i].clear();
		CLEAR(flow);
		auto addedge = [&](int u, int v) {
			g[u].push_back(v);
			g[v].push_back(u);
			flow[u][v] = 1;
		};
		int start = 0, end = 1;
		rep(i, N)rep(j, P)if (lo[i][j] <= hi[i][j]) {
			int id = i*P + j + 2;
			if (!i) {
				addedge(start, id);
			} else {
				rep(jj, P) {
					int l = max(lo[i][j], lo[i - 1][jj]);
					int r = min(hi[i][j], hi[i - 1][jj]);
					if (l <= r) {
						int id2 = (i - 1)*P + jj + 2;
						addedge(id2, id);
					}
				}
			}
			if (i + 1 == N) {
				addedge(id, end);
			}
		}
		int max_flow = 0;
		while (true) {
			vis.reset();
			vis[start] = 1;
			queue<int> Q;
			Q.push(start);
			while (!Q.empty()) {
				int u = Q.front(); Q.pop();
				for (int v : g[u])if (!vis[v] && flow[u][v] > 0) {
					vis[v] = 1;
					par[v] = u;
					Q.push(v);
				}
				if (vis[end])break;
			}
			if (!vis[end])break;
			for (int v = end; v != start;) {
				int u = par[v];
				flow[u][v]--;
				flow[v][u]++;
				v = u;
			}
			++max_flow;
		}
		printf("Case #%d: %d\n", T, max_flow);
	}

	return 0;
}