#include<stdio.h>
#include<string.h>
#include<math.h>
#include<list>
#include<map>
#include<stack>
#include<queue>

int main()
{
	int T;
	__int64 D, N;
	double K[1001], S[1001];
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	scanf("%d",&T);
	for(int i=0;i<T;i++)
	{
		double max=0;
		scanf("%I64d %I64d",&D,&N);
		for(int j=0;j<N;j++)
		{
			scanf("%lf %lf",&K[j],&S[j]);
			if(max<(D-K[j])/S[j])
				max=(D-K[j])/S[j];
		}
		printf("Case #%d: %lf\n",i+1,D/max);
	}
	return 0;
}