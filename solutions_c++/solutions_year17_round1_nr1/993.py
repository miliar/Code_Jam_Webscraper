//TAG : 
#include<bits/stdc++.h>
using namespace std;
#define rep(i,n)	for(int (i)=0;(i)<(n);(i)++)
#define repd(i,n)	for(int (i)=(n)-1;(i)>=0;(i)--)
#define REP(i,j,n)  for(int (i)=(j),_n=(n); (i) < _n; (i)++)
#define FOR(i,a,b)  for(int _b=(b), (i)=(a); (i) <= _b; (i)++)
#define FORD(i,a,b) for(int i=(a),_b=(b);i>=_b;i--)
#define ALL(c) (c).begin(), (c).end()
#define SORT(c) sort(ALL(c))
#define CLEAR(x) memset((x),0,sizeof(x))
#define REVERSE(c) reverse(ALL(c))
#define UNIQUE(c) SORT(c),(c).resize(unique(ALL(c))-(c).begin())
#define X first
#define Y second
#define MP make_pair
#define MT make_tuple
#define EPS 	(1e-9)
typedef pair<int, int>	pii;
typedef vector<int>		vi;
typedef unsigned int	uint;
typedef long long		ll;
typedef unsigned long long	ull;
template<typename T> void check_max(T& a, T b) { if (a < b) a = b; }
template<typename T> void check_min(T& a, T b) { if (a > b) a = b; }
#ifdef _MSC_VER
#include "builtin_gcc_msvc.h"
#define gets	gets_s
#else
#define popcnt(x)	__builtin_popcount(x)
#define ctz(x)		__builtin_ctz(x)
#define clz(x)		__builtin_clz(x)
#define popcntll(x)	__builtin_popcountll(x)
#define ctzll(x)	__builtin_ctzll(x)
#define clzll(x)	__builtin_clzll(x)
#endif

const int MX = 25;
char A[MX][MX + 1], B[MX][MX + 1];
int sum[MX][MX];
pii P[26];
int R, C, n;
bool solve(int step, int black, bitset<MX> vis[MX]) {
	if (step == n) {
		if (black == R*C)
			return true;
		else return false;
	}
	bitset<MX> v2[MX];
	int r = -1, c = -1;
	rep(i, R)rep(j, C)if (!vis[i][j]) {
		r = i, c = j; goto FOUND;
	}
FOUND:
	if (r != -1) {
		REP(r2, r, R)REP(c2, c, C) {
			int cnt = sum[r2][c2] - (r ? sum[r - 1][c2] : 0) - (c ? sum[r2][c - 1] : 0) + (r && c ? sum[r - 1][c - 1] : 0);
			int v = 0;
			FOR(i, r, r2)FOR(j, c, c2)v += vis[i][j];
			if (cnt == 1 && !v) {
				rep(i, R)v2[i] = vis[i];
				FOR(i, r, r2)FOR(j, c, c2)v2[i][j] = 1;

				int k = 0;
				while (k < n && !(r <= P[k].X && P[k].X <= r2 && c <= P[k].Y && P[k].Y <= c2))++k;
				char ch = A[P[k].X][P[k].Y];
				FOR(i, r, r2)FOR(j, c, c2)A[i][j] = ch;

				if (solve(step + 1, black + (r2 - r + 1)*(c2 - c + 1), v2)) {
					int k = 0;
					while (k < n && !(r <= P[k].X && P[k].X <= r2 && c <= P[k].Y && P[k].Y <= c2))++k;
					char ch = A[P[k].X][P[k].Y];
					FOR(i, r, r2)FOR(j, c, c2)A[i][j] = ch;
					return true;
				}
			}
		}
	}
	return false;
}
int main()
{
	int TC;
	scanf("%d", &TC);
	FOR(T, 1, TC)
	{
		scanf("%d%d", &R, &C);
		rep(i, R)scanf("%s", A[i]);
		n = 0;
		rep(i, R)rep(j, C)if (isupper(A[i][j]))
			P[n++] = MP(i, j);
		//memcpy(B, A, sizeof A);
		CLEAR(sum);
		rep(i, R)rep(j, C)
			sum[i][j] = (i ? sum[i - 1][j] : 0) + (j ? sum[i][j - 1] : 0) - (i && j ? sum[i - 1][j - 1] : 0) + isupper(A[i][j]);

		bitset<MX> vis[MX];
		rep(i, R)vis[i].reset();
		bool ok = solve(0, 0, vis);
		printf("Case #%d:\n", T);
		rep(i, R)puts(A[i]);
	}

	return 0;
}