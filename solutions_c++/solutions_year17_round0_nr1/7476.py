#include <bits/stdc++.h>
#define endl '\n'
#define mod 1000000007
typedef long long LL;
const int maxn = 1e5 + 2;
const LL inf = 1e18;
using namespace std;
inline void print(int x) {
	cout << x << endl;
}
inline void print(string s) {
	cout << s << endl;
}
int main() {
	ios_base::sync_with_stdio(false); cin.tie(0);
	int t; cin >> t;
	for(int i = 1; i <= t; i++) {
		string s; cin >> s;
		int k, cnt = 0; cin >> k;
		bool ok = 1;
		for(int j = 0; j <= s.length() - k; j++) {
			if(s[j] == '+') continue;
			++cnt;
			for(int c = j; c < j + k; c++) {
				s[c] = (s[c] == '+'? '-': '+');
			}
		}
		for(int j = 0; j < s.length(); j++) ok &= (s[j] == '+');
		cout << "Case #" << i << ": ";
		ok? print(cnt): print("IMPOSSIBLE");
	}
	return 0;
}
