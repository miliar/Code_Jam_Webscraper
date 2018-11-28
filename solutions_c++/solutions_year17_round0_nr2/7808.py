#include <bits/stdc++.h>

using namespace std;

#define ll long long
#define pb push_back
#define mp make_pair
#define pii pair< int , int >
#define vii vector< int >
#define ff first
#define ss second
#define rep(i,n) for(int i=0;i<n;i++)
#define frep(i , a , b) for(int i = a;i <= b;i++)
#define fast cin.sync_with_stdio(0);cin.tie(0);
#define CASES int t;cin >> t;while(t--)
#define FI freopen ("in.txt", "r", stdin)
#define FO freopen ("out.txt", "w", stdout)
#define inf 0x7fffffff
const int MOD = 1e9 + 7;
const int base = 1000000000;
const int base_digits = 9;

bool check(string x) {
	rep(i, x.length() - 1) if (x[i] > x[i + 1]) return 0; return 1;
}

int main()
{
	fast
	FO;
	int t; cin >> t;
	// cout<<t;
	rep(tc, t) {
		cout << "Case #" << tc + 1 << ": ";
		string s;
		// int x;
		cin >> s;
		// cin >> x;
		int len = s.length();
		if (len == 1) {
			cout << s << "\n";
			continue;
		}
		string ans = "";
		rep(i, len - 1) {
			if (s[i] > s[i + 1]) {
				if (s[i] == '1') {
					rep(j, i) {
						ans = ans + '9';
					}
				}
				else {
					while (s[i] == s[i - 1] && i > 0) {
						i--;
					}
					s[i]--;
					ans = s.substr(0, i + 1);
				}
				frep(j, i + 1, len) {
					s[j] = '9';
				}
				ans = ans + s.substr(i + 1);
				break;
			}
		}
		if (ans.length())
			cout << ans << "\n";
		else cout << s << "\n";



		// for (int i = x; i >= 1; i--) {
		// 	if (check(to_string(i))) {
		// 		cout << i << "\n";
		// 		break;
		// 	}
		// }
	}
}