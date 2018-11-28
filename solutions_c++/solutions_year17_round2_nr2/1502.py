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
int n, R, O, Y, G, B, V;
vector<vector<int>> g;

int cmp(pair<char, int> x, pair<char, int> y) {
	if (x.second == y.second)
		return x.first < y.first;
	return x.second > y.second;
}

int main() {
	freopen("B-small-attempt0.in", "r", stdin);
	freopen("B-small-attempt0.out", "w", stdout);
	cin >> T;
	for (int cse = 1; cse <= T; cse++) {
		cin >> n >> R >> O >> Y >> G >> B >> V;
		if (R > Y + B || Y > R + B || B > R + Y) {
			printf("Case #%d: IMPOSSIBLE\n", cse);
			continue;
		}
		vector<pair<char, int>> col;
		col.push_back(make_pair('R', R));
		col.push_back(make_pair('Y', Y));
		col.push_back(make_pair('B', B));
		sort(col.begin(), col.end(), cmp);
		
		int t = col[1].second + col[2].second - col[0].second;
		int l = col[1].second - t;
		int r = col[2].second - t;
		string ans = "";
		for (int i = 0; i < t; i++) {
			ans += col[0].first;
			ans += col[1].first;
			ans += col[2].first;
		}

		for (int i = 0; i < l; i++) {
			ans += col[0].first;
			ans += col[1].first;
		}
		
		for (int i = 0; i < r; i++) {
			ans += col[0].first;
			ans += col[2].first;
		}
		cout << "Case #" << cse << ": " << ans << endl;
	}
	return 0;
}
