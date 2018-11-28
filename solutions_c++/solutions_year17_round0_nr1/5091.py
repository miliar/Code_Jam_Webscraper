#include <stdio.h>
#include <string.h>
#include <queue>
#include <algorithm>
#include <vector>
using namespace std;

int main()
{
	int T;
	scanf("%d",&T);
//	freopen("1.out","w",stdout);
	for(int t= 0; t< T;t++)
	{
		char s[2000];
		int f;
		scanf(" %s %d", s, &f);
		int ans = 0;
		bool fl = true;
		printf("Case #%d: ",t+1);
		for(int i = 0; i < strlen(s); i++)
		{
			if(s[i] == '-')
			{
				ans++;
				if(i+f-1 >= strlen(s))
				{
					fl = false;
					printf("IMPOSSIBLE\n");
					break;
				}
				for(int j = 0; j < f; j++)
				{
					if(s[i+j] =='-')
						s[i+j] = '+';
					else s[i+j] ='-';
				}
			}
		}
		if(fl)
			printf("%d\n",ans);
	}
	return 0;
}
