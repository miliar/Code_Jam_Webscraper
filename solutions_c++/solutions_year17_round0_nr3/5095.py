/*AMETHYSTS*/
#pragma comment(linker, "/STACK:1000000000")
#include <cstdio>
#include <iostream>
#include <ctime>
#include <string>
#include <vector>
#include <cmath>
#include <algorithm>
#include <cstring>
#include <set>
#include <cstdlib>
#include <ctime>
#include <cassert>
#include <bitset>
#include <deque>
#include <stack>
#include <climits>
#include <string>
#include <queue>
#include <memory.h>
#include <map>
#include <unordered_map>
#include <unordered_set>

#define ll long long
#define ld double
#define mp make_pair

using namespace std;

const double PI = 3.14159265358979323846;
const int maxn = (int)101;
const ll mod = (ll)1e9 + 7;
const ll inf = (ll)1e18 + 7;
const double eps = 1e-6;

int t;

pair<ll, ll> solve(ll l, ll r, ll k) {
	ll n = r - l + 1;
	if (k == 1) {
		ll m = (l + r) / 2;
		return mp(max(m - l, r - m), min(m - l, r - m));
	}
	ll m = (l + r) / 2;
	k--;
	if (m - l > r - m) {
		if (k % 2 == 1) {
			return solve(l, m - 1, k / 2 + 1);
		}
		else {
			return solve(m + 1, r, k / 2);
		}
	}
	else {
		if (k % 2 == 1) {
			return solve(m + 1, r, k / 2 + 1);
		}
		else {
			return solve(l, m - 1, k / 2);
		}
	}
}

ll n, k;

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	
	cin >> t;
	for (int ii = 0; ii < t; ii++) {
		cin >> n >> k;
		printf("Case #%d: ", ii + 1);
		pair<ll, ll> tans = solve(1, n, k);
		cout << tans.first << ' ' << tans.second << endl;
	}

	return 0;
}