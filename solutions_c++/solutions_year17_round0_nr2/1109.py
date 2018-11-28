#include <cmath>
#include <cstdio>
#include <algorithm>
#include <iostream>
#include <vector>
#define int long long
using namespace std;

signed main() {
	int T; cin >> T;
	for(int tc = 1; tc <= T; ++tc) {
		string s; cin >> s;
		int n = s.size();
		for(int i = n-1; i >= 1; --i) {
			if(s[i-1] > s[i]) {
				--s[i-1];
				for(int j = i; j < n; ++j)
					s[j] = '9';
			}
		}
		printf("Case #%lld: ", tc);
		bool print = false;
		for(int i = 0; i < n; ++i) {
			if(s[i] != '0') print = true;
			if(print) cout << s[i];
		}
		cout << endl;
	}
}
