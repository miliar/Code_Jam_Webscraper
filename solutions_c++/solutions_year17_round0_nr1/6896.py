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

int main() {
	#ifdef accepted
		freopen(".in", "r", stdin);
		freopen(".out", "w", stdout);
	#endif
	onlycin;
	cin >> t;
	rep(test,1,t) {
		string s; int k; cin >> s >> k;
		rep(i,0,sz(s)-1) {
			val[i] = 0;
			if(s[i] == '-') s[i] = '0';
			else s[i] = '1';
		}	
		int tmp = 0, res = 0;	
		rep(i,0,sz(s)-1) {
			tmp += val[i];
			if(tmp&1) {
				if(s[i] == '1') s[i] = '0';
				else s[i] = '1';
			}
			if(s[i] == '1') continue;
			if(i+k > sz(s)) continue;
			tmp++;
			res++;
			s[i] = '1';
			val[i+k]--;
		}
		cout << "Case " << "#" << test << ": ";
		bool bad = 0;
		rep(i,0,sz(s)-1) if(s[i] == '0') bad = 1;
		if(bad) cout << "IMPOSSIBLE\n";
		else cout << res << nxtl;
	}

	return 0;
}