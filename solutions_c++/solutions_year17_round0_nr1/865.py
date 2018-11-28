#include <stdio.h>
#include <vector>
#include <algorithm>
#define FOR(i,n,m) for (int i=n;i<=m;i++)
#define si(n) fscanf(in,"%d",&n)
#define NM 25
using namespace std;
FILE *in = fopen("input.txt", "r"), *out = fopen("output.txt", "w");
//FILE *in = stdin, *out = stdout;
#include <string.h>
int n,K;
char a[1005];
void solve() {
	fscanf(in, "\n%s %d", a + 1, &K);
	n = strlen(a + 1);
	int ans = 0;
	FOR(i, 1, n - K + 1) {
		if (a[i] == '-') {
			ans++;
			FOR(j, i, i + K - 1) {
				if (a[j] == '-') a[j] = '+';
				else if (a[j] == '+') a[j] = '-';
			}
		}
	}
	FOR(i, 1, n) if (a[i] == '-') {
		fprintf(out, "IMPOSSIBLE\n");
		return;
	}
	fprintf(out, "%d\n", ans);
}
int main() {
	int TT; si(TT);
	FOR(tt, 1, TT) {
		fprintf(out, "Case #%d: ", tt);
		solve();
	}
	return 0;
}