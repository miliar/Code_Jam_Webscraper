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
		ll n;
		ld d;
		cin >> d >> n;

		ld mt = 0;
		for (ll i = 0; i < n; i++) {
			ll p, s;
			cin >> p >> s;
			mt = max(mt, (d - p) / ld(s));
		}

		cout << "Case #" << q + 1 << ": ";
		cout << setprecision(8) << fixed << d / mt << "\n";
	}

	return 0;
}