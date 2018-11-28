#include <stdio.h>
long long p10[19],dig[20];
void doe()
{
	long long n,i,i2,check=0,pos;
	scanf("%lld",&n);
	for(i=0;i<=18;i++)
		dig[i]=(n/p10[i])%10;
	for(i=18;i>=0;i--)
	{
		if(dig[i]<dig[i+1])
		{
			check=1;
			pos=i+1;
			break;
		}
	}
	if(check==0)
	{
		printf("%lld\n",n);
		return;
	}
	for(i=pos;dig[i]-1<dig[i+1];i++);
	dig[i]--;
	i--;
	for(;i>=0;i--)
		dig[i]=9;
	for(i=18;dig[i]==0;i--);
	for(;i>=0;i--)
		printf("%lld",dig[i]);
	printf("\n");
}
int main()
{
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int n,i;
	p10[0]=1;
	for(i=1;i<19;i++)
		p10[i]=p10[i-1]*10;
	scanf("%d",&n);
	for(i=1;i<=n;i++)
	{
		printf("Case #%d: ",i);
		doe();
	}
	return 0;
}