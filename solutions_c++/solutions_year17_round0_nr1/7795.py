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

int main()
{
	fast
	FO;
	int t; cin >> t;
	// cout<<t;
	rep(tc, t) {
		cout << "Case #" << tc + 1 << ": ";
		string s; int k;
		cin >> s >> k;
		// cout << s << "\n";
		int len = s.length();
		int ans = 0;
		if (len < k) {
			rep(i, len) {
				if (s[i] == '-') {
					cout << "IMPOSSIBLE\n";
					// continue;
					ans = -1;
					break;
				}
			}
			if (ans >= 0)
				cout << ans << "\n";
			continue;
		}
		rep(i, len - k + 1) {
			if (s[i] == '-') {
				ans++;
				for (int j = i; j < i + k && j < len; j++) {
					s[j] = (s[j] == '-') ? '+' : '-';
				}
			}
		}
		// cout << s << "\n";
		rep(i, len) {
			if (s[i] == '-') {
				cout << "IMPOSSIBLE\n";
				ans = -1;
				break;
			}
		}
		if (ans >= 0)
			cout << ans << "\n";
	}
	return 0;
}