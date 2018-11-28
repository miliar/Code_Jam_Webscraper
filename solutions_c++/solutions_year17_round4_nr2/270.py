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

int calc(int K, int N, int M, int C, const vector<int>& P, const vector<int>& B, const vector<int> u)
{
	int db = 0;
	int res = 0;
	REP(i, N)
	{
		db += u[i];
		res += max(u[i] - K,0);
		if (db > (i + 1)*K)
			return -1;
	}
	return res;
}

int main(int argc, char** argv) {
#ifdef HOME
 	freopen("B-large.in", "rb", stdin);
 	freopen("out.txt", "wb", stdout);
	freopen("err.txt", "wb", stderr);
#endif
	int T,N,M,C;
	scanf("%d", &T);
	FOR(tc,1,T+1)
	{
		scanf("%d %d %d", &N, &C, &M);
		vector<int> P(M), B(M);
		vector<vector<int> > w(C,vector<int> (N));
		vector<int> v(C);
		vector<int> u(N);
		int mi = 0;
		REP(i, M)
		{
			scanf("%d %d", &P[i], &B[i]);
			w[B[i] - 1][P[i] - 1]++;
			v[B[i] - 1]++;
			u[P[i] - 1]++;
			mi = max(mi, v[B[i] - 1]);
		}
		int res = 0;
		while (1)
		{
			res = calc(mi,N,M,C,P,B,u);
			if(res>=0) 
				break;
			++mi;
		}
		printf("Case #%d: %d %d\n", tc, mi, res);
	}
	return 0;
}
