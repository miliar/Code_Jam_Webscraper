#include<bits/stdc++.h>
using namespace std;
#define ll long long
#define f(i, x, n) for (int i = x; i < (int)(n); ++i)

int main(){
	freopen("main.in", "r", stdin);
	freopen("main.out", "w", stdout);
	int t;
	scanf("%d", &t);
	f(tc, 1, t + 1){
		printf("Case #%d: ", tc);
		ll n, k;
		scanf("%lld%lld", &n, &k);
		pair<ll, ll> a(n, 1), b(n, 0);
		while (k){
			if (k <= a.second) { printf("%lld %lld\n", a.first >> 1, a.first - 1 >> 1); break; }
			k -= a.second;
			if (k <= b.second) { printf("%lld %lld\n", b.first >> 1, b.first - 1 >> 1); break; }
			k -= b.second;
			pair<ll, ll> x(a.first >> 1, 0), y(b.first - 1 >> 1, 0);
			if (a.first & 1)x.second += a.second << 1; else x.second += a.second, y.second += a.second;
			if (b.first & 1)y.second += b.second << 1; else x.second += b.second, y.second += b.second;
			a = x;
			b = y;
		}
	}
}
