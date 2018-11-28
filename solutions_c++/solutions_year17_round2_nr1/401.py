#include <stdio.h>
#include <algorithm>
#include <string>
#include <sstream>
#include <queue>
#include <map>
#include <tuple>
#include <iostream>

using namespace std;

void solve() {
	int d, n;
	cin >> d >> n;
	double time = 0;
	for (int i = 0; i < n; ++i) {
		int k, s;
		cin >> k >> s;
		double t = double(d - k) / s;
		time = max(time, t);
	}
	printf("%.9lf\n", d / time);
}

#define DIR "C:/Users/dmarin3/Downloads/"
#define PROBLEM "A"

#define LARGE
//#define TEST

int main() {
#ifdef LARGE
	freopen(DIR PROBLEM "-large.in", "rt", stdin);
#elif defined(TEST)
	freopen("input.txt", "rt", stdin);
#else
	freopen(DIR PROBLEM "-small-attempt0.in", "rt", stdin);
#endif
	freopen("output.txt", "wt", stdout);

	int t;
	cin >> t;
	for (int i = 0; i < t; ++i) {
		cout << "Case #" << (i + 1) << ": ";
		solve();
	}
}
