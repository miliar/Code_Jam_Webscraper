/**********************
 #  By lintao [Hudi]  #
 **********************/

#include <bits/stdc++.h>
using namespace std;

// =========================================== //
#define _MULTI_TC_
// =========================================== //

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
void solve(int);
int main()
{
#ifdef _MULTI_TC_
	int TC;
	scanf("%d", &TC);
	REP(tc,1,TC+1) solve(tc);
#else
	solve(0);
#endif
	return 0;
}
// =========================================== //

void solve(int tc)
{
	char s[1024];
	int k, len, ans=0;
	scanf("%s%d", s, &k);

	len = strlen(s);
	REP(x,0,len-k+1) if (s[x] == '-') {
		REP(y,0,k) s[x+y] = (s[x+y]=='+' ? '-' : '+');
		++ans;
	}

	REP(x,0,len) if (s[x] == '-') {
		ans = -1;
		break;
	}

	printf("Case #%d: ", tc);
	if (ans == -1) printf("IMPOSSIBLE\n");
	else printf("%d\n", ans);
}