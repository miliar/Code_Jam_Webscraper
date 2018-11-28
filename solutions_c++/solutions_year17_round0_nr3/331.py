#include <vector>
#include <string>
#include <iostream>
#include <algorithm>
#include <queue>
#include <set>
#include <map>
#include <sstream>
#include <iomanip>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <ctime>
#include <cassert>
using namespace std;
typedef long long ll;
typedef double R;
#define pb push_back
#define mp make_pair
#define fi first
#define se second
#define FOR(i, s, t) for(i = (s); i < (t); i++)
#define RFOR(i, s, t) for(i = (s)-1; i >= (t); i--)

const R PI = acos(-1);
const int MAXN = 1<<20;
const int P = 1e9+7;

ll x;
ll a, b;
ll l, r;

ll sim(ll k){
	if(k > a+b){
		ll tot = a+b;
		l = (x-1)/2;
		r = (x) / 2;
		x = r;
		if(l == r){
			a = a*2 + b;
		}
		else{
			b = b*2 + a;
		}
		return tot;
	}
	else if(k <= a){
		l = (x-1)/2;
		r = (x) / 2;
		return k;
	}
	else{
		l = (x-2)/2;
		r = (x-1)/2;
		return k;
	}
}

int main(){
#ifdef LOCAL
	//freopen("in.txt", "r", stdin);
	//freopen("out.txt", "w", stdout);
#endif
	int T, i0;
	scanf("%d", &T);
	for(i0 = 1; i0 <= T; i0++){
		ll n, k;
		scanf("%lld%lld", &n, &k);
		x = n;
		a = 1;
		b = 0;
		while(k > 0){
			k -= sim(k);
			//printf("%lld %lld %lld\n", x, a, b);
		}
		printf("Case #%d: %lld %lld\n", i0, r, l);
	}
	return 0;
}
