#include<stdio.h>
#include<string.h>
#include<math.h>
#include<list>
#include<map>
#include<stack>
#include<queue>
#include<algorithm>

int main()
{
	int T,N,K;
	double U;
	double Si[100];
	double St;
	double rate;
	freopen("C-small-1-attempt4.in","r",stdin);
	freopen("C-small-1-attempt4.out","w",stdout);
	scanf("%d",&T);
	for(int i=0;i<T;i++)
	{
		scanf("%d %d",&N,&K);
		scanf("%lf",&U);
		St=0;
		for(int j=0;j<N;j++)
		{
			scanf("%lf",&Si[j]);
			St+=Si[j];
		}
		std::vector<double> v(Si,Si+N);
		std::sort(v.begin(),v.end());
		if(N==K)
		{
			double limit=(St+U)/N;
			int j=N-1;
			rate=1;
			while(v.at(j)>limit&&j>0)
			{
				rate*=v.at(j);
				St-=v.at(j);
				j--;
			}
			rate*=pow((St+U)/(j+1),(j+1));
		}
		printf("Case #%d: %lf\n",i+1,rate);
	}
	return 0;
}