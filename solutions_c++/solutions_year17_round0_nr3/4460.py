#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cmath>
#include <string>
#include <vector>
#include <stack>
#include <queue>
#include <set>
#include <cstring>
#include <map>
#include <cstdlib>
#include <ctime>
#include <cassert>
#include <bitset>
#define f first
#define s second
#define ll long long
#define ull unsigned long long
#define mp make_pair
#define pb push_back
#define vi vector <int>
#define ld long double
#define pii pair<int, int>
#define pll pair<ll, pair<ll,ll> >
using namespace std;    
const int N = int(3e5), mod = int(1e9)  + 7;
int T;

ll n,k;

map <pll,ll> ma;

ll get(ll n,ll a,ll b){
	if(ma.count(mp(n,mp(a,b)))) return ma[mp(n,mp(a,b))];
	ll res = 0;
	if(n == 0) return 0;
	if(n & 1){
		if(mp(n/2,n/2) >= mp(a,b)){
			res++;
			res += 2 * get(n / 2, a, b);
		}
		return ma[mp(n,mp(a,b))] = res;
	}
	else{
		ll x = n / 2;
		if(mp(x,x - 1) >= mp(a,b)){
			res++;
			res += get(x,a,b);
			res += get(x-1,a,b);
		}
		return ma[mp(n,mp(a,b))] = res;
	}
}

void solve(){
	cin >> n >> k;
	if(n == k){
		puts("0 0");
		return;
	}
	ll l = 0, r = n + 1;
	while(r - l > 1){
		ll m = (l + r) / 2;
		if(get(n,m,0) >= k) l = m;
		else r = m;
	}
	ll f = l;
	l = 0, r = f + 1;
	while(r - l > 1){
		ll m = (l + r) / 2;
		if(get(n,f,m) >= k) l = m;
		else r = m;
	}
	printf("%lld %lld\n", f, l);
}

int main () {
	freopen("in","r",stdin);
	freopen("out","w",stdout);
	scanf("%d",&T);
	for(int tt=1;tt<=T;tt++){
		printf("Case #%d: ",tt);
		solve();
	}

return 0;
}