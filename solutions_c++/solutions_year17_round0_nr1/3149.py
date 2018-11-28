#include <iostream>
#include <cstdio>
#include <algorithm>

using namespace std;

void solve_case() {
	string s;
	int k, res = 0;
	cin >> s >> k;
	for (int i=0; i < int(s.size()) - k + 1; i++) {
		if (s[i] == '-') {
			res++;
			for (int j=i; j<i+k; j++) {
				s[j] = '+' + '-' - s[j];
			}
		}
	}
	for (int i=int(s.size()) - k + 1; i<s.size(); i++) {
		if (s[i] == '-') {
			res = -1;
		}
	}
	if (res == -1) {
		cout << "IMPOSSIBLE" << endl;
	} else {
		cout << res << endl;
	}
}

int main() {
	int te;
	cin >> te;
	for (int tt=1; tt<=te; tt++) {
		cout << "Case #" << tt << ": ";
		solve_case();
	}
}

