#include <iostream>
#include <cstdio>
using namespace std;
int g, x;
long long n, t[20], a;
int main()
{
	t[0]=1;
	for(int i=1;i<=18;i++) t[i]=10*t[i-1];
	for(int i=1;i<=18;i++)
	{
		 t[i]=(t[i]-1)/9;
	}
	t[19]=t[18]*10+1;
	scanf("%d", &g);
	for(int i=1;i<=g;i++)
	{
		scanf("%lld", &n);
		a=n;
		x=0;
		while(a!=0)
		{
			x++;
			a/=10;
		}
		a=0;
		for(int j=x;j>=0;j--)
		{
			while(a+t[j]<=n && a%10<9)
			{
				 a+=t[j];
			}
		}
		printf("Case #%d: %lld\n", i, a);
	}
	return 0;
}
