#define _CRT_SECURE_NO_WARNINGS

#include <iostream>
#include <fstream>
#include <map>
#include <stack>
#include <queue>
#include <deque>
#include <set>
#include <cmath>
#include <vector>
#include <algorithm>
#include <string>
#include <bitset>
#include <memory.h>

using namespace std;

int dp[111][111][111][111];
int b, d;
int initial_hd;
bool open[111][111][111][111];

int go(int hd, int ad, int hk, int ak) {
	if (hk <= 0) {
		return 0;
	}
	if (hd <= 0) {
		return -2;
	}
	if (dp[hd][ad][hk][ak] != -1) {
		return dp[hd][ad][hk][ak];
	}
	if (open[hd][ad][hk][ak]) {
		return -2;
	}
	open[hd][ad][hk][ak] = true;

	int minTurns = INT_MAX;

	int tmp = go(hd - ak, ad, hk - ad, ak);
	if (tmp >= 0) {
		minTurns = min(minTurns, tmp + 1);
	}
	if (ad <= hk) {
		tmp = go(hd - ak, ad + b, hk, ak);
		if (tmp >= 0) {
			minTurns = min(minTurns, tmp + 1);
		}
	}
	tmp = go(initial_hd - ak, ad, hk, ak);
	if (tmp >= 0) {
		minTurns = min(minTurns, tmp + 1);
	}
	tmp = go(hd - max(0, ak - d), ad, hk, max(0, ak - d));
	if (tmp >= 0) {
		minTurns = min(minTurns, tmp + 1);
	}

	if (minTurns < INT_MAX) {
		dp[hd][ad][hk][ak] = minTurns;
	}
	else {
		dp[hd][ad][hk][ak] = -2;
	}
	open[hd][ad][hk][ak] = false;

	return dp[hd][ad][hk][ak];
}


int main() {
	ios_base::sync_with_stdio(false);
	ifstream cin("input.txt");
	ofstream cout("output.txt");


	int tests;
	cin >> tests;
	for (int test = 1; test <= tests; test++) {
		int hd, ad, hk, ak;
		cin >> hd >> ad >> hk >> ak >> b >> d;
		initial_hd = hd;
		memset(dp, -1, sizeof(dp));

		int ans = go(hd, ad, hk, ak);
		

		cout << "Case #" << test << ": ";
		if (ans == -2) {
			cout << "IMPOSSIBLE";
		}
		else {
			cout << ans;
		}
		cout << endl;
	}


	//system("pause");
	return 0;
}