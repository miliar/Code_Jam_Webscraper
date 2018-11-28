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

int N;
int ccc[6];

void solve(int tc)
{
	INIT(ccc,0);
	scanf("%d", &N);
	REP(x,0,6) scanf("%d", &ccc[x]);

	pair<int,char> c[3] = {MP(ccc[0],'R'), MP(ccc[2],'Y'), MP(ccc[4],'B')};
	sort(c,c+3);

	// REP(x,0,3) printf(" %d %c,", c[x].fi, c[x].sc); printf("\n");

	if (c[2].fi > c[1].fi + c[0].fi) {
		printf("Case #%d: IMPOSSIBLE\n", tc);
		return;
	}

	printf("Case #%d: ", tc);
	while (c[2].fi>0 || c[1].fi>0 || c[0].fi>0) {
		if (c[2].fi == c[1].fi  &&  c[2].fi == c[0].fi) {
			printf("%c%c%c", c[2].sc, c[1].sc, c[0].sc);
			REP(x,0,3) --c[x].fi;
		} else {
			printf("%c%c", c[2].sc, c[1].sc);
			--c[2].fi, --c[1].fi;
			if (c[1].fi < c[0].fi) swap(c[1], c[0]);
		}
	}
	printf("\n");

}