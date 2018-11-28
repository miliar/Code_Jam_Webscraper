#include <iostream>
#include <cstdio>
#include <algorithm>
#include <vector>
using namespace std;

#define SZ(a) (int)(a).size()
typedef long long ll;
typedef long double ld;

int itc;

void solve() {
	int n, k;
	cin >> n >> k;
	ld u;
	cin >> u;
	vector<ld> a;
	for (int i = 0; i < n; i++) {
		ld x;
		cin >> x;
		a.push_back(x);
	}
	n++;
	a.push_back(1);
	sort(begin(a), end(a));
	ld s = a[0];
	int i = 1;
	for (; i < n; i++) {
		ld d = a[i]-s;
		if (u <= d*i) {
			s += u/i;
			break;
		}
		else {
			s = a[i];
			u -= d*i;
		}
	}
	ld ans = 1;
	for (int j = 0; j < i; j++) {
		ans *= s;
	}
	for (int j = i; j < n; j++) {
		ans *= a[j];
	}
	printf("%.6Lf\n", ans);
}

int main() {
	cin.sync_with_stdio(false);
	int ntc;
	cin >> ntc;
	for (itc = 1; itc <= ntc; itc++) {
		printf("Case #%d: ", itc);
		solve();
	}
}
