#include <bits/stdc++.h>
using namespace std;
#define all(v) (v).begin(),(v).end()
#define pb push_back
#define sqr(x) ((x)*(x))
#define mp make_pair
#define ones(x) __builtin_popcount(x)
#define fast_io() ios_base::sync_with_stdio(0);cin.tie(0);
#define debug(x) cout << #x << ": " << x << endl;
#define REP(i,x,y) for(int (i)=(x);(i)<(y);(i)++)
#define REPIT(it,A) for(auto it = (A.begin()); it!=A.end();it++)
#define fst first
#define snd second
#define itm1 fst.fst
#define itm2 fst.snd
#define itm3 snd
#define mt(a,b,c) mp(mp(a,b),c)
#define sz(v) int(v.size())

typedef pair<int,int> ii;
typedef long long ll;
typedef unsigned long long ull;
typedef long double ld;
typedef pair< ii, int > tri;
typedef unsigned int uint;

const double PI = acos(-1);
const int  INF = 2e9;
const ll LINF = 1e18 + 5;
const ll MOD = 1e9 + 7;
const int MAXN = 1e5 + 5;
const int MN = 1e6 + 2;



ll val[MN];
ll c[MN]; 

void print(int tt){
	cout << "Case #" << tt << ": ";
}

pair< ll, ll > solve(ll n, ll k){
	map< ll, ll > mapa;	
	mapa.clear();
	map< ll, ll > :: iterator it;
	ll l = n, r = n + 1;
	ll c1 = 1, c2 = 0;
	while(l > 1){
		mapa[l] += c1;
		mapa[r] += c2;
		if(l % 2 == 0){
			c2 = 2 * c2 + c1;
			l = (l - 1)/2;
			r = l + 1;
		}
		else{
			c1 = 2 * c1 + c2;
			l = l / 2;
			r = l + 1;
		}
	}
	if(l == 1){
		mapa[2] += c2;
		mapa[1] += (c1 + c2);
	}
	if(l == 0){
		mapa[1] += c2;
	}

	int cnt = mapa.size();
	int tmp = cnt;
//	debug(cnt);
	for(it = mapa.begin(); it != mapa.end(); ++it){
		val[tmp - 1] = it -> first;
		c[tmp - 1] = it -> second;
		tmp--;
	}
	
//	for(int i = 0; i < cnt; ++i){
//		cout << "(" << val[i] << ", " << c[i] << ")" << endl; 
//	}

	ll cur = k;
	int idx = -1;
	for(int i = 0; i < cnt; ++i){
		cur -= c[i];
		if(cur <= 0){
			idx = i;
			break;
		}
	}

	ll elegido = val[idx];
//	debug(elegido);
	ll mid = (elegido - 1) / 2;
	ll x = mid;
	ll y = elegido - 1 - mid;
	if(x < y) swap(x, y);
	return mp(x, y);	
}

int main(){
	fast_io();
	int tc; cin >> tc;
	ll n, k; 
	for(int tt = 1; tt <= tc; ++tt){
		print(tt);
		cin >> n >> k;
		pair< ll, ll > ret  = solve(n, k);
		cout << ret.first << " " << ret.snd << endl; 
	}

	return 0;
}

















