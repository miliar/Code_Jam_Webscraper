#include<bits/stdc++.h>
#include<vector>
#include<set>
#include<stack>
#include<queue>
#include<list>
#include<map>
#define ll long long
#define INF 2000000000
#define NINF -2000000000
#define MOD 1000000007
#define br '\n'
#define PI 3.1415926535
using namespace std;
struct pc
{
	ll r,h,rh;
};
bool cmp(pc a, pc b)
{
	return(a.r<b.r);
}
struct classcomp {
  bool operator() (const ll& lhs, const ll& rhs) const
  {return lhs>rhs;}
};
int main()
{
	//ios_base::sync_with_stdio(false);
	//cin.tie(0);
	//freopen("input.txt","r",stdin);
	//freopen("A-small-attempt0.in","r",stdin);
	freopen("A-large.in","r",stdin);
	freopen("output.txt","w",stdout);
	int t;
	cin>>t;
	for(int cno=1;cno<=t;cno++)
	{
		ll n,k;
		cin>>n>>k;
		pc a[n];
		for(ll i=0;i<n;i++)
		{
			cin>>a[i].r>>a[i].h;
			a[i].rh=a[i].r*a[i].h;
		}
		sort(a,a+n,cmp);
		ll sum,max=0;
		int flag;
		for(int i=n-1; i>=k-1 ;i--)
		{
			sum=a[i].r*a[i].r + (2*a[i].rh);
			multiset<ll,classcomp> S;
			flag=0;
			for(int j=0;j<n;j++)
			{
				if(j!=i && a[j].r<=a[i].r)
				{
					S.insert(a[j].rh);
				}
			}
			for(int j=0;j<k-1;j++)
			{
				if(S.empty())
				{
					flag=1;
					break;
				}
				sum+=(2*(*(S.begin())));
				S.erase(S.begin());
			}
			if(flag !=1 && sum>max)
			{
				max=sum;
				//cout<<i<<br;
			}
			S.clear();
		}
		double ans=(double)max*PI;
		cout<<"Case #"<<cno<<": ";
		printf("%.10lf\n",ans);
	}
	return 0;
}

