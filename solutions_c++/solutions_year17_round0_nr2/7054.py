#include <cstdio>
#include <cstring>
char str[1010];
void SubOne(int x)
{
	str[x] --;
	for (int i = x - 1; i >= 0; i --)
	{
		if (str[i] > str[i + 1])
		{
			str[i] --;
			str[i + 1] = 9;
		}
	}
}
int main()
{
	freopen("ans", "w", stdout);
	int T;
	scanf("%d", &T);
	for (int cas = 1; cas <= T; cas ++)
	{
		int n;
		scanf("%s", str);
		int len = strlen(str);
		for (int i = 0; i < len; i ++)
		{
			str[i] -= '0';
		}
		int last = -1;
		for (int i = 0; i < len; i ++)
		{
			if (str[i] < last)
			{
				SubOne(i - 1);
				for (int j = i; j < len; j ++)
					str[j] = 9;
				//for (int j = 0; j < len; j ++)
				//	printf("%d", str[j]);puts("");
				break;
			}
			last = str[i];
		}
		int st = 0;
		while(str[st] == 0) st ++;
		for (int i = st; i < len; i ++)
		{
			str[i] += '0';
		}
		printf("Case #%d: %s\n", cas, str + st);
	}	
	return 0;
}