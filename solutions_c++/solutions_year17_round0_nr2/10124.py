#include <cstdio>
#include <cstdlib>

bool istidy(int n)
{
	char a[20];
	itoa(n,a,10);
	for(int i=1;a[i]!=0;i++)
	{
		if(a[i] < a[i-1]) return false;
	}
	return true;
}

int main()
{
	int t;
	scanf("%d",&t);
	for(int i=1;i<=t;i++)
	{
		int n;
		scanf("%d",&n);
		for(int j=n;j>0;j--)
		{
			if(istidy(j))
			{
				printf("Case #%d: %d\n",i,j);
				break;
			}
		}
	}
	return 0;
}
