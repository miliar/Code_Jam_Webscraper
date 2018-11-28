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

vector < int > p;
vector < int > k, s;
inline bool cmp(int i, int j) {
	return k[i] > k[j];
}
void solve(int cs) {
	cout << "Case #" << cs << ": ";
	int d, n; cin >> d >> n;
	p.resize(n);
	k.resize(n); s.resize(n);
	rep(i,0,n-1) {
		cin >> k[i] >> s[i];
		p[i] = i;
	}
	sort(all(p),cmp);
	double res; bool ok = 0;
	rep(ii,0,n-1) {
		int i = p[ii];
		double tim = (d-k[i]-0.0)/(s[i]*1.0);
		if(!ok) res = tim;
		updmax(res, tim);
		ok = 1;
	}
	cout << setprecision(10) << fixed << d*1.0/res << endl;
}

int main() {
	#ifdef accepted
		freopen(".in", "r", stdin);
		freopen(".out", "w", stdout);
	#endif
	onlycin;
	int test; cin >> test;
	rep(i,1,test) solve(i);
	
	return 0;
}