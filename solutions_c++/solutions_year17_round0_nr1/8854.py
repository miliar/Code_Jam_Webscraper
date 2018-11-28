#pragma warning(disable : 4996)
#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cstring>

using namespace std;

char pancake[1001];
int s, k;

int flipPC(char *pc, char face)
{
	int flipCnt = 0;
	for (int i = 0; i < s - k + 1; i++)
	{
		if (pc[i] == face) continue;
		flipCnt++;
		for (int j = 0; j < k; j++)
		{
			if (pc[i + j] == '-')
				pc[i + j] = '+';
			else
				pc[i + j] = '-';
		}
	}

	for (int i = 0; i < s; i++)
		if (pc[i] != face)
			return 987654321;

	return flipCnt;
}

void solve()
{
	
	scanf("%s %d", pancake, &k);
	s = strlen(pancake);

	int ans = 987654321;
	char pc[1001];
	
	strcpy(pc, pancake);
	ans = min(ans, flipPC(pc, '+'));
	
	strcpy(pc, pancake);
	reverse(&pc[0], &pc[s]);
	ans = min(ans, flipPC(pc, '+'));


	if (ans == 987654321)
		printf("IMPOSSIBLE\n");
	else
		printf("%d\n", ans);

}

int main()
{
	int tc;
	scanf("%d", &tc);
	for (int i = 1; i <= tc; i++)
	{
		printf("Case #%d: ", i);
		solve();
	}
	return 0;
}