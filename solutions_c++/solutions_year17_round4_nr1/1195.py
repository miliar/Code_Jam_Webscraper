#define _CRT_SECURE_NO_WARNINGS

#include <algorithm>
#include <assert.h>
#include <bitset>
#include <cmath>
#include <deque>
#include <fstream>
#include <iomanip>
#include <iostream>
#include <list>
#include <map>
#include <queue>
#include <set>
#include <stack>
#include <string>
#include <unordered_map>
#include <unordered_set>
#include <vector>

using namespace std;

typedef long long ll;
typedef long double ld;
typedef pair<ll, ll> llp;

const ll INF = 1000000000000;

int main() {
	ll t;
	cin >> t;

	for (ll q = 0; q < t; q++) {
		cout << "Case #" << q + 1 << ": ";

		ll n, p;
		cin >> n >> p;

		vector<ll> rem(10, 0);
		for (ll i = 0; i < n; i++) {
			ll x;
			cin >> x;
			rem[x % p]++;
		}

		ll ans = 0;
		ans += rem[0];
		ll trem = 0;

		if (p == 2) {
			ans += (rem[1] + 1) / 2;
		}
		else if (p == 3) {
			ll m = min(rem[1], rem[2]);
			ans += m;
			rem[1] -= m;
			rem[2] -= m;

			ans += (rem[1] + 2) / 3;
			ans += (rem[2] + 2) / 3;
		}
		else {
			ans += rem[2] / 2;
			rem[2] = rem[2] % 2;

			ll m = min(rem[1], rem[3]);
			ans += m;
			rem[1] -= m;
			rem[3] -= m;

			ans += rem[1] / 4;
			ans += rem[3] / 4;

			rem[1] = rem[1] % 4;
			rem[3] = rem[3] % 4;

			if (rem[2] > 0 && rem[1] >= 2) {
				ans++;
				rem[2]--;
				rem[1] -= 2;
			}

			if (rem[2] > 0 && rem[3] >= 2) {
				ans++;
				rem[2]--;
				rem[3] -= 2;
			}

			if (rem[2] > 0 || rem[1] > 0 || rem[3] > 0) {
				ans++;
			}
		}

		cout << ans << "\n";
	}

	return 0;
}