#include <bits/stdc++.h>
using namespace std;

typedef long long ll;
const int N = 1005;
const int M = 100000007;

ll n;

bool judge(ll x) {
    int pre = -1;
    while (x) {
    	if (pre != -1 && x % 10 > pre) { return false; }
    	pre = x % 10;
    	x /= 10;
    }
    return true;
}

int main() {
	freopen("B-small-attempt1.in", "r", stdin);
	freopen("out", "w", stdout);
    int C = 0, T;
    scanf("%d", &T);
    while (++C <= T) {
        scanf("%lld", &n);
		printf("Case #%d: ", C);
	
		if (judge(n)) { printf("%lld\n", n); continue; }
	
		ll t = n;
		int len = 0;
		while (t) { len++; t /= 10; }
	
		ll ans1 = 0; t = 1;
		while (ans1 + t * 9 <= n) { ans1 += t * 9; t *= 10; }
		if (n / t > 1) { ans1 += t * (n / t - 1); }
		
		//cout << ans1 << endl;
	
		ll ans2 = 0, d = n % 10; t = 1;
		while (true) {
			d = min(d, n / t % 10);
			if (d == 0 || ans2 + t * d > n) { break; }
			ans2 += t * d;
			t *= 10;
		}
		//cout << ans2 << endl;
	
		ll ans3 = 0; d = 9; t = 1;
		ll nn = n;
		while (nn % 10 != 9) { nn--; }
		while (true) {
			d = min(d, nn / t % 10);
			if (d == 0 || ans3 + t * d > n) { break; }
			ans3 += t * d;
			t *= 10;
		}
		//cout << ans3 << endl;
		
		ll ans = max({ans1,ans2,ans3});
		printf("%lld\n", ans);
	}
}
