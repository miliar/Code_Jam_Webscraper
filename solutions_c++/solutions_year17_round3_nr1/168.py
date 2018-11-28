#include <iostream>
#include <stdio.h>
#include <vector>
#include <string>
#include <math.h>
#include <algorithm>
#include <map>
#include <set>
#include <set>

#define sz(x) ((int)x.size())
#define all(x) (x).begin(), (x).end()
#define pb(x) push_back(x)
#define mp(x, y) make_pair(x, y)

typedef long long int64;

using namespace std;

void solve() {
	long double pi = 4.0 * atan(1.0);
    int64 n, k;
	cin >> n >> k;
	vector<pair<int64, int64>> pancakes;
	for (int i = 0; i < n; ++i) {
		int64 r, h;
		cin >> r >> h;
		pancakes.pb(mp(r * h, r));
	}
	sort(all(pancakes));
	reverse(all(pancakes));
	long double answer = 0;
	for (int i = 0; i < n; ++i) {
		long double result = pi * pancakes[i].second * pancakes[i].second;
		result += 2 * pi * pancakes[i].first;
		int num = k - 1;
		for (int j = 0; j < n; ++j) {
			if (num == 0) break;
			if (j == i) continue;
			if (pancakes[j].second > pancakes[i].second) continue;
			--num;
			result += 2 * pi * pancakes[j].first;
		}
		if (num == 0) {
			answer = max(answer, result);
		}
	}
	cout.precision(25);
	cout << answer << endl;
}

int main() {
    int tests;
    cin >> tests;
    for (int test = 1; test <= tests; ++test) {
        cout << "Case #" << test << ": ";
        solve();
    }
    return 0;
}
