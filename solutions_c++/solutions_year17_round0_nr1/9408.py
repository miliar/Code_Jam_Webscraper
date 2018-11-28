#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <cmath>
#include <memory.h>
#include <vector>
#include <queue>
#include <deque>
#include <string>
#include <stack>
#include <ctime>
#include <set>
#include <map>
#include <list>
#include <memory.h>
#include <cstring>

using namespace std;

void solve() {
	int k, ans = 0;
	string s;
	cin >> s >> k;
	for (int i = 0; i < s.length() - k + 1; ++i) {
		if (s[i] == '-') {
			for (int j = i; j < i + k; ++j) {
				if (s[j] == '-') {
					s[j] = '+';
				} else {
					s[j] = '-';
				}
			}
			//cout << s << endl;
			++ans;
		}
	}
	for (int i = s.length() - k + 1; i < s.length(); ++i) {
		if (s[i] == '-') {
			cout << "IMPOSSIBLE" << endl;
			return;
		}
	}
	cout << ans << endl;
}

int main() {
	freopen("input.txt", "r", stdin); 
	freopen("output.txt", "w", stdout);

	int n;
	cin >> n;
	for (int i = 0; i < n; ++i) {
		cout << "Case #" << i + 1 << ": ";
		solve();
	}
	
	return 0;
}

