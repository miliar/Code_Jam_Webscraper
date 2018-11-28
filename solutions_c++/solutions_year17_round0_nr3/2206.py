#include<iostream>
#include<algorithm>
#include<string>
#include<set>
using namespace std;

#define sz(x) (int)(x.size())
#define fi(a, b) for(int i=a;i<b;++i)
#define fj(a, b) for(int j=a;j<b;++j)
#define fk(a, b) for(int k=a;k<b;++k)
#define mp make_pair
#define pb push_back
typedef long long ll;
typedef pair<int, int> pii;
typedef pair<ll, ll> pll;

///////////////

pll f(ll len){
	ll m = (len + 1) / 2;
	return mp(m - 1, len - m);
}

void solve(int test){
	ll mini = 0;
	ll maxi = 0;
	ll n;
	ll k;
	cin >> n;
	cin >> k;
	ll deg = 0;
	pll ans;
	while(true){
		if(k - (1LL << (deg)) > 0){
			k -= (1LL << (deg));
			n -= (1LL << (deg));
			++deg;
		}else{
			ll same = n / (1LL << deg);
			ll oth = n % (1LL << deg);
			ans = mp(same / 2, same / 2);
			if(oth >= k) ans = f(same + 1);
			else ans = f(same);
			break;
		}
	}

	cout << "Case #" << test + 1 << ": " << ans.second << " " << ans.first << endl;
}

int main(){
#ifndef _DEBUG
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
#endif

	int test;
	cin >> test;
	fi(0, test){
		solve(i);
	}

	return 0;
}