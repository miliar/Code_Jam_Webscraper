/**********************
 #  By lintao [Hudi]  #
 **********************/

#define _MULTI_TC_

// =========================================== //
//    
// =========================================== //
#include <bits/stdc++.h>
using namespace std;

#define INIT(c,v) memset(c,v,sizeof(c))
#define REP(a,b,c) for (int a=b, _c=c; a<_c; ++a)
#define RED(a,b,c) for (int a=b, _c=c; a>=_c; --a)

#define PB push_back
#define MP make_pair
#define fi first
#define sc second

#define EPS 1e-8

typedef long long ll;
typedef pair<ll,ll> puu;
typedef pair<int,int> pii;

// =========================================== //
void solve(int);
int main()
{
#ifdef _MULTI_TC_
	int TC;
	scanf("%d", &TC);
	REP(tc,1,TC+1) solve(tc);
#else
	solve(-1);
#endif
	return 0;
}
// =========================================== //

bool isLT(pii a, pii b) {
	return ((ll)a.fi * (ll)b.sc < (ll)b.fi * (ll)a.sc);
}

void solve(int tc)
{
	int D, N, K, S;
	pii waktuKuda;
	pii jikanKakaru = MP(0,1000000000);
	scanf("%d%d", &D, &N);
	REP(x,0,N) {
		scanf("%d%d", &K, &S);
		waktuKuda = MP(D-K, S);
		if (isLT(jikanKakaru, waktuKuda)) {
			jikanKakaru = waktuKuda;
		}
	}
	// printf("%d %d\n", jikanKakaru);
	printf("Case #%d: %.6f\n", tc, ((ll)D*(ll)jikanKakaru.sc)/(double)jikanKakaru.fi);
}