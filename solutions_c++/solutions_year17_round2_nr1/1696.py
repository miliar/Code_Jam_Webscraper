// OI.cpp : Defines the entry point for the console application.

#include "stdafx.h"

#include <algorithm>
#include <iostream>
#include <fstream>
#include <cstdlib>
#include <cstring>
#include <climits>
#include <string>
#include <cstdio>
#include <vector>
#include <queue>
#include <stack>
#include <cmath>
#include <ctime>
#include <map>
#include <set>
using namespace std;

int T;
int d, n;

bool cmp(pair<int, int> x, pair<int, int> y) {
	if (x.first == y.first)
		return x.second > y.second;
	return x.first > y.first;
}

int main() {
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	cin >> T;
	for (int cse = 1; cse <= T; cse++) {
		cin >> d >> n;
		vector<pair<int, int>> a;
		for (int i = 0; i < n; i++) {
			int t1, t2;
			cin >> t1 >> t2;
			a.push_back(make_pair(t1, t2));
		}
		sort(a.begin(), a.end(), cmp);
		double pre = 0;
		for (int i = 0; i < n; i++) {
			double cur = (d - a[i].first) / 1.0 / a[i].second;
			pre = max(cur, pre);
		}
		double ans = d / pre;
		//cout << "Case #" << cse << ": " << ans<<;
		printf("Case #%d: %.6lf\n", cse, ans);
	}
	return 0;
}
