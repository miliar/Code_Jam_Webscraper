#define _CRT_SECURE_NO_WARNINGS
#define _USE_MATH_DEFINES

#include <algorithm>
#include <assert.h>
#include <bitset>
#include <math.h>
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
#include <unordered_set>
#include <unordered_map>
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

		ll n, k;
		cin >> n >> k;
		vector<llp> p(n);
		for (ll i = 0; i < n; i++) {
			cin >> p[i].first >> p[i].second;
		}

		sort(p.begin(), p.end());

		multiset<ld> s;
		ld sum = 0;
		for (ll i = 0; i < k - 1; i++) {
			s.insert(2 * M_PI * (ld)p[i].first * (ld)p[i].second);
			sum += 2 * M_PI * (ld)p[i].first * (ld)p[i].second;
		}

		ld ans = 0;
		for (ll i = k - 1; i < n; i++) {
			ld tsum = sum + 2 * M_PI * (ld)p[i].first * (ld)p[i].second + M_PI * (ld)p[i].first * (ld)p[i].first;

			ans = max(ans, tsum);

			s.insert(2 * M_PI * (ld)p[i].first * (ld)p[i].second);
			sum += 2 * M_PI * (ld)p[i].first * (ld)p[i].second;
			sum -= *s.begin();
			s.erase(s.begin());
		}

		cout << setprecision(8) << fixed << ans << "\n";
	}

	return 0;
}