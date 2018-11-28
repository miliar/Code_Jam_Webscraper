#define _CRT_SECURE_NO_WARNINGS
#define _USE_MATH_DEFINES
#include <cstdio>
#include <iostream>
#include <algorithm>
#include <cmath>
#include <vector>
#include <set>
#include <string>
#include<iomanip>
using namespace std;

typedef long long ll;

const double eps = 1e-9;

double d;

int n;

vector<pair<double, double> > v, v1;

void solve() {
	cin >> d >> n;
	v.resize(n);
	v1.resize(n);
	for (int i = 0; i < n; ++i) {
		cin >> v[i].first >> v[i].second;
	}
	for (int i = 0; i < n; ++i) {
		v1[i].second = v[i].first;
		v1[i].first = (d - v[i].first) / v[i].second;
	}
	sort(v1.begin(), v1.end());
	cout << fixed << setprecision(9) << d / v1.back().first;
}

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int nT;
	cin >> nT;
	for (int i = 0; i < nT; ++i) {
		cout << "Case #" << i + 1 << ": ";
		solve();
		cout << endl;
	}
	return 0;
}