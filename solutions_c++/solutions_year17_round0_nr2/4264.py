#include<cstdio>
#include<cstdlib>
#include<cstring>

using namespace std;

long long n;

int y[30],z[30],T;

bool check(int l)
{
	for (int a=l;a>=2;a--)
		if (y[a]>y[a-1]) return false;
	return true;
}

int main()
{
	scanf("%d",&T);
	for (int t=1;t<=T;t++)
	{
		scanf("%lld",&n);
		int l=1;
		while (n)
		{
			z[l]=n%10;
			n/=10;
			l++;
		}
		l--;
		z[0]=9;
		for (int a=0;a<=l;a++)
		{
			for (int b=1;b<=a;b++)
				y[b]=9;
			if (z[a]==9) y[a+1]=z[a+1];
			else y[a+1]=z[a+1]-1;
			for (int b=a+2;b<=l;b++)
				y[b]=z[b];
			if (check(l)) break;
		}
		long long ans=0;
		for (int a=l;a>=1;a--)
			ans=ans*10+y[a];
		printf("Case #%d: %lld\n",t,ans);
	}

	return 0;
}
