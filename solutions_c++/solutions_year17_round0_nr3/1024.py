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
const int INF = 1e9;
const ll MOD = 1e9 + 7;

const int MAXN = 1e5 + 5;

map<ll, ll> cnt;

void solve(int t){
	ll n, k;
	scanf("%lld%lld", &n, &k);
	cnt.clear();
	cnt[-n]++;
	ll last = 0;
	while(k){
		ll v = cnt.begin()->_1;
		ll cur_cnt = cnt.begin()->_2;
		ll dif = min(k, cur_cnt);
		if (dif == cur_cnt){
			cnt.erase(cnt.begin());
			cnt[v / 2] += dif;
			cnt[(v + 1) / 2] += dif;
		}
		k -= dif;
		last = -v;
	}
	printf("Case #%d: ", t);
	printf("%lld %lld\n", last / 2, (last - 1) / 2);
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
