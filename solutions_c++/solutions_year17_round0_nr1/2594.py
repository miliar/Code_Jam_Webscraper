#include <stdio.h>
#include <algorithm>
#include <string>
#include <iostream>

using namespace std;

void solve(string s, int k) {
	int r = 0, n = s.size();
	for (int i = 0; i < n; ++i) {
		if (s[i] == '-') {
			if (i + k > n) {
				cout << "IMPOSSIBLE";
				return; 
			}
			for (int j = 0; j < k; ++j)
				s[i + j] = s[i + j] == '-' ? '+' : '-';
			++r;
		}			
	}
	cout << r;
}

#define DIR "C:/Users/dmarin3/Downloads/"
#define PROBLEM "A"
#define ATTEMPT "0"

#define LARGE

int main() {
#ifndef LARGE
	freopen(DIR PROBLEM "-small-attempt" ATTEMPT ".in", "rt", stdin);
#else
	freopen(DIR PROBLEM "-large.in", "rt", stdin);
#endif
	freopen("output.txt", "wt", stdout);

	int t;
	cin >> t;
	for (int i = 0; i < t; ++i) {
		string s; 
		int k;
		cin >> s >> k;
		cout << "Case #" << (i + 1) << ": ";
		solve(s, k);
		cout << endl;
	}
}
