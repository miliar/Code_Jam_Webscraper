#include <stdio.h>

int a[10];
int min(int aa ,int bb)
{
	if (aa<bb)	
	{
		return aa;
	}
	return bb;
}
int max(int aa ,int bb)
{
	if (aa>bb)	
	{
		return aa;
	}
	return bb;
}
int main(void)
{
	int tt ,ii;
	int ans;
	int n ,p;
	int i;
	int g;
	int mi ,ma;
	int k;
	
	scanf("%d" ,&tt);
	for (ii=1 ; ii<=tt ; ii++)
	{
		scanf("%d %d" ,&n ,&p);
		for (i=0 ; i<p ; i++)
		{
			a[i]=0;
		}
		for (i=1 ; i<=n ; i++)
		{
			scanf("%d" ,&g);
			a[g%p]++;
		}
		ans=n;
		if (p==2)
		{
			ans-=(a[1]/2);
		}
		else if (p==3)
		{
			mi=min(a[1],a[2]);
			ma=max(a[1],a[2]);			
			ans-=mi;
			ma=ma-mi;
			ans-=(ma/3*2);
			if (ma%3==2)
			{	
				ans--;	
			}
		}
		else if (p==4)
		{
			if (a[2]&1)
			{
				k=1;
			}
			else
			{
				k=0;	
			}
			ans-=a[2]/2;
			mi=min(a[1],a[3]);
			ma=max(a[1],a[3]);			
			ans-=mi;
			ma=ma-mi;
			if (k)
			{
				if (ma==0)
				{
					ans=ans;
				}
				else if (ma==1)
				{
					ans--;
				}
				else if (ma>=2)
				{
					ans-=2;
					ma-=2;
					ans-=(ma/4*3);
					if (ma%4==2)
					{
						ans--;
					}
					else if (ma%4==3)
					{
						ans-=2;
					}					
				}
			}
			else
			{
				ans-=(ma/4*3);
				if (ma%4==2)
				{
					ans--;
				}
				else if (ma%4==3)
				{
					ans-=2;
				}
			}		
		}
		printf("Case #%d: %d\n" ,ii ,ans);		
	}
	
	return 0;
}
