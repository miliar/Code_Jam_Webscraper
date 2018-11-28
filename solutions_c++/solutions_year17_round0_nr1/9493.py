#include <stdio.h>
#include <string.h>
int T, S, K;
char str[1001]; int flip[1001]; int cnt = 0;
int main(void)
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	scanf("%d", &T);
	for (int test_case = 1; test_case <= T; test_case++)
	{
		cnt = 0;
		memset(str, NULL, sizeof(str));
		memset(flip, 0, sizeof(flip));
		scanf("%s %d", &str, &K); int len = strlen(str);
		memmove(str + 1, str, sizeof(str)); str[0] = 'NULL';
		bool flag = false;
		for (int i = 1; i <= len; i++)
		{
			if (str[i] == '-') flag = true;
		}
		if (!flag)
		{
			printf("case #%d: ", test_case);
			printf("0\n");
			continue;
		}
		else
		{
			int j;
			for (int l = 1; l + K <= len + 1; l++)
			{
				j = l + K;
				if (str[l] == '+') continue;
				for (int i = l; i < j; i++)
				{
					if (str[i] == '-')
					{
						str[i] = '+'; 
					}
					else str[i] = '-'; 
				
				}
				cnt++;
			}
			bool rst = true;
			for (int i = 1; i <= len; i++)
			{
				if (str[i] == '-') rst = false;
			}
			printf("case #%d: ", test_case);
			if (rst) printf("%d\n", cnt);
			else printf("IMPOSSIBLE\n");
		}
	}
	return 0;
}