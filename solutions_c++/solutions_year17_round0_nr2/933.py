#include <iostream>
#include <cstdio>
#include <cstring>
using namespace std;

int T, N;
char str[100];

int main()
{
	freopen("B.in", "r", stdin);
	freopen("B.out", "w", stdout);

	scanf("%d", &T);
	for (int id = 1; id <= T; id++)
	{
		scanf("%s", str+1);
		N = strlen(str+1);
		int i;
		printf("Case #%d: ", id);
		for (i=N; i>1; i--)
			if (str[i-1] > str[i])
			{
				str[i-1]--;
				for (int j=i; j<=N; j++)
					str[j] = '9';
			}
		for (int i=1; i<=N; i++)
			if (i==1 && str[i] == '0') continue;
			else printf("%c", str[i]);
		printf("\n");
	}
	return 0;
}
