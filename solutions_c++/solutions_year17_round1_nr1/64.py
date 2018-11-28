#include<cstdio>
char A[30][30];
int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int T;
	scanf("%d", &T);
	for(int j = 0; j < 30; j++) A[0][j] = '?';
	for(int t = 1; t <= T; t++)
	{
		int N, M;
		scanf("%d %d", &N, &M);
		for(int i = 1; i <= N; i++) scanf("%s", &A[i][1]);
		for(int i = 1; i <= N; i++)
		{
			bool flag = false;
			for(int j = 1; j <= M; j++) if(A[i][j] != '?') flag = true;
			if(flag)
			{
				int s = 1; char c;
				for(int j = 1; j <= M; j++)
				{
					if(A[i][j] != '?')
					{
						c = A[i][j];
						for(int k = s; k < j; k++) A[i][k] = c;
						s = j + 1;
					}
				}
				for(int k = s; k <= M; k++) A[i][k] = c;
			}
		}
		for(int i = N - 1; i >= 1; i--)
		{
			for(int j = 1; j <= M; j++)
			{
				if(A[i][j] == '?') A[i][j] = A[i + 1][j];
			}
		}
		for(int i = 2; i <= N; i++)
		{
			for(int j = 1; j <= M; j++)
			{
				if(A[i][j] == '?') A[i][j] = A[i - 1][j];
			}
		}
		printf("Case #%d:\n", t);
		for(int i = 1; i <= N; i++)
		{
			for(int j = 1; j <= M; j++) printf("%c", A[i][j]);
			printf("\n");
		}
	}
}