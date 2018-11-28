#define _CRT_SECURE_NO_WARNINGS

#include <map>
#include <set>
#include <cmath>
#include <deque>
#include <queue>
#include <stack>
#include <cstdio>
#include <string>
#include <vector>
#include <complex>
#include <cstring>
#include <iomanip>
#include <utility>
#include <iostream>
#include <algorithm>

using namespace std;
typedef long long ll;

int main() {

	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int T;
	cin >> T;

	for (int t = 1; t <= T; t++) {
		ll n, k;
		cin >> n >> k;
		map<ll, ll> amt;
		priority_queue<ll> sz;
		amt[n] = 1;
		sz.push(n);
		while (amt[sz.top()] < k) {
			ll cur = sz.top();
			sz.pop();
			if (amt[cur] == 0) continue;
			k -= amt[cur];
			amt[cur / 2] += amt[cur];
			amt[(cur - 1) / 2] += amt[cur];
			sz.push(cur / 2);
			sz.push((cur - 1) / 2);
			amt[cur] = 0;
		}
		cout << "Case #" << t << ": " << sz.top() / 2 << ' ' << (sz.top() - 1) / 2 << '\n';
	}

	return 0;
}