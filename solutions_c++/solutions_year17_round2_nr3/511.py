//TAG : 
#include<bits/stdc++.h>
using namespace std;
#define rep(i,n)	for(int (i)=0;(i)<(n);(i)++)
#define repd(i,n)	for(int (i)=(n)-1;(i)>=0;(i)--)
#define REP(i,j,n)  for(int (i)=(j),_n=(n);(i)<_n;(i)++)
#define FOR(i,a,b)  for(int _b=(b),(i)=(a);(i)<=_b;(i)++)
#define FORD(i,a,b) for(int i=(a),_b=(b);i>=_b;i--)
#define ALL(c) (c).begin(),(c).end()
#define SORT(c) sort(ALL(c))
#define CLEAR(x) memset((x),0,sizeof(x))
#define ff first
#define ss second
#define MP make_pair
#define EPS 	(1e-9)
typedef pair<int, int>	pii;
typedef vector<pii>	vii;
typedef vector<int>	vi;
typedef long long		ll;
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

const int MX = 100;
const ll INF = 1e18;
double dist[MX];
ll E[MX], S[MX], D[MX][MX];
bitset<MX> vis;
int main()
{
	int TC;
	scanf("%d", &TC);
	FOR(T, 1, TC)
	{
		int N, Q; scanf("%d%d", &N, &Q);
		rep(i, N)scanf("%lld%lld", &E[i], &S[i]);
		rep(i, N)rep(j, N) {
			scanf("%lld", &D[i][j]);
			if (D[i][j] == -1)D[i][j] = INF;
		}
		rep(k, N)rep(i, N)rep(j, N)
			check_min(D[i][j], D[i][k] + D[k][j]);
		printf("Case #%d:", T);
		while (Q-- > 0) {
			int s, t; scanf("%d%d", &s, &t);
			--s, --t;
			fill(dist, dist + N, 1e300);
			dist[s] = 0;
			priority_queue<pair<double, int>> Q;
			Q.push(MP(-0, -s));
			vis.reset();
			while (!Q.empty()) {
				double d = -Q.top().ff;
				int u = -Q.top().ss;
				Q.pop();
				if (vis[u])continue;
				vis[u] = 1;
				rep(v, N)if (!vis[v] && D[u][v] <= E[u]) {
					double d = dist[u] + (double)D[u][v] / S[u];
					if (d < dist[v])
						dist[v] = d, Q.push(MP(-d, -v));
				}
			}
			printf(" %.8lf", dist[t]);
		}
		puts("");
	}

	return 0;
}