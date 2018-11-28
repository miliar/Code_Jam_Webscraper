#include <stdio.h>

char s[30][30];
int a[30][30];
int main(void)
{
	int tt ,ii;
	int r ,c;
	int i ,j ,j1 ,j2;
	char cc;
	int k1 ,k2, k3 ,k4;
	int z;

	scanf("%d" ,&tt);
	for (ii=1 ; ii<=tt ; ii++)
	{
		scanf("%d %d" ,&r ,&c);
		for (i=1 ; i<=r ; i++)
		{
			for (j=1 ; j<=c ; j++)
			{
				a[i][j]=0;
			}
		}
		for (i=1 ; i<=r ; i++)
		{
			scanf("%s" ,s[i]+1);
		}
		for (i=1 ; i<=r ; i++)
		{
			for (j=1 ; j<=c ; j++)
			{
				if (s[i][j]!='?')
				{
					a[i][j]=1;
				}
			}
		}
		for (i=1 ; i<=r ; i++)
		{
			for (j=1 ; j<=c ; j++)
			{
				if (a[i][j])
				{
					cc=s[i][j];
					k1=i;
					k2=i;
					k3=j;
					k4=j;
					for (k1=i-1 ; k1 ; k1--)
					{
						if (s[k1][j]!='?')
						{
							break;
						}
					}
					k1++;
					for (k3=j-1 ; k3 ; k3--)
					{
						z=0;
						for (j1=k1 ; j1<=k2 ; j1++)
						{
							if (s[j1][k3]!='?')
							{
								z=1;
								break;
							}
						}
						if (z)
						{
							break;
						}
					}
					k3++;
					for (k4=j+1 ; k4<=c ; k4++)
					{
						z=0;
						for (j1=k1 ; j1<=k2 ; j1++)
						{
							if (s[j1][k4]!='?')
							{
								z=1;
								break;
							}
						}
						if (z)
						{
							break;
						}
					}
					k4--;		
					for (k2=i+1 ; k2<=r ; k2++)
					{
						z=0;
						for (j1=k3 ; j1<=k4 ; j1++)
						{
							if (s[k2][j1]!='?')
							{
								z=1;
								break;
							}
						}
						if (z)
						{
							break;
						}
					}
					k2--;					
					for (j1=k1 ; j1<=k2 ; j1++)
					{
						for (j2=k3 ; j2<=k4 ; j2++)
						{
							s[j1][j2]=cc;
						}					
					}
				}
			}
		}		
		printf("Case #%d:\n" ,ii);
		for (i=1 ; i<=r ; i++)
		{
			printf("%s\n" ,s[i]+1);
		}
	}
	
	return 0;	
}
