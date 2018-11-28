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
ll n, K, ans;
ll d[3], c[3];
void input() {
	fscanf(in, "%lld %lld", &n, &K);
}
ll big(ll x) {
	return x >> 1;
}
ll small(ll x) {
	return x - 1 - (x >> 1);
}
void pro() {
	d[1] = n, c[1] = 1;
	d[2] = 0, c[2] = 0;
	for (;;) {
		ll x1 = big(d[1]);
		ll x2 = x1 - 1;
		ll t1 = 0, t2 = 0;
		FOR(k, 1, 2) {
			if (big(d[k]) == x1) t1 += c[k];
			if (small(d[k]) == x1) t1 += c[k];

			if (big(d[k]) == x2) t2 += c[k];
			if (small(d[k]) == x2) t2 += c[k];
		}
		if (K <= c[1]) {
			fprintf(out, "%lld %lld\n", big(d[1]), small(d[1]));
			break;
		}
		K -= c[1];
		if (K <= c[2]) {
			fprintf(out, "%lld %lld\n", big(d[2]), small(d[2]));
			break;
		}
		K -= c[2];
		d[1] = x1, d[2] = x2;
		c[1] = t1, c[2] = t2;
	}
}
int main() {
	int TT; si(TT);
	FOR(tt, 1, TT) {
		input();
		fprintf(out, "Case #%d: ", tt);
		pro();
	}
	return 0;
}