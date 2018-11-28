#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <set>
#include <map>
#include <list>
#include <stdio.h>
#include <time.h>
#include <assert.h>
#include <math.h>
typedef long long ll;
typedef long double ld;
using namespace std;

const ll SZ = 1e5 + 10;
const ll INF = 1e9;

map<ll, ll> d;

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	ios::sync_with_stdio(false);

	ll t;
	cin >> t;
	for (ll testn = 1; testn <= t; testn++) {
		ll n, k;
		cin >> n >> k;
		d.clear();
		d[n] = 1;
		ll taken = 0;
		while (d.size() && d.rbegin()->second + taken < k) {
			auto x = d.end(); x--;
			taken += x->second;
			d[(x->first - 1) / 2] += x->second;
			d[(x->first - 1) - (x->first - 1) / 2] += x->second;
			d.erase(x);
		}
		auto x = d.end(); x--;
		cout << "Case #" << testn << ": " << (x->first - 1) - (x->first - 1) / 2 << " " << (x->first - 1) / 2 << "\n";
		cerr << testn << "\n";
	}

	return 0;
}