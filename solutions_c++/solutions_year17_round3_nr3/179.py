#include <stdio.h>
void solve();
int main()
{
	freopen("smallC3.in","r",stdin);
	freopen("output.txt","w",stdout);
	int T;
	scanf("%d",&T);
	for(int i=1;i<=T;i++)
	{
		printf("Case #%d: ",i);
		solve();
	}
}
double x[60];
void solve()
{
	int a,b;
	double c;
	scanf("%d%d",&a,&b);
	scanf("%lf",&c);
	for(int i=1;i<=a;i++) scanf("%lf",&x[i]);
	
	double min = 0, max = 1;
	double ans = 0;
	while(max-min>=0.00000001)
	{
		double h = (min + max)/2;
		double s = 0;
		for(int i=1;i<=a;i++) if(x[i]<h) s+= h-x[i];
		if(s<=c)
		{
			ans = h;
			min = h;
		}
		else max = h;
	}
	for(int i=1;i<=a;i++) if(x[i]<ans) x[i] = ans;
	double k = 1;
	for(int i=1;i<=a;i++) k*=x[i];
	printf("%.12lf\n",k);
}
