#include <cstdio>
#include <algorithm>
#include <vector>
#include <cmath>
#include <cstring>
#include <string>
#include <map>
#include <queue>
#include <set>

#define LL long long int
#define FOR(i, s, e) for (int i=(s); i<(e); i++)
#define FOE(i, s, e) for (int i=(s); i<=(e); i++)
#define FOD(i, s, e) for (int i=(s)-1; i>=(e); i--)
#define CLR(x, a) memset(x, a, sizeof(x))
#define eps (1e-9) 

#define N 55
using namespace std;

int test;
int n, m, w[N], a[N][N], l[N][N], r[N][N], p[N];

void get_range(int id, int x, int *l, int *r) {
	*r = floor((x * 1.0 + eps) / (0.9 * w[id]));
	*l = ceil((x * 1.0 - eps) / (1.1 * w[id]));
}

void solve(int test) {
	scanf("%d%d", &n, &m);
	
	FOR(i, 0, n) scanf("%d", &w[i]);
	FOR(i, 0, n) {
		FOR(j, 0, m) scanf("%d", &a[i][j]);
		sort(a[i], a[i] + m);
		FOR(j, 0, m) get_range(i, a[i][j], &l[i][j], &r[i][j]);
	}
	
	FOR(i, 0, n) p[i] = 0;
	int ret = 0;
	
	do {
		int done = 0;
		FOR(i, 0, n) if (p[i] == m) done = 1;
		if (done) break;
		
		int L = -1, R = 2000000;
		FOR(i, 0, n){
			L = max(L, l[i][p[i]]);
			R = min(R, r[i][p[i]]);
		}
		
		if (L <= R) {
			if (R >= 1) ret++;
			FOR(i, 0, n) p[i]++;
		}
		else {
			FOR(i, 0, n) if (r[i][p[i]] < L) p[i]++;
		}
		
		
		
		
	} while (1);
	
	
	printf("Case #%d: %d\n", test, ret);
	
}

int main(){
	scanf("%d", &test);
	FOR(i, 0, test) solve(i + 1);
	return 0;
}
