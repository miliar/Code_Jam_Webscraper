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

	ll n;
	cin >> n;

	bool passed = true;
	do {
		ll base = 1ll;
		while (base * 10 <= n) {
			base *= 10;
		}

		passed = true;
		int prevDig = 0;
		for (; base > 0; base /= 10) {
			int dig = (n / base) % 10;
			if (dig < prevDig) {
				ll base10 = base * 10;
				n = (n / base10 - 1) * base10 + base10 - 1;
				passed = false;
				break;
			}
			prevDig = dig;
		}
	} while (!passed);

	printf("Case #%d: ", T);
	cout << n << endl;
}

	return 0;
}

