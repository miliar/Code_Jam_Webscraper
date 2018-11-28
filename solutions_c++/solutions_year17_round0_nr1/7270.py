#include <stdio.h>
#include <string.h>
#include <stdlib.h>
int main()
{
	freopen("2017QA.out", "w", stdout);
	freopen("2017QA.in", "r", stdin);
	int T,t;
	for (scanf("%d", &T),t=0;t<T;t++)
	{
		char cake[1001];
		int cs,size,ans=0;
		scanf("%s%d", cake, &size);
		cs = strlen(cake);
		for (int i = 0; i <= cs-size; i++)
		{
			if (cake[i] == '-')
			{
				ans++;
				for (int j = 0; j < size; j++)
					if (cake[i + j] == '-') cake[i + j] = '+';
					else cake[i + j] = '-';
			}
		}
		for(int i=cs-size;i<cs;i++)
			if (cake[i] == '-')
			{
				ans = -1;	break;
			}
		if(ans<0)
			printf("Case #%d: IMPOSSIBLE\n", t + 1, ans);
		else printf("Case #%d: %d\n", t + 1, ans); 
	}
}