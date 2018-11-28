#define _CRT_SECURE_NO_WARNINGS
#pragma comment(linker, "/STACK:256000000")
#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <bitset>
#include <sstream>
#include <fstream>
#include <ctime>
#include <cstring>
#include <numeric>
#include <queue>
#include <cassert>
#include <unordered_map>

using namespace std;

typedef long long ll;
typedef double ld;

#define TASK "divisible"

int solve();

int main() {
#ifdef PoDuReM
	freopen("input.txt", "r", stdin), freopen("output.txt", "w", stdout);
#else
	//freopen(TASK".in", "r", stdin), freopen(TASK".out", "w", stdout);
#endif
	return solve();
}

const int dd = (int)1e3 + 1;

ld A[dd];

int solve() {
	ios_base::sync_with_stdio(0);
	int t;
	cin >> t;
	for (int i = 1; i <= t; ++i) {
		cout << "Case #" << i << ": ";
		int n, k;
		ld u;
		cin >> n >> k >> u;
		for (int i = 0; i < n; ++i)
			cin >> A[i];
		ld l = 0, r = 1;
		for (int i = 0; i < 100; ++i) {
			ld m = (l + r) / 2;
			ld F = 0;
			for (int i = 0; i < n; ++i)
				F += max(0.0, m - A[i]);
			if (F <= u)
				l = m;
			else
				r = m;
		}
		for (int i = 0; i < n; ++i)
			A[i] = max(A[i], l);
		ld ans = 1;
		for (int i = 0; i < n; ++i)
			ans *= A[i];
		cout.precision(7);
		cout << fixed << ans << "\n";
	}
	return 0;
}