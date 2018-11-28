#include <bits/stdc++.h>

#define all(a) (a).begin(), (a).end()
#define sz(a) (int)(a).size()
#define pb push_back

using namespace std;

int main()
{

	//ifstream cin("input.txt");
	//ofstream cout("output.txt");

	ios_base::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);

	ifstream cin("input.txt");
	ofstream cout("output.txt");

	int tt;
	cin >> tt;

	for (int test = 1; test <= tt; ++test) {
		cout << "Case #" << test << ": ";
		string s;
		cin >> s;
		int k;
		cin >> k;
		int ans = 0;
		for (int i = 0; i + k - 1 < sz(s); ++i) {
			if (s[i] == '-') {
				for (int j = i; j <= i + k - 1; ++j) {
					if (s[j] == '+') {
						s[j] = '-';
					} else {
						s[j] = '+';
					}
				}
				++ans;
			}
		}
		bool ok = true;
		for (int i = 0; i < sz(s); ++i) {
			if (s[i] == '-') {
				ok = false;
				break;
			}
		}
		if (ok) {
			cout << ans << "\n";
		} else {
			cout << "IMPOSSIBLE\n";
		}
	}

}
