#include <bits/stdc++.h>

#define maxn 1100
#define sq 333
#define logn 23
#define inf 0x3F3F3F3F
#define linf 0x3F3F3F3F3F3F3F3FLL
#define eps 1e-9
#define pb push_back
#define mp make_pair
#define mod 1000000007LL

using namespace std;

typedef long double ld;
typedef long long ll;
typedef unsigned long long ull;
typedef pair<int, int> pii;
typedef vector<int> vi;
typedef vector<pii> vii;
typedef priority_queue<pii, vii, greater<pii> > pq;

#ifdef ONLINE_JUDGE
#define debug(args...)
#else
#define debug(args...) fprintf(stderr,args)
#endif

struct pank {
	ll h, r;

	pank() {}
	bool operator < (pank a) const {
		return r > a.r;
	}
} v[maxn];

int t, n, k;
ll pd[maxn][maxn];
int vis[maxn][maxn];

ll borda(int i) {
	return 2 * v[i].r * v[i].h;
}

ll area(int i) {
	return v[i].r * v[i].r;
}

ll f(int i, int rem) {
	if(rem == 0) {
		return 0;
	}
	if(i >= n) {
		return -linf;
	}
	ll &p = pd[i][rem];
	if(!vis[i][rem]) {
		vis[i][rem] = 1;
		p = max(f(i+1, rem-1) + borda(i), f(i+1, rem));
	}
	return p;
}

int main() {
	scanf("%d", &t);
	for(int cas = 1; cas <= t; ++cas) {
		scanf("%d %d", &n, &k);
		for(int i = 0; i < n; ++i) {
			scanf("%lld %lld", &v[i].r, &v[i].h);
		}
		sort(v, v+n);
		memset(vis, 0, sizeof vis);
		ll ans = 0;
		for(int i = 0; i <= n-k; ++i) {
			ans = max(ans, (f(i+1, k-1) + borda(i) + area(i)));
		}
		cout<<"Case #"<< cas << ": "<< std::setprecision(8) << std::fixed <<(M_PI * (long double)ans)<<endl;//%.7lf\n", cas, M_PI * (long double)ans);
	}

	return 0;
}