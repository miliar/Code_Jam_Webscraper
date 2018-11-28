#include <bits/stdc++.h>
using namespace std;

typedef long long ll;
typedef unsigned long long int llu;
#define pb push_back
#define mp make_pair
#define X first
#define Y second
#define mem(a, v) memset(a, v, sizeof(a))
#define PI acos(-1)
#define S(a) scanf("%d",&a)
#define SL(a) scanf("%lld",&a)
#define S2(a, b) scanf("%d%d",&a,&b)
#define nl printf("\n")
#define deb(x) cout<<#x<<" : "<<x<<endl;
#define deb2(x, y) cout<<#x<<" : "<<x<<" | "<<#y<<" : "<<y<<endl;
#define deb3(x, y, z) cout<<#x<<" : "<<x<<" | "<<#y<<" : "<<y<<" | "<<#z<<" : "<<z<<endl;
#define debv(x) {cout<<#x<<" : "<<endl; for(int ii =0; ii < x.size(); ii++) cout<<x[ii]<<" "; cout<<endl; }
#define debarr(x, xs) {cout<<#x<<" : "<<endl; for(int ii =0; ii < xs; ii++) cout<<x[ii]<<" "; cout<<endl; }
//auto T=clock(); 
//cout<<double(clock()-T)/CLOCKS_PER_SEC<<'\n';
//cout << fixed << setprecision(10) << f(0, 0, 0) << "\n";
const ll mod = 1000000007LL;
const int lmt = 1000005;
const ll inf = 1LL<<58;

vector<pair<ll, ll> > cake;

bool cmp(pair<ll, ll> a, pair<ll, ll> b) {
	if(a.X == b.X)
		return a.Y > b.Y;
	return a.X > b.X;
}

int n, k;

ll dp[1005][1005][2];

ll solve(int idx, int cnt, int taken) {
	if(cnt == k)
		return 0;
	if(idx == n)
		return -inf;
	if(dp[idx][cnt][taken] != -1)
		return dp[idx][cnt][taken];
	ll ans = solve(idx+1, cnt, taken);
	ll r = cake[idx].X, h = cake[idx].Y;
	ll area = r*r + 2*r*h;
	if(taken)
		area -= r*r;
	ans = max(ans, solve(idx+1, cnt+1, 1) + area);
	return dp[idx][cnt][taken] = ans;
}

int main(){
	freopen("A-large.in", "r", stdin);
	freopen("out.txt", "w", stdout);
	int t;
	S(t);
	for(int tst = 1; tst <= t; tst++) {
		cake.clear();
		mem(dp, -1);
		S2(n, k);
		for(int i = 0; i < n; i++) {
			ll r, h;
			SL(r);
			SL(h);
			cake.pb(mp(r, h));
		}
		sort(cake.begin(), cake.end(), cmp);

		ll ans = solve(0, 0, 0);
		double x = (double)ans*PI;
		printf("Case #%d: %.9lf\n", tst, x);
	}
    return 0;
}