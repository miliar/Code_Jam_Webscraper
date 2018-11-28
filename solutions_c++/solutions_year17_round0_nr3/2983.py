#include <cstdio>
#include <algorithm>
#include <vector>
#include <cstring>
#include <numeric>
#include <cassert>
#include <cmath>
#include <map>
#include <set>
#include <iostream>
#include <ctime>

using namespace std;

#define FOR(k,a,b) for(int k(a); k < (b); ++k)
#define REP(k,a) for(int k=0; k < (a); ++k)
#define ABS(a) ((a)>0?(a):-(a))
#define EPS 1e-9
typedef long long LL;
const LL MOD = 1e9 + 7;
const int INF = 1e9 + 1;

int main(int argc, char** argv) {
#ifdef HOME
	freopen("C-large.in", "rb", stdin);
	freopen("C-large.out", "wb", stdout);
#endif
	int T;
	scanf("%d", &T);
	FOR(tc, 1, T + 1)
	{
		LL N,K;
		scanf("%lld %lld", &N,&K);
		map<LL, LL> m;//hole size, cnt
		m[N] = 1;
		while (K)
		{
			//get the largest hole and drop it
			LL holesize = m.rbegin()->first - 1;
			LL cnt = m.rbegin()->second;
			if(cnt>=K) break;
			m.erase(holesize + 1);
			m[holesize / 2] += cnt;
			m[(holesize + 1) / 2] += cnt;
			K -= cnt;
		}
		LL holesize = m.rbegin()->first - 1;
		LL large = (holesize + 1) / 2;
		LL smal = holesize / 2;
		printf("Case #%d: %lld %lld\n",tc, large, smal);
	}
	
	return 0;
}
