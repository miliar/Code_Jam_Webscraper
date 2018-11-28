#include <cstdio>
#include <cstring>
char A[1001];
int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int T;
	scanf("%d", &T);
	for(int t = 1; t <= T; t++)
	{
		scanf("%s", &A[1]);
		int N = strlen(&A[1]);
		int K;
		scanf("%d", &K);

		int Ans = 0;
		for(int i = 1; i <= N - K + 1; i++)
		{
			if(A[i] == '-')
			{
				Ans++;
				for(int j = i; j < i + K; j++) A[j] = A[j] == '-' ? '+' : '-';
			}
		}
		bool flag = false;
		for(int i = 1; i <= N; i++) if(A[i] == '-') flag = true;
		printf("Case #%d: ", t);
		if(flag) printf("IMPOSSIBLE");
		else printf("%d", Ans);
		printf("\n");
	}
}