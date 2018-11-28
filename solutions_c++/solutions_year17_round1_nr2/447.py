#include <stdio.h>

int r[110];
int a[2010] ,b[2010] ,c[2010];
int tempa[2010] ,tempb[2010] ,tempc[2010];
void mergesort(int *a ,int *b ,int *c ,int n1 ,int n2);
int su[110] ,tmp[110];
int main(void)
{
	int tt ,ii;
	int n ,p ,i ,j;
	int k ,kk1 ,kk2;
	int np;
	int z;
	int aa ,bb ,cc;
	int ans;
	
	scanf("%d" ,&tt);
	for (ii=1 ; ii<=tt ; ii++)
	{
		scanf("%d %d" ,&n ,&p);
		for (i=1 ; i<=n ; i++)	
		{
			scanf("%d" ,&r[i]);
		}
		np=0;
		for (i=1 ; i<=n ; i++)
		{
			for (j=1 ; j<=p ; j++)
			{
				scanf("%d" ,&k);
				
				kk1=k/r[i];
				while (r[i]*kk1*11>=k*10)
				{
					kk1--;
				}
				kk1++;
				
				kk2=k/r[i];
				while (r[i]*kk2*9<=k*10)
				{
					kk2++;
				}	
				kk2--;
				
				if (kk1<=kk2)
				{
					np++;
					a[np]=kk1;
					b[np]=i;
					c[np]=1;						
					np++;	
					a[np]=kk2;
					b[np]=i;
					c[np]=2;
				}
			}
		}
		mergesort(a,b,c,1,np);
/*/	for (i=1 ; i<=np ; i++)
		{
		printf("%d %d %d\n" ,a[i] ,b[i] ,c[i]);
		}//*/
		
		for (i=1 ; i<=n ; i++)
		{
			su[i]=0;
			tmp[i]=0;
		}
		ans=0;
		for (i=1 ; i<=np ; i++)
		{
			aa=a[i];
			bb=b[i];
			cc=c[i];
			if (cc==1)
			{
				su[bb]++;
			}
			else
			{
				if (tmp[bb])
				{
					tmp[bb]--;
				}
				else
				{
					su[bb]--;
				}
			}
			z=1;
			for (j=1 ; j<=n ; j++)
			{
				if (!su[j])
				{
					z=0;
					break;
				}
			}
			if (z)
			{
				ans++;
				for (j=1 ; j<=n ; j++)
				{
					su[j]--;
					tmp[j]++;
				}			
			}
		}
		printf("Case #%d: %d\n" ,ii ,ans);
		
	}
	
	return 0;	
}

void mergesort(int *a ,int *b ,int *c ,int n1 ,int n2)
{
	int a1 ,a2 ,n12;
	int i ,j;
	
	if (n1<n2)
	{	
		n12=(n1+n2)/2;
		mergesort(a,b,c,n1,n12);
		mergesort(a,b,c,n12+1,n2);
		for (i=n1 ; i<=n2 ; i++)
		{
			tempa[i]=a[i];	
			tempb[i]=b[i];
			tempc[i]=c[i];
		}
		a1=n1;
		a2=n12+1;
		for (i=n1 ; (a1<=n12 && a2<=n2) ;i++)
		{
			if (tempa[a1]<tempa[a2]||(tempa[a1]==tempa[a2]&&tempc[a1]<=tempc[a2]))
			{
				a[i]=tempa[a1];
				b[i]=tempb[a1];
				c[i]=tempc[a1];				
				a1++;
			}
			else
			{
				a[i]=tempa[a2];
				b[i]=tempb[a2];
				c[i]=tempc[a2];					
				a2++;				
			}
		}
		if (a1>n12)
		{
			for (j=a2 ; j<=n2 ; j++ , i++)
			{
				a[i]=tempa[j];
				b[i]=tempb[j];
				c[i]=tempc[j];					
			}
		}
		else
		{
			for (j=a1 ; j<=n12 ; j++ , i++)
			{
				a[i]=tempa[j];
				b[i]=tempb[j];
				c[i]=tempc[j];						
			}			
		}
	}
}
