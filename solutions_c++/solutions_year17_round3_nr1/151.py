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
#define ll long long
#define ld double
#define mp make_pair

using namespace std;

const double PI = 3.14159265358979323846;
const ll maxn = (ll)3e3 + 10;
const ll maxlog = (ll)13;
const ll mod = (ll)1e9 + 7;
const ll inf = (ll)1e18 + 7;
const ld eps = 1e-7;

ll n, k, x, y, t;
vector<pair<ll, ll> > v;
ld a[maxn];
multiset<ld> s;

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	cin >> t;
	for (int ii = 0; ii < t; ii++) {
		cin >> n >> k;
		v.clear();
		for (int i = 0; i < n; i++) {
			cin >> x >> y;
			v.push_back(mp(x, y));
		}
		sort(v.rbegin(), v.rend());
		for (int i = 0; i < v.size(); i++) {
			a[i] = 2.0 * PI * (ld)v[i].first * (ld)v[i].second;
		}
		ld ans = 0;
		for (int i = 0; i < v.size(); i++) {
			ld tans = a[i] + PI * (ld)v[i].first * (ld)v[i].first;
			ld sum = 0;
			s.clear();
			for (int j = i + 1; j < v.size(); j++) {
				s.insert(a[j]);
				sum += a[j];
				while (s.size() > k - 1) {
					sum -= *s.begin();
					s.erase(s.begin());
				}
				if (s.size() == k - 1) {
					ans = max(ans, tans + sum);
				}
			}
			if (k == 1) {
				ans = max(ans, tans);
			}
		}
		printf("Case #%d: %.8lf\n", ii + 1, ans);
	}
	return 0;
}