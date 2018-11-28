#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <set>
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

ll gen(ll lft, ll taken, ll lastn, ll x) {
	if (!lft)
		return taken;
	for (ll i = 9; i >= lastn; i--) {
		ll l = lft, y = taken;
		while (l--)
			y = y * 10 + i;
		if (y <= x)
			return gen(lft - 1, taken * 10 + i, i, x);
	}
	return -1;
}

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	ios::sync_with_stdio(false);

	ll t;
	cin >> t;
	for (ll testn = 1; testn <= t; testn++) {
		ll x;
		cin >> x;
		ll len = 0, y = x;
		while (y) {
			len++;
			y /= 10;
		}
		ll a = gen(len, 0, 1, x);
		cout << "Case #" << testn << ": ";
		if (a != -1)
			cout << a;
		else
			cout << gen(len - 1, 0, 1, x);
		cout << "\n";
	}

	return 0;
}