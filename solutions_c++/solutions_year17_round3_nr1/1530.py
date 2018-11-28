#include<bits/stdc++.h>
#define rep(i,a,b) for(i=a;i<b;++i)
#define mod 1000000007
#define rev(i,a,b) for(i=a;i>b;--i)
#define ll long long int
#define si(x) scanf("%d",&x)
#define sll(x) scanf("%lld",&x)
#define sstr(x) scanf("%s",x)
#define vi vector<int>
#define vii vector<pair<int, int> >
#define vll vector<ll>
#define mapii map<int, int>
#define mp(x,y) make_pair(x,y)
#define pb(x) push_back(x)
#define ins(x) insert(x)
#define mulmap multimap<int, int>
#define itr ::iterator
ll pow(ll, ll);
ll min(ll, ll);
using namespace std;
struct pan{
	double r,h;
};
int cmp(const pan &a, const pan &b)
{
	if(a.r>b.r)
		return 1;
	else if(a.r<b.r)
		return 0;
	else if(a.h>b.h)
		return 1;
	else
		return 0;
}
int cmp1(const pan &a, const pan &b)
{
	double a1,a2;
	a1 = 2*M_PI*a.r*a.h;
	a2 = 2*M_PI*b.r*b.h;
	if(a1>a2)
		return 1;
	else
		return 0;
}
int main()
{
	int j,l,t,n,k,i,count=0;
	double x,y,ans,tans;
	scanf("%d",&t);
	while(t--)
	{
		count++;
		pan pancake[1005],temp[1005];
		scanf("%d %d",&n,&k);
		rep(i,0,n)
		{
			scanf("%lf %lf", &x, &y);
 			pancake[i].r = x;
			pancake[i].h = y;
		}
		sort(pancake, pancake+n, cmp);
		ans=0;
		rep(i,0,n-k+1)
		{
			tans=0;
			l=0;
			tans=M_PI*pancake[i].r*pancake[i].r + 2*M_PI*pancake[i].r*pancake[i].h;
			rep(j,i+1,n)
			{
				temp[l++]=pancake[j];
			}
			sort(temp, temp+l,cmp1);
			rep(j,0,k-1)
				tans+=2*M_PI*temp[j].r*temp[j].h;
			ans = max(ans,tans);
		}
		printf("Case #%d: %.7lf\n",count, ans);
	}
	return 0;
}
ll min(ll a, ll b)
{
	if(a>b)
		return b;
	else
		return a;
}
ll pow(ll a, ll b)
{
	ll ans=1;
	while(b)
	{
		if(b&1)
		{
			ans=ans*a;
		}
		a=a*a;
		b=b>>1;
	}
	return ans;
}
