#include<bits/stdc++.h>
using namespace std;
typedef long long int ll;
typedef vector<int> vi;
typedef vector<char> vc;
typedef pair<int, int> pi;
const int mod = 1e9 + 7;
const double EPS = 1e-9;
const int INF = 1 << 29;
#define mp make_pair
#define el putchar('\n')
#define sp putchar(' ')
#define Fill(a,val) memset(a,val,sizeof a)
#define all(a) a.begin(),a.end()
#ifndef ONLINE_JUDGE
#define tr(a, it) for (decltype(a.begin()) it = a.begin(); it != a.end(); ++it)
#else
#define tr(a, it) for (typeof(a.begin()) it = a.begin(); it != a.end(); ++it)
#endif
#define in(n) scanf("%d",&n)
#define inl(n) scanf("%lld",&n)
#define out(n) printf("%d",n);
#define outl(n) printf("%lld",n);

int const NN = 1e3 + 5;
ll R[NN], H[NN];
pair<ll, ll>p[NN];
const double PI = 2.0*acos(0);

void solve(ll n, ll k){
	double ans = 0;
	for (ll i = 1; i <= n; ++i){
		double ar = PI * 1.0 * R[i] * R[i] + 2.0 * PI * 1.0 * R[i] * H[i];
		ll req = k - 1;
		for (ll j = n; j >= 1 && req > 0; --j){
			ll idx = p[j].second;
			if (idx == i)continue;
			if (R[idx] > R[i])continue;
			req--;
			ar += 2.0 * PI * p[j].first;
		}
		if (req == 0){
			ans = max(ans, ar);
		}
	}
	printf("%.15lf\n", ans);
}

int main(){
	freopen("ip.in", "r", stdin);
	freopen("op.out", "w", stdout);
	int t; in(t);
	for (int cs = 1; cs <= t; ++cs){		
		ll n, k; cin >> n >> k;
		for (ll i = 1; i <= n; ++i)cin >> R[i] >> H[i], p[i] = mp(R[i] * H[i], i);
		sort(p + 1, p + n + 1);
		printf("Case #%d: ",cs);
		solve(n, k);
	}
	return 0;
}