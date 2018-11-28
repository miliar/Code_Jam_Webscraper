#include<bits/stdc++.h>
using namespace std;
void execute()
{
	int D,n;
	double mx = 0;
	scanf("%d %d",&D, &n);
	for(int i=1; i<=n; i++)
	{
		double k,s;
		scanf("%lf %lf",&k, &s);
		mx = max(mx, (D-k)/s);
	}
	printf("%lf\n", D/mx);
}
int main()
{
	freopen("A-large.in","r",stdin);
	freopen("A.out","w",stdout);
	int test;
	scanf("%d",&test);
	for(int tc=1; tc<=test; tc++)
	{
		printf("Case #%d: ",tc);
		execute();
	}
	return 0;
}
