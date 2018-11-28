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
const ll inf = (ll)1e9 + 7;
const ld eps = 1e-7;
const int maxm = 24 * 60;
const int maxk = 720;

int n, t, k;
ld u;
ld a[maxn];

multiset<ld> s;

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	cin >> t;
	for (int ii = 0; ii < t; ii++) {
		cerr << ii << endl;
		cin >> n >> k >> u;
		s.clear();
		for (int i = 0; i < n; i++) {
			cin >> a[i];
			s.insert(a[i]);
		}
		ld step = 1e-5;
		while (u > 0) {
			ld num = *s.begin();
			s.erase(s.begin());
			num += min(u, step);
			u -= step;
			s.insert(num);
		}
		ld ans = 1;
		for (auto it = s.begin(); it != s.end(); it++) {
			ans *= *it;
		}
		printf("Case #%d: %.6lf\n", ii + 1, ans);
	}
	return 0;
}