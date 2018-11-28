#include <bits/stdc++.h>

using namespace std;

typedef long long ll;
typedef vector<int> vi;
typedef pair<int, int> ii;

#define fastio ios_base::sync_with_stdio(false);
#define fi first
#define se second

vector<ll> v;

void gen(ll num, int last_d, int len){
	if(len == 19) return;
	ll x;
	
	for(int i = last_d; i <= 9; ++i){
		x = num * 10 + (ll)i;
		
		if(x <= 1000000000000000000)
			v.push_back(x);
		
		
		gen(x, i, len + 1);
	}
}

int main(){
	gen(0, 1, 0);
	sort(v.begin(), v.end());
	vector<ll>::iterator it;
	int T;
	ll n;
	
	scanf("%d", &T);
	
	for(int t = 1; t <= T; ++t){
		scanf("%lld", &n);
		it = upper_bound(v.begin(), v.end(), n);
		it--;
		printf("Case #%d: %lld\n", t, *it);
	}
	
	return 0;
}
