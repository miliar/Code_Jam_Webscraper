#include <iostream>
#include <vector>
#include <map>
#include <algorithm>
#include <cstdlib>
#include <cstdio>
#include <string>
using namespace std;
#define x first
#define y second
int n;
long double d;
bool check(long double m, vector<pair<long double, long double>> &a) {
	for (int i = 0; i < a.size(); i++) {
		if (a[i].y >= m)
			continue;
		if ((m * a[i].x / (m - a[i].y)) < (long double)d)
			return false;
	}
	return true;
}
void solve() {
	cin >> d >> n;
	vector<pair<long double, long double>> a(n);
	for (int i = 0; i < n; i++) {
		cin >> a[i].x >> a[i].y;
	}
	long double l = 1, r = 9000000000000000000;
	while (r - l > 0.000001) {
		long double m = (l + r) / 2;
		if (check(m, a))
			l = m;
		else 
			r = m;
	}
	cout << l;
	return;
}
void solve2() {
	cin >> d >> n;
	vector<pair<long double, long double>> a(n);
	for (int i = 0; i < n; i++) {
		cin >> a[i].x >> a[i].y;
	}
	cout << d << " " << n << endl;
	for (int i = 0; i < n; i++) {
		cout << a[i].x << " " << a[i].y << endl;
	}
	exit(0);
}
int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(nullptr);
	cout.tie(nullptr);
	cout.precision(20);
	//freopen("in.txt", "r", stdin);
	//freopen("out.txt", "w", stdout);
	int t;
	cin >> t;
	for (int i = 0; i < t; i++) {
		cout << "Case #" << i + 1 << ": ";
		solve();
		cout << endl;
	}

	return 0;
}
