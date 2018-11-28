#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<iostream>
#include<algorithm>
#define N 111
#define eps 1e-10
using namespace std;
double ans,p[N],u,l,r,mid;
int n,test,k;
bool can(double a)
{
	double ret=0;
	for (int i=1;i<=n;i++) if (a>p[i]) ret+=a-p[i];
	return u-ret>eps;
}
int main()
{
	freopen("C-small-1-attempt0.in","r",stdin);
	freopen("3.out","w",stdout);
	cin>>test;
	for (int kk=1;kk<=test;kk++)
	{
		ans=1.0;
		printf("Case #%d: ",kk);
		cin>>n>>k;
		cin>>u;
		for (int i=1;i<=n;i++)
		scanf("%lf",&p[i]);
		sort(p+1,p+n+1);
		l=0.0;
		r=1.0;
		mid=0.5;
		while (r-l>eps)
		{
			if (can(mid)) l=mid;
			else r=mid;
			mid=(l+r)/2;
		}
		for (int i=1;i<=n;i++)
		ans*=max(p[i],mid);
		printf("%.8lf\n",ans);
	}
	return 0;
}
