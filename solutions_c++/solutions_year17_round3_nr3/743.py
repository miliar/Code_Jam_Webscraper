#include<bits/stdc++.h>
using namespace std;
int main()
{
	freopen("C-small-1-attempt1.in","r",stdin);
	freopen("C_small-1_1.txt","w",stdout);
	int a,b,T,N,K;
	double U,sum,m[100],ans,num,num2;
	scanf("%d",&T);
	for(a=0;a<T;a++)
	{
		scanf("%d %d",&N,&K);
		scanf("%lf",&U);
		sum=U;
		for(b=0;b<N;b++)
		{
			scanf("%lf",&m[b]);
			sum+=m[b];
		}
		sort(m,m+N);
		if(N==K)
		{
			ans=1.0;
			num2=N;
			for(b=N-1;b>=0;b--)
			{
				num=sum/double(num2);
				if(m[b]>num)
				{
					ans*=m[b];
					num2--;
					sum-=m[b];
				}
				else ans*=num;
			}
			printf("Case #%d: %lf\n",a+1,ans);
		}
	}
}
