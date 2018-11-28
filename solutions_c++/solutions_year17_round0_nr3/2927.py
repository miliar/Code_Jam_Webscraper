#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

int main(){
	int Test;
	scanf("%d\n", &Test);
	ll n, k;
	map<ll, ll> M;
	for(int test=1; test<=Test; test++){		
		scanf("%lld %lld\n", &n, &k);
		M.clear();
		M[n]=1; M[0]=0;
		ll x=0, y=0, a, b, l, r;
		//cout<<n<<" :: "<<k<<endl;
		while(1){
			a = (--M.end())->first;
			b = (--M.end())->second;
			M.erase(--M.end());
			l = (a-1LL)/2LL;
			r = a/2LL;
			x = y+1LL;
			y = x+b-1LL;
			//cout<<x<<" to "<<y<<endl;
			if(x<=k and k<=y){
				break;
			}
			M[l]+=b;
			M[r]+=b;
		}
		printf("Case #%d: %lld %lld\n", test, max(l, r), min(l, r));
	}
   
	return 0;
}
