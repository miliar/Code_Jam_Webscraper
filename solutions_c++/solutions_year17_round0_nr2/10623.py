#include<stdio.h>
#include<stdlib.h>
int check(long long int);
int main(void)
{
	 long long int t,n[100],i,j;
	scanf("%lld",&t);
	for(i=0;i<t;i++)
	scanf("%lld",&n[i]);
	for(i=0;i<t;i++)
	{
		for(j=n[i];j>=1;j--)
		{
			if(check(j)==1)
			{
				printf("case #%lld: %lld\n",(i+1),j);
				break;
			}
		}
	}
	return 0;
}
int check(long long int n)
{
	int r1,r2;
	r1=n%10;
	n=n/10;
	while(n!=0)
	{
		r2=n%10;
		if(r1<r2)
		return 0;
		r1=r2;
		n=n/10;
	}
	return 1;
}
