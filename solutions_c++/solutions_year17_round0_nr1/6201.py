#include<cstdio>
#include<cstring>

char S[1005];
int K, len;

void changeSide(int& start)
{
	int limit = start + K;
	if (limit > len) return;
	for (int i = start; i < limit; ++i)
	{
		S[i] = (S[i] == '-') ? '+' : '-';
	}
}

int main()
{
	/*freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);*/
	int t, T;
	scanf("%d", &T);
	for (t = 1; t <= T; ++t)
	{
		int result = 0;
		bool flag = true;
		scanf("%s %d", S, &K);
		len = strlen(S);

		for (int i = 0; S[i] != 0; ++i)
		{
			if (S[i] == '-') {
				changeSide(i);
				result++;
			}
		}

		for (int i = 0; S[i] != 0; ++i)
		{
			if (S[i] == '-') {
				flag = false;
				break;
			}
		}
		printf("Case #%d: ", t);
		(flag) ? printf("%d\n", result) : printf("IMPOSSIBLE\n");
		memset(S, 0, 1005);
	}
}