#include <bits/stdc++.h>
using namespace std;

#define rep(i, a, b) for(int i = (a); i < int(b); ++i)
#define rrep(i, a, b) for(int i = (a) - 1; i >= int(b); --i)
#define trav(it, v) for(typeof((v).begin()) it = (v).begin(); it != (v).end(); ++it)
#define all(v) (v).begin(), (v).end()
#define what_is(x) cerr << #x << " is " << x << endl;

typedef double fl;
typedef long long ll;
typedef pair<int, int> pii;
typedef vector<int> vi;
typedef vector<pii> vpi;

ll getSmallest(ll a){
	ll ten=1;
	rep(i,0,18)
		ten *= 10;
	int digit=0;
	int fixedDigit=-1;
	ll ans=0;
	while(ten > 0){
		int d=(a/ten)%10;
		if(fixedDigit >= 0)
			d = fixedDigit;
		else{
			if(d < digit){
				fixedDigit = digit;
				d = fixedDigit;
			}
			else{
				digit = d;
			}
		}
		ans += ten*d;
		ten /= 10;
	}
	return ans;
}

void solve(){
	ll N;
	scanf("%lld", &N);
	ll ten=1;
	rep(i,0,18)
		ten *= 10;
	ll ans=0;
	while(ten > 0){
		while((ans/ten)%10 != 9){
			ll tmpAns = ans + ten;
			if(getSmallest(tmpAns) <= N)
				ans = tmpAns;
			else
				break;
		}
		ten /= 10;
	}
	printf("%lld\n", ans);
}

int main(){
	int T;
	scanf("%d", &T);
	for(int i=1; i <= T; ++i){
		printf("Case #%d: ", i);
		solve();
	}
}
