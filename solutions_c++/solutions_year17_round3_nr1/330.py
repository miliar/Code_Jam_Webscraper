	//g++ -std=c++0x your_file.cpp -o your_program
#include <iostream>
#include <fstream>
#include <string>
#include <algorithm>
#include <math.h>
#include <vector>
#include <cstring>
#include <queue>
#include <cstdio>
#include <cstdlib>
#include <map>
#include <set>
#include <iomanip>
#define fname ""
#define mp make_pair
#define F first
#define pb push_back
#define S second
#define ub upper_bound
#define lb lower_bound
#define inf 2000000000
#define INF 2000000000000000000ll
using namespace std;

typedef long long ll;

const int maxn = 1010;

double pi;

struct Slice {
	int r, h;
	bool operator < (Slice b) const {
		return r < b.r;
	}
}a[maxn];

const double eps = 1e-11;

set <pair <ll, int> > q;

inline ll f(int id) {
	return 2ll * a[id].r * a[id].h;
}

inline void solve() {
	int n, k;
	cin >> n >> k;
	for (int i = 1; i <= n; i++) {
		cin >> a[i].r >> a[i].h;
	}
	q.clear();
	ll sum = 0, cur, ans = 0;
	sort (a + 1, a + n + 1);
	for (int i = 1; i <= n; i++) {
		cur = sum + f(i) + a[i].r * 1ll * a[i].r;
		if (cur > ans) {
			ans = cur;
		}
//		cout << i << " " << cur << endl;
		if ((int)q.size() < k - 1) {
			q.insert(mp(f(i), i));
			sum += f(i);
		}
		else if (k > 1) {
			if (q.begin() -> F < f(i)) {
				sum -= q.begin() -> F;
				q.erase(q.begin());
				sum += f(i);
				q.insert(mp(f(i), i));
			}
		}
	}
	long double ans2 = pi * ans;
	cout << fixed;
	cout << setprecision(9) << ans2 << endl;
}

int main() {
	freopen (fname"A-large.in.txt", "r", stdin);
	freopen (fname"out.txt", "w", stdout);
	ios_base::sync_with_stdio(0);
	int T;
	cin >> T;
	pi = acos(-1.0);
	for (int Case = 1; Case <= T; Case++) {
		cout << "Case #" << Case << ": ";
		solve();
	}
	return 0;
}
