#include <stdio.h>

int p[1010] ,b[1010];
int a[1010];
int pos[1010];
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
	int n ,c ,m ,i;
	int ans1 ,ans2 ,sum;
	
	scanf("%d" ,&tt);
	for (ii=1 ; ii<=tt ; ii++)
	{
		scanf("%d %d %d" ,&n ,&c ,&m);
		for (i=1 ; i<=c ; i++)
		{
			a[i]=0;
		}
		for (i=1 ; i<=n ; i++)
		{
			pos[i]=0;
		}
		for (i=1 ; i<=m ; i++)
		{
			scanf("%d %d" ,&p[i] ,&b[i]);
			a[b[i]]++;
			pos[p[i]]++;
		}
		ans1=0;
		for (i=1 ; i<=c ; i++)
		{
			ans1=max(ans1,a[i]);
		}
		sum=0;
		for (i=1 ; i<=n ; i++)
		{	
			sum+=pos[i];
			ans1=max(ans1,(sum-1)/i+1);
		}
		ans2=0;
		for (i=1 ; i<=n ; i++)
		{	
			if (pos[i]>ans1)
			{
				ans2+=pos[i]-ans1;	
			}
		}		
		printf("Case #%d: %d %d\n" ,ii ,ans1 ,ans2);		
	}
	
	return 0;
}
