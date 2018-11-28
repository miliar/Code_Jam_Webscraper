#include<bits/stdc++.h>
using namespace std;
typedef long long ll;
map<ll, ll> cnt;
void execute()
{
	ll n,k;
	priority_queue<ll, vector<ll>, less<ll> > pq;
	
	cnt.clear();
	
	scanf("%lld %lld",&n,&k);
	cnt[n] = 1;
	pq.push(n);
	while(k)
	{
		ll u = pq.top(); pq.pop();
		ll nu = cnt[u]; cnt.erase(u);
		ll l = ll((u-1)/2), r = u-l-1;
		if(nu>=k)
		{
			printf("%lld %lld\n", r, l);
			return;
		}
		if(cnt.find(l) == cnt.end()) pq.push(l);
		if(cnt.find(r) == cnt.end()) pq.push(r);
		cnt[l] += nu;
		cnt[r] += nu;
		k -= nu;
	}
}
int main()
{
	freopen("C.inp","r",stdin);
	freopen("C.out","w",stdout);
	int test;
	scanf("%d",&test);
	for(int tc=1; tc<=test; tc++)
	{
		printf("Case #%d: ",tc);
		execute();
	}
	return 0;
}
