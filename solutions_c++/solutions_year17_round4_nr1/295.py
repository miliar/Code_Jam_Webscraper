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
 	freopen("A-large.in", "rb", stdin);
 	freopen("out.txt", "wb", stdout);
	freopen("err.txt", "wb", stderr);
#endif
	int T,N,P,tmp;
	scanf("%d", &T);
	FOR(tc,1,T+1)
	{
		scanf("%d %d", &N, &P);
		vector<int> G(P);
		REP(i, N)
		{
			scanf("%d", &tmp);
			G[tmp%P]++;
		}
		int res = G[0];
		if (P == 2)
		{
			res += G[1] / 2;
			res += G[1] & 1;
		}
		else if (P == 3)
		{
			res += min(G[1], G[2]);
			int tmp = min(G[1], G[2]);
			G[1] -= tmp;
			G[2] -= tmp;
			res += (G[1] + G[2] +2) / 3;
		}
		else if (P == 4)
		{
			res += min(G[1], G[3]);
			int tmp = min(G[1], G[3]);
			G[1] -= tmp;
			G[3] -= tmp;
			res += G[2] / 2;
			G[2] %= 2;
			int rem = max(G[1], G[3]);
			if (G[2] )
			{
				++res;
				rem -= 2;
			}
			if (rem > 0)
			{
				res += (rem + 3) / 4;
			}
		}
		printf("Case #%d: %d\n", tc, res);
	}
	return 0;
}
