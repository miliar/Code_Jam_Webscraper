/**
 * Sergey Kopeliovich (burunduk30@gmail.com)
 */

#include <bits/stdc++.h>

using namespace std;

#define forn(i, n) for (int i = 0; i < (int)(n); i++)
#define err(...) fprintf(stderr, "%.2f : ", 1. * clock() / CLOCKS_PER_SEC), fprintf(stderr, __VA_ARGS__), fflush(stderr)

const int N = 103;

int f[3][4][N][N][N];

void relax( int &a, int b ) { a = max(a, b); }

int get( int p, int rest, int a1, int a2, int a3 ) {
	int &res = f[p - 2][rest][a1][a2][a3];
	if (res != -1)
		return res;
	res = 0;
	if (a1 > 0) relax(res, !rest + get(p, (rest + 1) % p, a1 - 1, a2, a3));
	if (a2 > 0) relax(res, !rest + get(p, (rest + 2) % p, a1, a2 - 1, a3));
	if (a3 > 0) relax(res, !rest + get(p, (rest + 3) % p, a1, a2, a3 - 1));
	return res;
}

void solve() {
	int n, p, x;
	scanf("%d%d", &n, &p);
	vector<int> cnt(max(p, 4));
	forn(i, n) {
		scanf("%d", &x);
		cnt[x % p]++;
	}
	// err("cnt[0] = %d\n" ,cnt[0]);
	printf("%d\n", cnt[0] + get(p, 0, cnt[1], cnt[2], cnt[3]));
}
int main() {
	int tn;
	scanf("%d", &tn);
	memset(f, -1, sizeof(f));
	forn(t, tn) {
		printf("Case #%d: ", t + 1);
		// err("Case #%d\n", t + 1);
		solve();
	}
}