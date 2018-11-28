#include <bits\stdc++.h>
using namespace std;
typedef long long int ll;

void solve(ll n, ll k, ll& mi, ll& ma) {
	ll p2 = 1, a = 1, b = 0;
	while (k > p2) {
		k -= p2;
		int a1, b1;
		if (n % 2 == 0) a1 = a, b1 = a + 2*b, n = (n - 1) / 2;
		else a1 = 2 * a + b, b1 = b, n /= 2;
		a = a1, b = b1;
		p2 *= 2;
	}
	if (k <= b) {
		if ((n + 1) % 2 == 0) mi = (n / 2), ma = mi + 1;
		else mi = ma = (n / 2);
	}
	else { // k <= a + b
		if (n % 2 == 0) mi = (n - 1) / 2, ma = mi + 1;
		else mi = ma = (n / 2);
	}
}

int main()
{
	int t; cin >> t;
	for (int ti = 1; ti <= t; ti++) {
		ll n, k, min, max; cin >> n >> k;
		solve(n, k, min, max);
		cout << "Case #" << ti << ": " << max << " " << min << endl;
	}
}