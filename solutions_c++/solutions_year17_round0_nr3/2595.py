#include <bits/stdc++.h>

using namespace std;
typedef long long int ll;
#define BR __int("$3");

int main()
{
	int t;
	cin >> t;
	for (int tt = 1; tt <= t; ++tt)
	{
		ll n;
		ll k;
		cin >> n >> k;
		ll f = k;
			f >>= 1;
			f |= f >> 1;
			f |= f >> 2;
			f |= f >> 4;
			f |= f >> 8;
			f |= f >> 16;
			f |= f >> 32;
		ll g = f + 1;
		ll nn = n - f;
		ll b = nn / g;
		ll c = nn % g;
		if (c >= k - f) ++b;
		cout << "Case #" << tt << ": " << b/2 << ' ' << (b-1)/2 << endl;
	}
	return 0;
}
