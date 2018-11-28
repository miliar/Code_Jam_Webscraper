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
	freopen("A-large.in", "rb", stdin);
	freopen("A-large.out", "wb", stdout);
	freopen("err.txt", "wb", stderr);
#endif
	int T,D,N,K,M;
	scanf("%d", &T);
	FOR(tc, 1, T + 1)
	{
		scanf("%d %d", &D, &N);
		double res = 0;
		REP(i, N)
		{
			scanf("%d %d", &K, &M);
			double dist = D - K;
			if (dist > 0)
			{
				dist /= M;
				res = max(res, dist);
			}
		}
		res = D / res;
		printf("Case #%d: %.7f\n", tc, res);
	}
	return 0;
}
