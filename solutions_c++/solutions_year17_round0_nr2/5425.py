#include<stdio.h>
#include<math.h>
int main()
{
	long long int n,i,j,t,count,zero,p,p1;
	scanf("%lld",&t);
	for(i=0;i<t;i++)
	{
		scanf("%lld",&n);
		count=0;
		zero=0;
		for(j=n;j>0;j=j/10)
		{
		    //printf("%lld    %lld   %lld\n",j,j%10,j%100);
			count++;
			if(j%10>=(j%100)/10)
			continue;
			else
			{
				p=pow(10,count);
				n=n-p;
				n=(n/p)*p + (p-1);
				p1=pow(10,count-1);
				j=n/p1;
			}
		}
		printf("Case #%lld: %lld\n",i+1,n);
	}
	return 0;
}
