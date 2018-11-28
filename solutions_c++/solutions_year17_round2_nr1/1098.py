#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<iostream>
#include<algorithm>
using namespace std;
int test,m,n,a,b;
double ans;
int main()
{
	freopen("A-large (1).in","r",stdin);
	freopen("1.out","w",stdout);
	cin>>test;
	for (int kk=1;kk<=test;kk++)
	{
		ans=0;
		printf("Case #%d: ",kk);
		cin>>m>>n;
		for (int i=1;i<=n;i++)
		{
			scanf("%d%d",&a,&b);
			ans=max(ans,1.0*(m-a)/b);
		}
		printf("%.8lf\n",1.0*m/ans);
	}
	return 0;
}
