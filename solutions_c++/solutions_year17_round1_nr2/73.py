#define _CRT_SECURE_NO_DEPRECATE
#include <iostream>
#include <string.h>
#include <string>
#include <algorithm>
#include <vector>
#include <set>
#include <queue>
#include <map>
#include <functional>

using namespace std;
#define lli long long int
const int N = 111;
double M = 1e7;

int r[200], a[200][200];

bool can(lli k, lli req, lli s) {
	return (100ll * s >= 90 * k * req && 100ll * s <= 110 * k * req);
}

pair<int, int> getLH(lli req, lli s) {
	int k = s / req;
	if (can(k, req, s)) {}
	else if (can(k - 1, req, s)) {
		k = k - 1;
	}
	else if (can(k + 1, req, s)) {
		k = k + 1;
	}
	else {
		return make_pair(0, 0);
	}
	int l = k, h = k;
	while (l > 1 && can(l - 1, req, s)) --l;
	while (can(h + 1, req, s)) ++h;
	return make_pair(l, h);
}

int ptr[N], low[N], high[N];
int n, p;

bool update(int minL) {
	for (int i = 0; i < n; ++i) {
		for (; ptr[i] < p && ptr[i] < p; ++ptr[i]) {
			pair<int, int> b = getLH(r[i], a[i][ptr[i]]);
			if (b.second < minL) continue;
			low[i] = b.first; high[i] = b.second;
			break;
		}
		if (ptr[i] == p) return false;
	}
	return true;
}

int main() {
	ios_base::sync_with_stdio();
#ifdef FILE_IO
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif
	int T;
	cin >> T;
	for (int qq = 0; qq < T; ++qq) {
		cout << "Case #" << (qq + 1) << ": ";

		
		cin >> n >> p;
		for (int i = 0; i < n; ++i) {
			cin >> r[i];
		}
		for (int i = 0; i < n; ++i) for (int j = 0; j < p; ++j) {
			cin >> a[i][j];
		}
		for (int i = 0; i < n; ++i) sort(&a[i][0], &a[i][0] + p);

		memset(ptr, 0, N*sizeof(int));
		int ans = 0;
		for (int c = 1; c <= 2000000; ) {
			if (!update(c)) break;
			int mmin = low[0], mmax = high[0];
			for (int i = 1; i < n; ++i) { mmin = max(mmin, low[i]); mmax = min(mmax, high[i]); }
			if (mmin <= mmax) {
				++ans;
				for (int i = 0; i < n; ++i) ++ptr[i];
			}
			else ++c;
		}

		cout << ans;

		cout << endl;
	}
	return 0;
}
