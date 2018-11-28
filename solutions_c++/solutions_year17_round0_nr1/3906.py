#include <cstdio>
#include <cstring>


int main()
{
	int T;
	scanf("%d", &T);
	int cnt = 1;
	while(T--)
	{
		char s[2048];
		int k;
		scanf("%s%d", s, &k);
		int l = strlen(s);
		int start = 0;
		int cur = 0;
		int finish = 0;
		int step = 0;
		while(!finish)
		{
			for(int i = start; i < l; i++)
			{
				if(s[i] == '-')
				{
					cur = i;
					start = i+1;
					break;
				}
				if(i == l - 1)
					finish = 1;
			}
			if(!finish)
			{
				if(cur+k > l)
				{
					printf("Case #%d: IMPOSSIBLE\n", cnt);
			//		printf("cur=%d\n, l = %d\n", cur, l);
					finish = 1;
				}
				for(int i = cur; i < cur+k; i++)
				{
					if(s[i] == '-')
						s[i] = '+';
					else
						s[i] = '-';
				}
				step++;
			//	printf("now = %s\n", s);
			}
			else
			{
				printf("Case #%d: %d\n", cnt, step);
			}
			
		}
		cnt++;
	}



	return 0;
}