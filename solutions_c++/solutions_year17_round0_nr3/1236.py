#include<cstdio>
#include<queue>
using namespace std;
typedef long long ll;

ll solve1(){
	ll n,k;
	priority_queue<ll> q;
	scanf("%lld%lld",&n,&k);
	q.push(n);
	for(ll i=0;i<k-1;i++){
		ll x = q.top();
		ll l,r;
		q.pop();
		if(x%2) l = r = x / 2;
		else{
			l = x / 2;
			r = x / 2 - 1;
		}
		q.push(l);
		q.push(r);
	}
	return q.top();
}

ll solve2(){
	ll n,k;
	scanf("%lld%lld",&n,&k);
	ll s = 1;
	while(s*2-1<k) s *= 2;
	ll a = (n - s + 1) / s;
	ll r = n - s + 1 - a * s;
	if(k-s+1<=r) return a + 1;
	else return a;
}

int main(){
	int t;
	scanf("%d",&t);
	for(int i=1;i<=t;i++){
		ll ans = solve2();
		ll l,r;
		if(ans%2) l = r = ans / 2;
		else{
			l = ans / 2;
			r = ans / 2 - 1;
		}
		printf("Case #%d: %lld %lld\n",i,l,r);
	}
}
