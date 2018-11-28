#include <stdio.h>
#include <string.h>
#define mn(a,b) a<b ? a:b
#define mx(a,b) a>b ? a:b
#define INF 1000000000

// using namespace std ;

char x[3000];
int flip[3000];

int main()
{
	int i, j, k, n, t;
	// freopen("../test.in","r",stdin);
	// freopen("../test.out","w",stdout);
	int res;
	scanf("%d",&t);
	for(int loop = 1; loop <= t; loop++)
	{
		printf("Case #%d: ",loop);
		res = 0;
		scanf(" %s %d",x,&k);
		n = strlen(x);
		for(i = 0; i <= n; i++)
			flip[i] = 0;
		for(i = 1; i <= n; i++)
		{
			flip[i] += flip[i-1];
			if(flip[i]%2)
			{
				if(x[i - 1] == '+')
				{
					x[i - 1] = '-';
				}
				else
				{
					x[i - 1] = '+';
				}
			}
			if(x[i - 1] == '-')
			{
				res++;
				flip[i]++;
				if(i+k > n+1)
				{
					printf("IMPOSSIBLE\n");
					break;
				}
				flip[i+k]--;
			}
		}
		if(i == n+1)
		{
			printf("%d\n",res);
		}

	}
	return 0;
}