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
	int n, p;
	cin >> n >> p;
	vector<int> count(p, 0);
	for (int i = 0; i < n; ++i) {
		int g;
		cin >> g;
		++count[g % p];
	}
	int answer = 0;
	if (p == 2) {
		answer = count[0] + (count[1] + 1) / 2;
	}
	if (p == 3) {
		answer = count[0] + min(count[1], count[2]) + (abs(count[1] - count[2]) + 2) / 3;
	}
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
