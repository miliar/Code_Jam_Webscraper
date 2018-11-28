#include <cstdio>
#include <algorithm>
#include <vector>
#include <cstring>
#include <numeric>
#include <cassert>
#include <cmath>
#include <map>
#include <unordered_map>
#include <set>


using namespace std;
typedef unsigned int uint;
typedef long long LL;
typedef vector<int> VI;
typedef vector<LL> VL;
typedef vector<VI> VVI;
typedef vector<VVI> VVVI;
typedef vector<VL> VVL;
typedef pair<int, int> PII;
typedef pair<LL, LL> PLL;
typedef vector<PII > VPII;
typedef vector<VPII> VVPII;

#define FOR(k,a,b) for(int k(a); k < (b); ++k)
#define REP(k,a) for(int k=0; k < (a); ++k)
#define ABS(a) ((a)>0?(a):-(a))
int main(int argc, char** argv) {
#ifdef HOME
	freopen("C-small-attempt0.in", "rb", stdin);
	freopen("C-small-attempt0.out", "wb", stdout);
	freopen("err.txt", "wb", stderr);
#endif
	int T, N, Q;
	scanf("%d", &T);
	FOR(tc,1,T+1)
	{
		scanf("%d %d", &N,&Q);
		vector<pair<int, int> > horses(N);
		vector<vector<int> > dist(N, vector<int>(N));
		REP(i, N)
		{
			scanf("%d %d", &horses[i].first, &horses[i].second);
		}
		REP(i, N)
			REP(j, N)
		{
			scanf("%d", &dist[i][j]);
		}
		vector<vector<double> > th(N, vector<double>(N, 1e18));
		REP(i, N)
		{
			vector<LL> dd(N, -1);
			dd[i] = 0;
			bool update = 1;
			while (update)
			{
				update = 0;
				REP(j, N) REP(k, N)
				{
					if (dd[j] >= 0 && dist[j][k] >= 0 && dd[j] + dist[j][k] <= horses[i].first)
					{
						if (dd[k] == -1 || dd[k] > dd[j] + dist[j][k])
						{
							dd[k] = dd[j] + dist[j][k];
							update = 1;
						}
					}
				}
			}
			REP(j, N) if (dd[j] >= 0)
				th[i][j] = double(dd[j]) / horses[i].second;
		}
		REP(k, N) REP(i, N) REP(j, N)
		{
			th[i][j] = min(th[i][j], th[i][k] + th[k][j]);
		}
		printf("Case #%d: ",tc);
		REP(q, Q)
		{
			int u, v;
			scanf("%d %d", &u, &v);
			--u, --v;
			printf("%.7f ", th[u][v]);
		}
		printf("\n");
	}
	return 0;
}
