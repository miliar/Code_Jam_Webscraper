#include <cstdio>
#include <cstring>
#include <algorithm>

using namespace std;

char Buf[10000];
int k;

void Work()
{
	scanf("%s%d", Buf, &k);
	int n = strlen(Buf);
	int Cnt = 0;
	for (int i = 0; i + k - 1 < n; i ++)
	{
		if (Buf[i] == '+')
			continue;
		Cnt ++;
		for (int j = 0; j < k; j ++)
			Buf[i + j] = '+' + '-' - Buf[i + j];
	}
	for (int i = 0; i < n; i ++)
		if (Buf[i] != '+')
			Cnt = -1;
	if (Cnt == -1)
		printf("IMPOSSIBLE\n");
	else
		printf("%d\n", Cnt);
}

int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	int Cases;
	scanf("%d", &Cases);
	for (int Case = 1; Case <= Cases; Case ++)
	{
		printf("Case #%d: ", Case);
		Work();
		fflush(stdout);
	}
	return 0;
}