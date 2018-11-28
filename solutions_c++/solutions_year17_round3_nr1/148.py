#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<iostream>
#include<algorithm>
#define PI 3.1415926535897932
#define N 1111
using namespace std;
long long test,n,k,now,ans;
struct node
{
	long long r,h;
}p[N];
bool cmp(node a,node b)
{
	return a.r>b.r;
}
bool cmp2(node a,node b)
{
	return a.r*a.h>b.r*b.h;
}
int main()
{
	freopen("A-large (2).in","r",stdin);
	freopen("11.out","w",stdout);
	cin>>test;
	for (int kk=1;kk<=test;kk++)
	{
		printf("Case #%d: ",kk);
		cin>>n>>k;
		ans=0;
		for (int i=1;i<=n;i++)
		scanf("%lld%lld",&p[i].r,&p[i].h);
		for (int i=1;i<=n-k+1;i++)
		{
			sort(p+1,p+n+1,cmp);
			now=p[i].r*p[i].r+2*p[i].r*p[i].h;
			sort(p+i+1,p+n+1,cmp2);
			for (int j=i+1;j<i+k;j++)
			now+=2*p[j].r*p[j].h;
			ans=max(ans,now);
		//	cout<<ans<<endl;
		}
		printf("%.12lf\n",1.0*PI*ans);
	}
	return 0;
}
