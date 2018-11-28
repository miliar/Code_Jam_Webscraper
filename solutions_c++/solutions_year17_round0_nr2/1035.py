#include<stdio.h>

long long x, y, tmp, tmp2;

void process()
{
	int n=0;
	long long a[30];
	int i, j;

	while(x)
	{
		a[++n]=x%10;
		x/=10;
	}

	tmp = 0;
	for(i=n;i>=1;i--)
	{
		if(tmp % 10 <= a[i])
		{
			if(tmp % 10 < a[i])
			{
				tmp = tmp * 10 + a[i];
				if(y < tmp)
					y = tmp;
				tmp2 = tmp-1;
				for(j=1;j<i;j++)
					tmp2 = tmp2 * 10 + 9;
				if(y<tmp2)
					y=tmp2;
			}
			else
			{
				tmp = tmp * 10 + a[i];
				if(y < tmp)
					y = tmp;
			}
		}
		else
			break;
	}
}

int main(void)
{
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	int t, T;
	scanf("%d",&T);
	for(t=1;t<=T;t++)
	{
		printf("Case #%d: ",t);
		scanf("%lld",&x);
		y=0;
		process();
		printf("%lld\n",y);
	}
}