#include <stdio.h>

int main(void)
{
	int tt ,ii;
	long long n ,k;
	long long a1 ,a11 ,a2 ,a22 ,a3 ,a33 ,a4 ,a44;
	long long ans ,ans1 ,ans2;
	
	scanf("%d" ,&tt);
	for (ii=1 ; ii<=tt ; ii++)
	{
		scanf("%I64d %I64d" ,&n ,&k);
		k--;
		a1=n/2;
		a11=1;
		a2=(n-1)/2;
		a22=1;
		ans=n;
		while (k)
		{
			if (k<=a11)
			{
				ans=a1;
				break;
			}
			else
			{
				k-=a11;
				if (k<=a22)
				{
					ans=a2;
					break;
				}
				else
				{
					k-=a22;
					a3=a1/2;
					a33=0;
					a4=(a2-1)/2;
					a44=0;
					if (a1==a3+a3+1)
					{
						a33+=a11+a11;
					}
					else if (a1==a3+a4+1)
					{
						a33+=a11;
						a44+=a11;
					}
					else
					{
						a44+=a11+a11;
					}
					if (a2==a3+a3+1)
					{
						a33+=a22+a22;
					}
					else if (a2==a3+a4+1)
					{
						a33+=a22;
						a44+=a22;
					}
					else
					{
						a44+=a22+a22;
					}					
					a1=a3;
					a11=a33;
					a2=a4;
					a22=a44;
				}
			}
		}
		ans1=ans/2;
		ans2=(ans-1)/2;
		printf("Case #%d: %I64d %I64d\n" ,ii ,ans1 ,ans2);
	}
	
	return 0;	
}
