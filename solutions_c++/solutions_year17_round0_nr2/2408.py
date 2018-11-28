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
    string s;
	cin >> s;
	int n = sz(s);
	for (int i = 0; i < n; ++i) {
		if (s.substr(i) < string(n - i, s[i])) {
			string result = s.substr(0, i) + string(1, s[i] - 1) + string(n - i - 1, '9');
			while (sz(result) > 0 && result[0] == '0') {
				result = result.substr(1);
			}
			cout << result << endl;
			return;
		}
	}
	cout << s << endl;
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
