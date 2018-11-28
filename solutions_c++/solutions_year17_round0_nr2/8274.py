/**********************
 #  By lintao [Hudi]  #
 **********************/

#define _MULTI_TC_
// #define _DEBUG_
#ifdef _DEBUG_
	#define DEBUG printf
#else
	#define DEBUG if (0) printf
#endif

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

typedef long long ll;
typedef pair<ll,ll> puu;
typedef pair<int,int> pii;

// =========================================== //
ll power10[20];
// =========================================== //
void prec();
void solve(int);
int main()
{
	prec();
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

void prec()
{
	ll a = 1;
	REP(x,0,19) {
		power10[x] = a;
		a *= 10;
	}
}

int digit(ll n, int idx) {
	DEBUG("%I64d %d %d\n", n, idx, ((n/power10[idx])%10));
	return ((n/power10[idx])%10);
}

void solve(int tc)
{
	ll n;
	scanf("%I64d", &n);

	int idx=0;
	while (idx<18) {
		if (digit(n,idx) < digit(n,idx+1)) {
			int cur = idx;
			while (cur>0  &&  digit(n,cur-1)!=9) --cur;
			n -= power10[cur] * (digit(n,cur)+1);
			idx = cur;
		}
		++idx;
	}

	printf("Case #%d: %I64d\n", tc, n);
}