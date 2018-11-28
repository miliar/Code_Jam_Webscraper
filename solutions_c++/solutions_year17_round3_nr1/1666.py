#include <algorithm>
#include <iostream>
#include <cstring>
#include <vector>
#include <cstdio>
#include <iomanip>
#include <queue>
#include <stack>
#include <ctime>
#include <cmath>
#include <map>
#include <set>
#define r first
#define h second
#define ll long long

using namespace std;

const double pi = acos(-1.0);
const double eps = 1e-8;

int t;
pair < ll, ll > a[1004];
ll b[1005], m;

void solve(int id) {
	cout << "Case #" << id << ": ";
	int n, k;
	cin >> n >> k;
	for (int i = 1; i <= n; ++i) 
		cin >> a[i].r >> a[i].h;

	sort(a + 1, a + 1 + n);
	ll ans = 0;
	m = 0;

	for (int i = 1; i <= n; ++i) {		
		ll cur = 0;
		for (int j = 0, cnt = 1; j < m && cnt < k; ++j, ++cnt)
			cur += b[j];
		cur += (a[i].r * a[i].r + a[i].r * a[i].h * 2);
		ans = max(ans, cur);
		b[m++] = (a[i].r * a[i].h * 2);
		sort(b, b + m);
		reverse(b, b + m);
	}

	cout << fixed << setprecision(9) << ans * pi << endl;
}

int main() {
	#ifdef LOCAL	
	freopen("in", "r", stdin);
	freopen("out", "w", stdout);
	#endif
	cin >> t;
	for (int i = 1; i <= t; ++i)
		solve(i);
	return 0;
}