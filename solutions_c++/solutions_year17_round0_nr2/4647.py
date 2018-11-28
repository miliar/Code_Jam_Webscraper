#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <vector>
#include <stdio.h>
#include <set>
#include <algorithm>
#include <string.h>
#include <assert.h>
#include <time.h>
#include <string>
#include <queue>
#include <random> 
#include <map>
#include <numeric>
using namespace std;
typedef long long li;
#define mp make_pair
#define sz(a) (int)a.size()
const int N = 30;
const int K = 10;
li dp[N][K][2];
string s;
li pows[N];

li calc(int pos, int last, int less) {
	if (dp[pos][last][less] != -1LL)
		return dp[pos][last][less];
	
	if (pos >= sz(s)) {
		return 0;
	}

	dp[pos][last][less] = -1e18 - 2;
	int d = s[pos] - '0';
	int lastd = (less ? 9 : d);
	for (int digit = last; digit <= lastd; digit++) {
		int st = sz(s) - pos - 1;
		int nless = (less | (digit < d));
		li nd = pows[st] * (li)digit;

		dp[pos][last][less] = max(dp[pos][last][less], nd + calc(pos + 1, digit, nless));
	}
	return dp[pos][last][less];
}

void solve() {
	int tests;
	cin >> tests;

	pows[0] = 1;
	for (int i = 1; i < N; i++) {
		pows[i] = pows[i - 1] * 10LL;
	}
	for (int t = 0; t < tests; t++){
		cin >> s;
		for (int i = 0; i < N; i++) {
			for (int k = 0; k < K; k++) {
				dp[i][k][0] = dp[i][k][1] = -1LL;
			}
		}
		cout << "Case #" << t + 1 << ": " << calc(0, 0, 0) << endl;
	}
}

int main() {
#ifdef _DEBUG
	freopen("B-large (1).in", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif
	cout.sync_with_stdio(false);
	cin.tie(0);
	srand(time(NULL));
	solve();
	return 0;
}