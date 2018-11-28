#include <stdio.h>
#include <vector>
#include <algorithm>
#define FOR(i,n,m) for (int i=n;i<=m;i++)
#define si(n) fscanf(in,"%d",&n)
#define NM 25
using namespace std;
FILE *in = fopen("input.txt", "r"), *out = fopen("output.txt", "w");
//FILE *in = stdin, *out = stdout;
typedef long long int ll;
ll n;
ll ans, ten[20];
int len;
void pre() {
	ten[0] = 1;
	FOR(i, 1, 18) ten[i] = ten[i - 1] * 10;
}

bool pro(int idx, int num, ll limit, ll x) {
	if (x > n) return false;
	if (idx == -1) {
		fprintf(out, "%lld", x);
		return true;
	}
	for (int i = 9; i >= num; i--)
		if (pro(idx - 1, i, limit, x + i*ten[idx])) return true;
	return false;
}

void solve() {
	fscanf(in, "%lld", &n);
	len = 0;
	for (ll x = n; x; x /= 10, len++);
	if (!pro(len-1, 0, n, 0)) FOR(j, 0, len - 2) fprintf(out, "9");
	fprintf(out, "\n");
}
int main() {
	int TT; si(TT);
	pre();
	FOR(tt, 1, TT) {
		fprintf(out, "Case #%d: ", tt);
		solve();
	}
	return 0;
}