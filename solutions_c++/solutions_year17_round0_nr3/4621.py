#include <cinttypes>
#include <inttypes.h>
#include <vector>
#include <string>
#include <stdio.h>
#include <stdlib.h>
#include <iostream>
#include <map>
#include <utility>
#include <cmath>
#include <algorithm>
#include <set>
#include <stack>
#include <string.h>
#include <list>
#include <bitset>
#include <functional>

#define vi vector<int>
#define vvi vector<vi>
#define pii pair<int,int>
#define vpii vector<pii>
#define ll long long

#define all(s) s.begin(), s.end()

using namespace std;

int nxi() { int a; cin >> a; return a; }

vector<ll> a;
void inc(int i, ll v) {
	for (; i < a.size(); i |= i + 1) {
		a[i] = max(a[i], v);
	}
}

long long get(int r) {
	long long ans = 0;
	for (; r >= 0; r = (r & (r + 1)) - 1) {
		ans = max(ans, a[r]);
	}
	return ans;
}

long long get(int l, int r) {
	return get(r) - get(l - 1);
}


int gcd(int a, int b) { return a == 0 ? b : gcd(b % a, a); }


int main() {

	freopen("data.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

int TCount = nxi();
for (int T = 1; T <= TCount; ++T) {

	ll n, k;
	cin >> n >> k;

	map<ll, ll, greater<ll>> m;
	m[n] = 1;
	while (k > 0) {
		auto & p = m.begin();

		ll delta = min(k, p->second);
		ll left = (p->first - 1) / 2, right = (p->first) / 2;
		m[left] += delta, m[right] += delta;
		k -= delta;
		if (k == 0) break;

		if (p->second == delta) m.erase(p);
	}

	printf("Case #%d: ", T);
	auto & p = m.begin();
	ll left = (p->first - 1) / 2, right = (p->first) / 2;
	cout << right << ' ' << left << endl;
}

	return 0;
}

