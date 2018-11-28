#include <bits/stdc++.h>

using namespace std;

#define fi first
#define se second
#define MOD (1000LL * 1000LL * 1000LL)
#define maxn 100111

long long x[maxn], s[maxn];
long long d, n;

long double solve(){
	scanf("%lld%lld", &d, &n);
	for(long long i = 0; i < n; i++)
		scanf("%lld%lld", x + i, s + i);

	long double ans = 10000000000000.0;
	for(int i = 0; i < n; i++){
		long double time = x[i] / ans;
		long long pot = (d - x[i]);
		if( 1.0 * pot * ans > d * s[i])
			ans = 1.0 * d / (1.0 * pot / s[i]);
	}
	return ans;
}

int main(){
	long long t;
	scanf("%lld", &t);
	for(long long l = 1; l <= t; l++){
		cout << "Case #" << l << ": ";
		cout << fixed << setprecision(7) << solve() << endl;
	}
	return 0;
}