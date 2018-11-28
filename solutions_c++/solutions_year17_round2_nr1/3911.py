#include<stdlib.h>
#include<stdio.h>
#include<cstring>
#include<string>
#include<vector>
#include<algorithm>
using namespace std;

const int maxn = 1500;

typedef long long ll;

const double EPS = 1e-9;

struct h{
	ll k, s;
	h(ll kk = 0, ll ss = 0): k(kk), s(ss) {
	}
	bool operator < (const h &a) const {
		if (k!=a.k)
			return k > a.k;
		return s < a.s;
	}
} ho[maxn];

int main(){
    freopen("A-large.in","rt",stdin);
	freopen("A-large.out", "w", stdout);
	int T; scanf("%d", &T);
	for (int tc = 1; tc <= T; tc++){
		ll de, n;
		scanf("%lld%lld", &de, &n);
		for (int i = 0; i < n; i++){
			scanf("%lld%lld", &ho[i].k, &ho[i].s);
		}
		sort(ho, ho + n);
		double dt = 0.;
		for (int i = 0; i < n; i++){
			double ti = double(de - ho[i].k) / double(ho[i].s);
			dt = max(dt, ti);
		}
		double sped, ded = de;
		if (dt - EPS < 0.) printf("Case #%d: %lf\n", tc, double(de)), sped = de;
		else printf("Case #%d: %.10lf\n", tc, ded / dt), sped = ded / dt;
	}
}
