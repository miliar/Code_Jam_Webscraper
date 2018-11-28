#include<cstdio>
#include<cstring>

char input[20];
char result[20];

void sol(int& len)
{
	int i = 0;
	while (i < len - 1)
	{
		if (input[i] > input[i + 1])
		{
			result[i] = input[i] - 1;
			break;
		}
		else result[i] = input[i];
		i++;
	}

	for (i = i + 1; i < len; ++i)
		result[i] = '9';
	if (result[0] == '0') {
		result[0] = '9';
		result[len - 1] = 0;
	}
}

bool check()
{
	int len = strlen(result);
	for (int i = 0; i < len - 1; ++i)
	{
		if (result[i] > result[i + 1])
			return false;
	}
	return true;
}

int main()
{
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);
	int t, T;
	scanf("%d", &T);

	for (t = 1; t <= T; ++t)
	{
		int len;
		scanf("%s", input);
		len = strlen(input);
		strcpy(result, input);
		
		sol(len);
		while (!check()) {
			strcpy(input, result);
			sol(len);
		}
		
		printf("Case #%d: %s\n", t, result);
		memset(input, 0, 20);
		memset(result, 0, 20);
	}
}