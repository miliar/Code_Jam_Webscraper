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
const int N = 1e5;

void solve() {
	int tests;
	cin >> tests;
	for (int test = 0; test < tests; test++) {
		string s;
		int k;
		cin >> s >> k;
		int n = sz(s);
		int ans = 0;
		for (int i = 0; i + k - 1 < n; i++) {
			int cnt = 0;
			if (s[i] == '-'){
				for (int j = i; j <= i + k - 1; j++) {
					if (s[j] == '-')
						s[j] = '+';
					else
						s[j] = '-';
				}
				ans++;
			}
		}
		bool ok = true;
		for (int i = 0; i < n; i++) {
			if (s[i] != '+')
				ok = false;
		}
		cout << "Case #" << test + 1 << ": ";
		if (!ok)
			cout << "IMPOSSIBLE" << endl;
		else
			cout << ans << endl;
	}
}

int main() {
#ifdef _DEBUG
	freopen("A-large (1).in", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif
	cout.sync_with_stdio(false);
	cin.tie(0);
	srand(time(NULL));
	solve();
	return 0;
}