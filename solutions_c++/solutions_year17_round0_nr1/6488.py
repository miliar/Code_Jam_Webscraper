#include <bits/stdc++.h>

using namespace std;

#define INF 2000000000
#define MOD 1000000007
typedef long long ll;
typedef pair<int, int> P;


char flip(char c) {
	if (c=='-') {
		return '+';
	}
	return '-';
}

int main()
{
	int t;
	cin >> t;

	for (int ii = 1; ii <= t; ii++) {
		string s;
		cin >> s;
		int k;
		cin >> k;
		int l=0;
		int r=s.size()-1;
		int ret=0;
		while (true) {
			if (l>=r) {
				break;
			}
			if (s[l]=='-') {
				if (l+k-1<s.size()) {
					ret++;
					for (int i = 0; i < k; i++) {
						s[l+i] = flip(s[l+i]);
					}
				}

			}
			if (s[r]=='-') {
				if (r-k+1>=0) {
					ret++;
					for (int i = 0; i < k; i++) {
						s[r-i] = flip(s[r-i]);
					}
				}
			}
			l++;
			r--;
		}
		bool imp = false;
		for (int i = 0; i < s.size(); i++) {
			if (s[i]=='-') {
				imp = true;
			}
		}
		if (imp) {
			cout << "Case #" << ii << ": " << "IMPOSSIBLE" << "\n";
		} else {
			cout << "Case #" << ii << ": " << ret << "\n";
		}
	}
}
