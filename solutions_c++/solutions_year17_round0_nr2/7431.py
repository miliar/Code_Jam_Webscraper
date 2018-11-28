#include <bits/stdc++.h>

#define all(a) (a).begin(), (a).end()
#define sz(a) (int)(a).size()
#define pb push_back

typedef long long ll;

using namespace std;

int main()
{

	//ifstream cin("input.txt");
	//ofstream cout("output.txt");

	ios_base::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);

	ifstream cin("input.txt");
	ofstream cout("output.txt");

	int tt;
	cin >> tt;

	for (int test = 1; test <= tt; ++test) {
		cout << "Case #" << test << ": ";
		ll n;
		n = test;
		cin >> n;
		ll ans;
		int ansLen;
		for (int len = 1; ; ++len) {
			ll sum = 0;
			ll deg = 1;
			for (int i = 0; i < len; ++i) {
				sum += deg;
				deg *= 10;
			}
			bool ok = true;
			for (int d = 1; d < 10; ++d) {
				if (sum * d > n) {
					ok = false;
					break;
				}
				ans = sum * d;
				ansLen = len;
			}
			if (!ok) {
				break;
			}
		}
		int prevD = ans % 10;
		for (int i = ansLen - 1; i >= 1; --i) {
			ll sum = 0;
			ll deg = 1;
			for (int j = 0; j < i; ++j) {
				sum += deg;
				deg *= 10;
			}
			for (int d = prevD + 1; d < 10; ++d) {
				if (ans + sum <= n) {
					ans += sum;
					prevD = d;
				} else {
					break;
				}
			}
		}
		cout << ans << "\n";
	}

}
