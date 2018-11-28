#include <bits/stdc++.h>
/*#include <ext/pb_ds/assoc_container.hpp>
#include <ext/pb_ds/tree_policy.hpp>
#include <ext/pb_ds/detail/standard_policies.hpp>*/
 
#define pb push_back
#define mp make_pair
#define sz(s) ((int)(s.size()))
#define all(s) s.begin(),s.end()
#define rep(i,a,n) for(int i=a;i<=n;++i)
#define per(i,n,a) for(int i=n;i>=a;--i)
#define onlycin ios_base::sync_with_stdio(false); cin.tie(0) 
using namespace std;
// using namespace __gnu_pbds;
typedef long long ll;
typedef unsigned long long ull;
/*typedef tree<
pair < int, int >,
null_type,
less< pair < int, int > >,
rb_tree_tag,
tree_order_statistics_node_update>
ordered_set;*/
// find_by_order() order_of_key()
const int MAXN = (int)5e5+228;
const char nxtl = '\n';
const int mod = (int)1e9+7;
const double eps = (double)1e-7;
template<typename T> inline bool updmin(T &a, const T &b) {return a > b ? a = b, 1 : 0;}
template<typename T> inline bool updmax(T &a, const T &b) {return a < b ? a = b, 1 : 0;}

int t, val[MAXN];
ll dp[2][20][10];
string s;

ll calc(ll num) {
	s.clear();
	while(num > 0ll) {
		s.pb(num%10ll+'0');
		num /= 10ll;
	}
	reverse(all(s));
	memset(dp,0,sizeof dp);
	dp[1][0][0] = 1;
	rep(i,0,sz(s)-1) {
		ll cur0 = 0, cur1 = 0;
		rep(last,0,9) {
			cur0 += dp[0][i][last];
			cur1 += dp[1][i][last];
			if(last > s[i]-'0') dp[0][i+1][last] += cur0;
			else if(last == s[i]-'0') {
				dp[1][i+1][last] += cur1;
				dp[0][i+1][last] += cur0;
			} else {
				dp[0][i+1][last] += cur1+cur0;
			}
		}
	}
	ll res = -1;
	rep(i,0,9) res += dp[0][sz(s)][i]+dp[1][sz(s)][i];
	return res;
}

int main() {
	#ifdef accepted
		freopen(".in", "r", stdin);
		freopen(".out", "w", stdout);
	#endif
	onlycin;
	cin >> t;
	rep(test,1,t) {
		ll num; cin >> num;
		ll res = calc(num);
		ll l = 0, r = num+1;
		while(r-l > 1ll) {
			ll mid = l+r>>1ll;
			if(calc(mid) < res) l = mid;
			else r = mid;
		}
		cout << "Case " << "#" << test << ": " << r << nxtl;
	}

	return 0;
}