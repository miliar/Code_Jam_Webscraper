#include <bits/stdc++.h>
#define si(n) scanf("%d",&n);
#define pi(n) printf("%d\n",n);
#define pl(n) printf("%lld\n",n);
#define sl(n) scanf("%lld",&n);
#define sd(n) scanf("%lf",&n);
#define pd(n) printf("%lf\n",n);
#define ss(s) scanf("%s",s);
#define ps(s) printf("%s\n",s);
#define pb push_back
#define ll long long int
#define maxn 1000005
#define sqrtn 317
#define maxm 1000005
#define minv(a,b,c) min(a,min(b,c))
#define pii pair<int,int>
#define pll pair<ll,ll>
#define eps 1e-9
#define mod 1000000007
#define psi pair < string,ll>
#define mp make_pair
#define BLOCK 450
using namespace std;

ll arr[65];
ll parr[65];

pair<ll,ll> find(ll num,ll k,int c)
{
	if(k==1)
	{
		//printf("%lld %lld\n",p.first,p.second);
		return mp(num/2,(num-1)/2);
	}

	ll val=k-arr[c-1];
	val--;
	//printf("%lld %lld\n",val,val%parr[c-1]+parr[c-1]);
	pll p=find(num,val%parr[c-1]+parr[c-1],c-1);
	if(val/parr[c-1]==0)
	{
		return mp(p.first/2,(p.first-1)/2);
	}
	return mp(p.second/2,(p.second-1)/2);


	/*pll p=find(num,k/2);
	if(k%2==0)
	{
		printf("%lld %lld\n",p.first,p.second);
		return mp(p.first/2,(p.first-1)/2);
	}
	printf("%lld %lld\n",p.first,p.second);
	return mp(p.second/2,(p.second-1)/2);*/
}

int main()
{
	int t;
	si(t);
	arr[0]=1;
	parr[0]=1;
	ll num=1;
	int c=1;
	while(num <= 1e18)
	{
		num=num*2;
		arr[c]=arr[c-1]+num;
		parr[c]=num;
		c++;
	}
	for(int i=1;i<=t;i++)
	{
		printf("Case #%d: ",i);
		ll num,k;
		sl(num);sl(k);
		c=0;
		while(arr[c]<k)
		{
			c++;
		}
		//pi(c);
		pll p=find(num,k,c);
		printf("%lld %lld\n",p.first,p.second);
	}
}