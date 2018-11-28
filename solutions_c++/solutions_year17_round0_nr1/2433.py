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
    int n;
	string s;
	cin >> s;
	n = sz(s);
	int k;
	cin >> k;
	int result = 0;
	for (int i = 0; i + k <= n; ++i) {
		if (s[i] == '-') {
			++result;
		    for (int j = 0; j < k; ++j) {
				if (s[i + j] == '+') {
					s[i + j] = '-';
				} else {
					s[i + j] = '+';
				}
			}
		}
	}
	for (int i = 0; i < n; ++i) {
		if (s[i] == '-') {
			cout << "IMPOSSIBLE" << endl;
			return;
		}
	}
	cout << result << endl;
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
