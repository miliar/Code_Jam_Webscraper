#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include<iomanip>
#include <cassert>
#include<algorithm>

#include<string>
#include<vector>
#include<set>
#include <queue>
using namespace std;

#define forn(i, n) for(int i = 0; i < int(n); ++i)
#define sz(a) int(a.size())
#define mp make_pair
typedef long long li;


li toLI(string s) {
	li ans = 0;
	for (int i = 0; i < s.length(); i++) {
		ans *= 10LL;
		ans += (s[i] - '0');
	}
	return ans;
}
void solve() {
	int tests;
	cin >> tests;
	for (int t = 0; t < tests; t++) {
		string n;
		cin >> n;
		li ans = 0;
		for (int i = 0; i < n.length() - 1; i++) {
			ans *= 10LL;
			ans += 9;
		}
		string ans2;
		bool ok = true;
		for (int i = 0; i < n.length(); i++) {
			if (i == 0 || n[i] > n[i - 1]) {
				if (!(i == 0 && n[i] == '1')) 
					ans2.push_back(n[i] - 1);
				for (int j = i + 1; j < n.length(); j++) {
					ans2.push_back('9');
				}
			//	cout << ans << endl;
				ans = max(ans, toLI(ans2));
				for (int j = i + 1; j < n.length(); j++) {
					ans2.pop_back();
				}
				if (!(i == 0 && n[i] == '1'))  ans2.pop_back();
			}
			if (i != 0 && n[i] < n[i - 1]) {
				ok = false;
				break;
			}
			ans2.push_back(n[i]);
		}
		
		
		if (ok ) ans = max(ans, toLI(ans2));
		cout << "Case #" << t +1<< ": " << ans << endl;
	}
}

int main() {
#if _DEBUG
	cout << setprecision(15) << fixed;
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif

	solve();

	return 0;
}