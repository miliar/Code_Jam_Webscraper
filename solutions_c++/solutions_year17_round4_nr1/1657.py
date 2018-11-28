#include <cinttypes>
#include <inttypes.h>
#include <numeric>
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
#include <queue>
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

#define EPS 1e-11

int dyn[201][101][101][101]; //2139062143

int hd_orig, b, d;
int deep = 0;

int main() {

	freopen("data.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

int TCount = nxi();
for (int T = 1; T <= TCount; ++T) {

	printf("Case #%d: ", T);
	cerr << T << endl;

	int n = nxi(), p = nxi();;
	int v;
	vi a(p);
	for (int i = 0; i < n; ++i) {
		cin >> v;
		a[v % p]++;
	}

	int ans = 0;
	ans += a[0];

	if (p == 2) {
		if (a[1] > 0)
			ans += (a[1] - 1) / 2 + 1;
	}
	if (p == 3) {
		int k = min(a[1], a[2]);
		ans += k;
		a[1] -= k, a[2] -= k;
		if (a[1] > 0)
			ans += (a[1] - 1) / 3 + 1;
		if (a[2] > 0)
			ans += (a[2] - 1) / 3 + 1;
	}
	if (p == 4) {
		int k = min(a[1], a[3]);
		a[1] -= k, a[3] -= k;
		ans += k;

		if (a[2] > 0) {
			ans += a[2] / 2;
			a[2] -= (a[2] / 2 )* 2;
		}

		if (a[2] > 0) {
			if (a[1] > 1) {
				a[1] -= 2;
			} else
				if (a[3] > 1) {
					a[3] -= 2;
				}

			ans++;
		}

		if (a[1] > 0)
			ans += (a[1] - 1) / 4 + 1;
		if (a[3] > 0)
			ans += (a[3] - 1) / 4 + 1;
	}

	cout << ans << endl;
	
}

	return 0;
}

