#include <iostream>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <algorithm>
#define maxn 1000


using namespace std;

char ch[5000];
int a[5000];

int main()
{
	int T;
	scanf("%d",&T);
	for(int cas = 1; cas <= T; cas++)
	{
		int k;
		printf("Case #%d: ", cas);
		scanf("%s%d", ch + 1, &k);
		int len = strlen(ch + 1);
		for(int i = 1; i <= len; i++)
		{
			if(ch[i] == '+')a[i] = 1;
			else a[i] = 0;
		}
		int ans = 0;
		for(int i = 1; i <= len; i++)
		{
			if(a[i] == 0)
			{
				if(i + k - 1 <= len)
				{
					ans ++;
					for(int j = i; j <= i + k - 1; j++)
					{
						a[j] ^= 1;
					}
				}
				else
				{
					break;
				}
			}
		}
		int flag = 0;
		for(int i = 1; i <= len; i++)
		{
			if(a[i] == 0)
			{
				flag = 1;
				break;
			}
		}
		if(flag == 1)
		{
			puts("IMPOSSIBLE");
		}
		else
		{
			printf("%d\n", ans);
		}
	}

	return 0;
}


