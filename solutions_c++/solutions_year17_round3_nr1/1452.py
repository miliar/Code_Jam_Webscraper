#include <bits/stdc++.h>
#include <ext/hash_map>
#include <ext/numeric>

using namespace std;
using namespace __gnu_cxx;

#define REP(i,n) for( (i)=0 ; (i)<(n) ; (i)++ )
#define rep(i,x,n) for( (i)=(x) ; (i)<(n) ; (i)++ )
#define REV(i,n) for( (i)=(n) ; (i)>=0 ; (i)-- )
#define FORIT(it,x) for( (it)=(x).begin() ; (it)!=(x).end() ; (it)++ )
#define foreach(it,c) for(__typeof((c).begin()) it=(c).begin();it!=(c).end();++it)
#define rforeach(it,c) for(__typeof((c).rbegin()) it=(c).rbegin();it!=(c).rend();++it)
#define foreach2d(i, j, v) foreach(i,v) foreach(j,*i)
#define all(x) (x).begin(),(x).end()
#define rall(x) (x).rbegin(),(x).rend()
#define SZ(x) ((int)(x).size())
#define MMS(x,n) memset(x,n,sizeof(x))
#define mms(x,n,s) memset(x,n,sizeof(x)*s)
#define pb push_back
#define mp make_pair
#define NX next_permutation
#define UN(x) sort(all(x)),x.erase(unique(all(x)),x.end())
#define CV(x,n) count(all(x),(n))
#define FIND(x,n) find(all(x),(n))-(x).begin()
#define ACC(x) accumulate(all(x),0)
#define PPC(x) __builtin_popcount(x)
#define LZ(x) __builtin_clz(x)
#define TZ(x) __builtin_ctz(x)
#define mxe(x) *max_element(all(x))
#define mne(x) *min_element(all(x))
#define low(x,i) lower_bound(all(x),i)
#define upp(x,i) upper_bound(all(x),i)
#define NXPOW2(x) (1ll << ((int)log2(x)+1))
#define PR(x) cout << #x << " = " << (x) << endl ;

typedef unsigned long long ull;
typedef long long ll;
typedef vector<int> vi;
typedef vector<vector<int> > vvi;
typedef pair<int, int> pii;

const int OO = (int) 2e9;
const double eps = 1e-9;

#ifndef M_PI
#define M_PI 3.1415926535897932384626433832795
#endif

const int N = 1001;

int n, k;
pii a[N];

ll dp[N][N];
int vis[N][N];
int vid;

ll calc(int idx, int rem) {
	if (rem == 0)
		return 0;
	if (idx == n)
		return -OO;
	ll &ret = dp[idx][rem];
	if (vis[idx][rem] == vid)
		return ret;
	vis[idx][rem] = vid;
	ret = calc(idx + 1, rem);
	if (ret < 0)
		ret = 0;
	ll cur = a[idx].first * 2LL * a[idx].second;
	ll v = calc(idx + 1, rem - 1);
	if (v >= 0)
		ret = max(ret, v + cur);
	return ret;
}

int main() {
	std::ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);
//#ifndef ONLINE_JUDGE
	freopen("A-large.in", "rt", stdin);
	freopen("out.txt", "wt", stdout);
//#endif
	int t, tt = 1;
	cin >> t;
	while (t--) {
		cin >> n >> k;
		for (int i = 0; i < n; i++)
			cin >> a[i].first >> a[i].second;
		sort(a, a + n, greater<pii>());
		ll res = 0;
		vid++;
		for (int i = 0; i < n; i++) {
			ll v = calc(i + 1, k - 1);
			if (v >= 0)
				res = max(res, v + a[i].first * 1LL * a[i].first + a[i].first * 2LL * a[i].second);
		}
		double ans = res * M_PI;
		cout << fixed << setprecision(6);
		cout << "Case #" << tt++ << ": " << ans << "\n";
	}
	return 0;
}
