#include <bits/stdc++.h>
#include <stdio.h>
#include <cstdio>
#include <unordered_map>

#define SZ(c) int(c.size())
#define ALL(c) c.begin(), c.end()
#define clr(a,b) memset(a,b,sizeof a)
#define fr first
#define sc second
#define pb push_back

typedef long long ll;
typedef unsigned long long ull;

using namespace std;

int main() {

#ifndef ONLINE_JUDGE
	freopen("input.txt", "r", stdin);
	freopen("output1.txt", "w", stdout);
#endif
	ios_base::sync_with_stdio(false);

	int t;
	string s;
	cin >> t;

	int c = 0;
	while (t--) {
		c++;
		cin >> s;

		int fir = -1;

		for (int i = 0; i < SZ(s) - 1; ++i) {
			if (s[i] > s[i + 1]) {
				fir = i;
				break;
			}
		}
		if (fir != -1) {
			while (s[fir] == s[fir - 1] && fir >= 1) {
				fir--;
			}
			s[fir]--;
			for (int i = fir + 1; i < SZ(s); ++i) {
				s[i] = '9';
			}
			if (s[0] == '0') {
				s = string(s.begin() + 1, s.end());
			}
			for (int i = 0; i < SZ(s); ++i) {
				if (s[i] == '0') {
					s[i] = '9';
				} else {
					break;
				}
			}
		}
		cout << "Case #" << c << ": ";
		cout << s << endl;
	}

	return 0;
}
