#include <cstdio>
#include <cstring>
char S[1050];
bool A[1050];
int N, K;
int main()
{
	int T;
	freopen("A-large.in", "r", stdin);
	freopen("A.out", "w", stdout);
	scanf("%d", &T);
	for (int _T = 1; _T <= T; _T++)
	{
		scanf("%s%d", S, &K);
		N = strlen(S);
		for (int i = 0; i < N; i++)
			A[i] = (S[i] != '+');
		int cnt = 0;
		for (int i = 0; i <= N - K; i++)
			if (A[i])
			{
				cnt++;
				for (int j = i; j < i + K; j++) A[j] ^= 1;
			}
		bool flag = true;
		for (int i = 0; i < N; i++)
			if (A[i])
			{
				flag = false;
				break;
			}
		printf("Case #%d: ", _T);
		if (flag) printf("%d\n", cnt);
		else printf("IMPOSSIBLE\n");
	}
	return 0;
}
