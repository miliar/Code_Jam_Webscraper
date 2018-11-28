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
int ar[10000010];

int main() {

#ifndef ONLINE_JUDGE
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif
	ios_base::sync_with_stdio(false);

	int t, k;
	string s;

	int c = 0;
	cin >> t;
	while (t--) {
		c++;
		cin >> s >> k;

		int ans = 0;
		for (int i = 0; i <= SZ(s) - k; ++i) {
			if (s[i] == '-') {
				ans++;
				for (int j = i; j < i + k; ++j) {
					if (s[j] == '-') {
						s[j] = '+';
					} else {
						s[j] = '-';
					}
				}
			}
		}
		cout << "Case #" << c << ": ";
		if (SZ(s) == count(ALL(s), '+')) {
			cout << ans << endl;
		} else {
			cout << "IMPOSSIBLE" << endl;
		}
	}

	return 0;
}
