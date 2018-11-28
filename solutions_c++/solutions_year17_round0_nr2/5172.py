#include <bits\stdc++.h>
using namespace std;
typedef long long int ll;

ll solve(ll n) {
	ll m = 1; 
	while (m * 10 <= n) m *= 10;
	for (; m >= 10; m /= 10) {
		ll n1 = n / m;
		ll a = n1 % 10;
		ll b = (n / (m / 10)) % 10;
		if (a > b) return (solve(n1 - 1) * m + m - 1);
	}
	return n;
}

int main()
{
	int t; cin >> t;
	for (int ti = 1; ti <= t; ti++) {
		ll n; cin >> n;
		cout << "Case #" << ti << ": " << solve(n) << endl;
	}
}