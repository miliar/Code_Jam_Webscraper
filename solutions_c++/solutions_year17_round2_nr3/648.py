/**********************
 #  By lintao [Hudi]  #
 **********************/

#define _MULTI_TC_
// #define _DEBUG_

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

#ifdef _DEBUG_
	#define DEBUG printf
	#define DREP REP
#else
	#define DEBUG if (0) printf
	#define DREP if (0) REP
#endif

typedef long long ll;
typedef pair<ll,ll> pll;
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

#define maxn 105
#define maxDbl 1e32
#define maxDst 1000000000000000

int N, Q;
pll kuda[maxn];
ll D[maxn][maxn];
double T[maxn][maxn];

void solve(int tc)
{
	INIT(D,-1);
	INIT(kuda,0);
	INIT(T,0);

	scanf("%d%d", &N, &Q);
	REP(x,0,N) scanf("%I64d%I64d", &kuda[x].fi, &kuda[x].sc);
	REP(x,0,N) REP(y,0,N) {
		scanf("%I64d", &D[x][y]);
		if (D[x][y] == -1LL) D[x][y] = maxDst;
	}

	// FW Distance
	REP(k,0,N) REP(i,0,N) REP(j,0,N)
		if (D[i][k] + D[k][j] < D[i][j]) {
			D[i][j] = D[i][k] + D[k][j];
		}

	DREP(x,0,N) {
		DREP(y,0,N) DEBUG(" %I64d", D[x][y]); DEBUG("\n");
	}
	DEBUG("<<<<<>>>>>\n");

	// compute time taken by kuda from each city wo change
	REP(x,0,N) REP(y,0,N) {
		if (D[x][y] <= kuda[x].fi) {
			T[x][y] = (double)D[x][y]/kuda[x].sc;
		} else {
			T[x][y] = maxDbl;
		}
	}

	DREP(x,0,N) {
		DREP(y,0,N) DEBUG(" %.6lf", T[x][y]); DEBUG("\n");
	}
	DEBUG("<<<<<>>>>>\n");

	// FW Time
	REP(k,0,N) REP(i,0,N) REP(j,0,N) {
		if (T[i][k] + T[k][j] < T[i][j] - EPS) {
			T[i][j] = T[i][k] + T[k][j];
		}
	}

	DREP(x,0,N) {
		DREP(y,0,N) DEBUG(" %.6lf", T[x][y]); DEBUG("\n");
	}
	DEBUG("<<<<<>>>>>\n");

	// Serve the question~
	printf("Case #%d:", tc);
	REP(x,0,Q) {
		int a, b;
		scanf("%d%d", &a, &b);
		printf(" %.6lf", T[--a][--b]);
	}
	printf("\n");

}