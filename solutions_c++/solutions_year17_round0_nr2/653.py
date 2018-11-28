#include <cstdio>
#include <cstring>
char S[25];
int main()
{
	int T;
	freopen("B-large.in", "r", stdin);
	freopen("B.out", "w", stdout);
	scanf("%d", &T);
	for (int _T = 1; _T <= T; _T++)
	{
		scanf("%s", S);
		int L = strlen(S);
		bool flag;
		do
		{
			flag = false;
			for (int i = 1; i < L; i++)
				if (S[i] < S[i - 1])
				{
					S[i - 1]--;
					for (int j = i; j < L; j++) S[j] = '9';
					flag = true;
					break;
				}
		}
		while (flag);
		printf("Case #%d: ", _T);
		for (int i = 0; i < L; i++)
			if (S[i] != '0') printf("%c", S[i]);
		printf("\n");
	}
	return 0;
}
