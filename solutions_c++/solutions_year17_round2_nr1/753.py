#include <bits/stdc++.h>
using namespace std;
int T;
int main()
{
	freopen("a.in","r",stdin);
	freopen("a.out","w",stdout);
	cin>>T;

	for(int ca=1;ca<=T;ca++)
	{
		int n;
		double d;
		printf("Case #%d: ",ca);
		cin>>d>>n;
		double t=0;
		for(int i=0;i<n;i++)
		{
			double g,v;
			scanf("%lf%lf",&g,&v);
			t=max(t,(d-g)/v);
		}
		double ans=d/t;
		printf("%.10f\n",ans);
	}
	return 0;
}