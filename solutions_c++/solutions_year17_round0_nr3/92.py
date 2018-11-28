#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <memory.h>
#include <math.h>
#include <assert.h>
#include <queue>
#include <map>
#include <set>
#include <string>
#include <algorithm>
#include <iostream>
#include <functional>
#include <unordered_map>
#include <unordered_set>
#include <list>
#include <bitset>

using namespace std;
typedef pair<int, int> Pi;
typedef long long ll;
#define pii Pi
#define pll PL
#define Fi first
#define Se second
#define pb(x) push_back(x)
#define sz(x) ((int)(x).size())
#define rep(i, n) for(int i=0;i<n;i++)
#define all(x) (x).begin(), (x).end()
typedef tuple<int, int, int> t3;
typedef pair<ll, ll> PL;
typedef long double ldouble;

map <ll, ll> M;

void solve(){
	M.clear();
	ll n, k; cin >> n >> k;
	M[n]++;
	ll c = 0;
	while(1){
		auto it = --M.end();
		ll t = it->Se;
		c += t;
		ll a = it->Fi / 2;
		ll b = (it->Fi - 1) / 2;
		M.erase(it);
		if(a > 0)M[a] += t;
		if(b > 0)M[b] += t;
		if(c >= k){
			printf("%lld %lld\n", a, b);
			return;
		}
	}
}

int main(){
	int Tc = 1; scanf("%d\n", &Tc);
	for(int tc=1;tc<=Tc;tc++){
		printf("Case #%d: ", tc);
		solve();
	}
}
