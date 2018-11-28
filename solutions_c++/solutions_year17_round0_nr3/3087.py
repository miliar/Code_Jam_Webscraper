#include <iostream>
#include <cstdio>
#include <stack>
using namespace std;
long long n, k, t, a1, a2, n1, n2, n3, a3, wyn, wyn1, wyn2;
int main()
{	
	scanf("%d", &t);
	for(int i=1;i<=t;i++)
	{
		scanf("%lld", &n);
		scanf("%lld", &k);
		k--;
		a1=1;
		a2=0;
		n1=n;
		n2=0;
		n3=0;
		a3=0;
		for(;;)
		{
			if(n1<n2)
			{
				swap(n1,n2);
				swap(a1,a2);
			}
			if(n1<n3)
			{
				swap(n1,n3);
				swap(a1,a3);
			}
			if(n1==n3)
			{
				a1+=a3;
				a3=0;
			}
			if(n1==n2)
			{
				a1+=a2;
				a2=0;
			}
			if(n3==n2)
			{
				a2+=a3;
				a3=0;
			}
			if(k<a1)
			{
				wyn=n1;
				 break;
			}
			k-=a1;
			if(n1%2==1)
			{
				n1/=2;
				a1*=2;	
			}
			else
			{
				if(n2!=0)
				{
					n3=n1/2;
					a3=a1;
				}
				else
				{
					n2=n1/2;
					a2=a1;
				}
				n1--;
				n1/=2;
			}
		}
		wyn1=wyn/2;
		wyn2=wyn/2-1+wyn%2;
		printf("Case #%d: ", i);
		printf("%lld %lld\n", wyn1, wyn2); 
	}
	return 0;
}
