#include<cstdio>
#include<algorithm>
using namespace std;
int main()
{
	int T,n;
	double ans,d,s,c;
	scanf("%d",&T);
	for(int I=1;I<=T;I++)
	{
		ans=0;
		scanf("%lf%d",&d,&n);
		for(int i=0;i<n;i++)
		{
			scanf("%lf%lf",&s,&c);
			ans=max(ans,(d-s)/c);
		}
		printf("Case #%d: %lf\n",I,d/ans);
	}
}