#include <stdio.h>

char str[30];
int L;
char res[30];

inline int max(int a, int b)
{
	if (a > b)	return a;
	return b;
}

bool solve(int prv, int index, bool flag)
{
	if (index == L)
	{
		res[index] = '\0';
		return true;
	}
	int l = flag ? 9 : str[index] - '0';
	for (int i = l; i >= prv; i--)
	{
		res[index] = i + '0';
		if (solve(i, index + 1,flag))
			return true;
		flag = true;
	}
	if (index == 0 && solve(prv, index + 1, true))
	{
		int i;
		for (i = 1; res[i]; i++)
			res[i - 1] = res[i];
		res[i - 1] = '\0';
		return true;
	}
	return false;
}

int main()
{
	int T;
	scanf("%d", &T);
	for (int t = 1; t <= T; t++)
	{
		scanf("%s", &str);
		L = 0;
		for (int i = 0; str[i]; i++) L++;
		solve(1,0, false);
		printf("Case #%d: %s\n", t, res);
	}
	return 0;
}