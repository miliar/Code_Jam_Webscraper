#include <cstdio>
#include <cstring>

char buf[1002];

void flip(int s, int e)
{
	for(int i = s; i < e; i++)
	{
		if(buf[i] == '+') buf[i] = '-';
		else buf[i] = '+';
	}
}

int main()
{
	int T;
	scanf("%d", &T);
	for(int t = 0; t < T; t++)
	{
		int K;
		scanf(" %s%d", buf, &K);
		int len = strlen(buf);
		
		int count = 0;
		for(int i = 0; i < len; i++) if(buf[i] == '-')
		{
			if(i + K > len)
			{
				count = -1;
				break;
			}
			count++;
			flip(i, i + K);
		}
		if(count == -1)
			printf("Case #%d: IMPOSSIBLE\n", t + 1);
		else printf("Case #%d: %d\n", t + 1, count);
	}
}
