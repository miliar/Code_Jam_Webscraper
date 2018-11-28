#include <iostream>
#include <cstdio>
#include <cassert>
#include <string>
#include <vector>
#include <algorithm>
#include <tuple>

using namespace std;

int d, n;
long long p[1001];
long long s[1001];

void read() {
	cin >> d;
	cin >> n;
	for (int i = 0; i < n; i++) {
		cin >> p[i];
		cin >> s[i];
	}

}

void solve(int test) {
	cout << "Case #" << test + 1 << ": ";

	double res = 0;
	double t = 0;

	for (int i = 0; i < n; i++) {
		t = max((double(d - p[i]) / s[i]), t);
	}

	res = d / t;

	printf("%.8f\n", res);
}

int main() {
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);

	int testCount;
	cin >> testCount;

	for (int test = 0; test < testCount; test++) {
		read();
		solve(test);
	}

	return 0;
}