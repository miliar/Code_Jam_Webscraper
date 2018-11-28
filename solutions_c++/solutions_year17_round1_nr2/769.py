#include<bits/stdc++.h>
using namespace std;
 
// Numeric Constants
#define MOD 1000000007
#define maxs 250005
#define mins 1005
#define eps 0.000000000001
#define imax 2000000200
#define llmax 1000000002000000000ll
 
// Others
#define ll long long int
#define pb push_back
#define gc getchar_unlocked
#define iosbase ios_base::sync_with_stdio(false)
#define pii pair<int,int>
#define pll pair<ll,ll>
#define ppi pair<pair<int,int>,int>
#define ppl pair<pll,ll>
#define vi vector<int>
#define sc scanf
#define pr printf
#define lld I64d
#define F first
#define S second
#define siter set<int>::iterator
#define p_pq priority_queue
#define ub upper_bound
#define lb lower_bound

ll r[51];
vector<pair<ll,ll> > v[51];
ll in[51];

pair<ll,ll> fun(ll x,ll y)
{
	ll l,r;
	long double dd=(x*10.0/11.0);
	ll val=ceil(dd);
	if(val%y==0)
		l=val/y;
	else
		l=val/y+1;
	dd=(x*10.0/9.0);
	val=floor(dd);
	if(val%y==0)
		r=val/y;
	else
		r=val/y;
	pair<ll,ll> temp;
	temp.first=l;
	temp.second=r;
	return temp;
}

bool comp(pair<ll,ll> p1,pair<ll,ll> p2)
{
	if(p1.first==p2.first)
		return p1.second<p2.second;
	return p1.first<p2.first;
}

int main()
{
	ll t,n,p,sum,fl,tt;
    scanf("%lld",&t);
    for(ll o=1;o<=t;++o)
    {
       	scanf("%lld%lld",&n,&p);
       	for(ll i=0;i<n;++i)
       	{
       		v[i].clear();
       		scanf("%lld",&r[i]);
       	}
       	for(ll i=0;i<n;++i)
       	{
       		for(ll j=0;j<p;++j)
       		{
       			scanf("%lld",&tt);
    			pair<ll,ll> temp=fun(tt,r[i]);
    			if(temp.first<=temp.second)
    				v[i].pb(temp);
       		}
       		sort(v[i].begin(),v[i].end(),comp);
       		// for(ll j=0;j<v[i].size();++j)
       		// 	cout<<v[i][j].first<<" "<<v[i][j].second<<endl;;
       		// cout<<endl;
       	}
       	memset(in,0,sizeof in);
       	sum=0;
       	while(1)
       	{
       		fl=1;
       		for(ll i=0;i<n;++i)
       		{
       			if(in[i]==v[i].size())
       			{
       				fl=0;
       				break;
       			}
       		}
       		if(fl==0)
       			break;
       		ll l=v[0][in[0]].first;
       		ll r=v[0][in[0]].second;
       		for(ll i=1;i<n;++i)
       		{
       			l=max(l,v[i][in[i]].first);
       			r=min(r,v[i][in[i]].second);
       		}
       		if(l<=r)
       		{
       			sum++;
       			for(ll i=0;i<n;++i)
       				in[i]++;
       		}
       		else
       		{
       			tt=0;
       			for(ll i=1;i<n;++i)
       			{
       				if(v[tt][in[tt]].first>v[i][in[i]].first)
       					tt=i;
       				else if((v[tt][in[tt]].first==v[i][in[i]].first)&&(v[tt][in[tt]].second>v[i][in[i]].second))
       					tt=i;
       			}
       			in[tt]++;
       		}
       	}
        printf("Case #%lld: %lld\n",o,sum);
    }
	return 0;
}