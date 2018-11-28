#include <iostream>
#include <cstdio>
#include <algorithm>
#include <vector>
using namespace std;

#define SZ(a) (int)(a).size()
typedef long long ll;

int itc;

void solve() {
	int n, m;
	cin >> n >> m;
	vector<string> a(n);
	for (auto& r: a) {
		cin >> r;
	}
	int ir0 = -1;
	for (int i = 0; i < n; i++) {
		auto& r = a[i];
		auto it = find_if(begin(r), end(r), [&] (char c) {
				return c != '?';
				});
		if (it == end(r)) {
			continue;
		}
		if (ir0 == -1) {
			ir0 = i;
		}
		char c = *it;
		it = begin(r);
		while (true) {
			for (; it != end(r) && *it == '?'; it++) {
				*it = c;
			}
			if (it == end(r)) {
				break;
			}
			c = *it;
			it++;
		}
	}
	for (int i = ir0-1; i >= 0; i--) {
		a[i] = a[i+1];
	}
	for (int i = ir0+1; i < n; i++) {
		if (a[i][0] != '?') {
			continue;
		}
		a[i] = a[i-1];
	}
	for (auto& r: a) {
		printf("%s\n", r.c_str());
	}
}

int main() {
	cin.sync_with_stdio(false);
	int ntc;
	cin >> ntc;
	for (itc = 1; itc <= ntc; itc++) {
		printf("Case #%d:\n", itc);
		solve();
	}
}
