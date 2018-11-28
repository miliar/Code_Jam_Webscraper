#include<bits/stdc++.h>
using namespace std;
int main()
{
	int t;
	scanf("%d",&t);
	int p=1;
	while(t--)
	{
		int n;
		double d,r,ma=0,x,y;
		scanf("%lf%d",&d,&n);
		for(int i=0;i<n;i++)
		{
			scanf("%lf%lf",&x,&y);
			r=(d-x)/y;
			if(ma<r)
				ma=r;
		}
		double ans;
		ans=d/ma;
		printf("Case #%d: ",p);
		printf("%lf\n",ans);
		p++;
	}
}