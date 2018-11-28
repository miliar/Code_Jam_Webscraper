#include <bits/stdc++.h>
using namespace std;

#define pb push_back
#define mp make_pair
typedef long long ll;
typedef pair<int, int> pii;
typedef vector<int> vi;
typedef complex<double> point;
#define xx real()
#define yy imag()

#define REP(i, a, b) for(int i = (a); i < (int)(b); i++)
#define REPN(i, a, b) for(int i = (a); i <= (int)(b); i++)
#define FA(it, x) for(__typeof((x).begin()) it = (x).begin(); it != (x).end(); it++)
#define SZ(x) (int)(x).size()
#define BE(x) (x).begin(), (x).end()
#define SORT(x) sort(BE(x))
#define _1 first
#define _2 second

#define x1 gray_cat_x1
#define y1 gray_cat_y1

template<class T> T gcd(T a, T b) { return b ? gcd(b, a % b) : a; }

#define file "I1"

const double EPS = 1e-9;
const double PI = acos(-1.);
const ll INF = 3e18;
const ll MOD = 1e9 + 7;

const int MAXN = 1e5 + 5;

ll hd, ad, hk, ak, b, d;

ll cnt1;

ll solve_d(ll y){
	ll ans = 0;
	ll cur_ak = ak;
	ll cur_hd = hd;
	
	for(; y > 0; ){
		if (cur_ak - d >= cur_hd){
			ans++;
			cur_hd = hd - cur_ak;
			if (cur_ak - d >= cur_hd){
				return INF;
			}
		} else {
			y--;
			ans++;
			cur_ak -= d;
			cur_hd -= cur_ak;
		}
	}
	
	for(ll v = cnt1; v > 1; ){
		if (cur_hd <= cur_ak){
			ans++;
			cur_hd = hd - cur_ak;
			if (cur_hd <= cur_ak){
				return INF;
			}
		} else {
			v--;
			ans++;
			cur_hd -= cur_ak;
		}
	}
	
	ans++;
	return ans;
}


void solve(int t){
	scanf("%lld%lld%lld%lld%lld%lld", &hd, &ad, &hk, &ak, &b, &d);
	cnt1 = 0;
	if (ad >= hk){
		cnt1 = 1;
	} else if (b == 0){
		cnt1 = (hk + ad - 1) / ad;
	} else {
		cnt1 = INF;
		ll x, y;
		for(y = 0; y < 1e5; y++){
			ll v = ad + y * b;
			x = (hk + v - 1) / v;
			cnt1 = min(cnt1, x + y);
		}
	}
	
	printf("Case #%d: ", t);
	
	
	ll cnt2 = (hd + ak - 1) / ak;
	
	//printf("%lld %lld ", cnt1, cnt2);
	
	if (cnt1 <= cnt2){
		printf("%lld\n", cnt1);
		return;
	}
	
	/*if (max(0ll, ak - d) * 2 >= hd){
		printf("IMPOSSIBLE\n");
		return;
	}*/
	
	ll ans = INF;
	ll d_lim = 0;
	if (d > 0){
		d_lim = (ak + d - 1) / d;
	}
	
	for(ll y = 0; y <= min((ll)1e6, d_lim); y++){
		ans = min(ans, solve_d(y));
	}
	for(ll y = max(0ll, d_lim - (ll)1e6); y <= d_lim; y++){
		ans = min(ans, solve_d(y));
	}
	
	if (ans == INF){
		printf("IMPOSSIBLE\n");
		return;
	}
	
	printf("%lld\n", ans);
}   

int main(){
#ifndef ONLINE_JUDGE
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
#endif
    //freopen(file".in", "r", stdin); freopen(file".out", "w", stdout);
    int t = 1;
    //cin >> t;
    cin >> t;
    for(int i = 1; i <= t; i++){
        solve(i);    
    }
}
