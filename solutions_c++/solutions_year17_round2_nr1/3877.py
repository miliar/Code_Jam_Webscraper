#include<bits/stdc++.h>
using namespace std;
#define sint(a) int a; scanf("%d",&a);
#define sint2(a,b) int a,b; scanf("%d %d",&a,&b);
#define sint3(a,b,c) int a,b,c; scanf("%d %d %d",&a,&b,&c);
#define slong(a) long long a; scanf("%lld",&a);
#define slong2(a,b) long long a,b; scanf("%lld %lld",&a,&b);
#define slong3(a,b,c) long long a,b,c; scanf("%lld %lld %lld",&a,&b,&c);
#define sstring(a) scanf("%s",a);
#define all(x) (x).begin(),(x).end()
#define F first
#define S second
#define pb push_back
#define sz(x) (int)(x).size()
#define mset(a,b) memset(a,b,sizeof(a))
#define FOR(i,a,b) for(int i=a;i<b;i++)
#define ROF(i,b,a) for(int i=b;i>a;i--)
typedef pair<int,int> ii;
typedef vector<int> vi;
typedef vector<ii> vii;
typedef pair<long long,long long> ll;
typedef vector<long long> vl;
typedef vector<ll> vll;

int main()
{
	sint(t);
	FOR(l,1,t+1)
	{
		vii v;
		printf("Case #%d: ",l);
		double ans;
		sint2(n,m);
		while(m--)
		{
			sint2(a,b);
			v.pb(make_pair(a,b));
		}
		sort(all(v));
		int f=v[sz(v)-1].S,d=v[sz(v)-1].F;
		double ss=(double)((double)(n)-d)/f;
//		printf("%d %d %d\n",n,d,f);
		for(int i=sz(v)-1;i>0;i--)
		{
//			printf("%d %d\n",v[i-1].S,f);
			if((double)((double)(n)-v[i-1].F)/v[i-1].S>=ss)
			{
				ss=(double)((double)(n)-v[i-1].F)/v[i-1].S;
				f=v[i-1].S;
				d=v[i-1].F;
			}
		}
//		printf("%d %d %d\n",n,d,f);
		ans=(double)n/(((double)n-(double)d)/(double)f);
		printf("%lf\n",ans);
	}
}
