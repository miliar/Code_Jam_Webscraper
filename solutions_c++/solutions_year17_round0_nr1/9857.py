
#define _CRT_SECURE_NO_WARNINGS

#include <iostream>
#include <string>
using namespace std;

char line[1001] = { 0, };
int l = 0;
int k = 0;
int chk[1001] = { 0, };
int solve = 1e9;
int min(int a, int b)
{
	return (a > b) ? b : a;
}
int slen(char* t)
{
	char* p = &t[0];
	int len = 0;
	while (*p != 0)
		p++, len++;
	return len;
}
int check()
{
	int c = 0;
	while (line[c] == '+' && c < l)
		c++;
	if (c == l)
		return 1;
	return 0;
}
void foo(int id, int cnt)
{
	if (check())
	{
		solve = min(solve, cnt);
		return;
	}

	if (id + k > l)
		return;

	for (int i = id; i < id + k && i < l; i++)
	{
		if (line[i] == '-')
			line[i] = '+';
		else if (line[i] == '+')
			line[i] = '-';
	}
	chk[id] = 1;
	
	int next = id+1;
	while (line[next] != '-' && next < l)
		next++;

	if(chk[next] == 0)
		foo(next, cnt+1);

}
void init()
{
	for (int i = 0; i < 1001; i++)
	{
		line[i] = 0, chk[i] = 0;
	}
	solve = 1e9;
	l = 0, k = 0;
}
int main()
{
	int tc = 0, t=1;
	cin >> tc;
	while (tc--)
	{
		init();
		printf("Case #%d: ", t++);
		scanf("%s %d ", line, &k);

		l = slen(line);

		int chk = 0;
		for (int i = 0; i < l; i++)
		{
			if (line[i] == '-')
			{
				chk = 1;
				foo(i, 0);
				break;
			}
		}
		if (chk == 0)
			solve = 0;

		if (solve == 1e9)
			printf("IMPOSSIBLE\n");
		else
			printf("%d\n", solve);
		int d = 0;
	}

	return 0;
}
