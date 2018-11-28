#include<cstdio>

int T, n, A[7];
char ans[1010];

char ID(int x)
{
	if (x == 1) return 'R';
	if (x == 2) return 'O';
	if (x == 3) return 'Y';
	if (x == 4) return 'G';
	if (x == 5) return 'B';
	if (x == 6) return 'V';
}

void Doit()
{
	if (A[2] == A[5] && A[2] + A[5] == n)
	{
		for (int i = 1; i <= A[2]; i++) printf("OB"); printf("\n");
		return;
	}
	if (A[4] == A[1] && A[4] + A[1] == n)
	{
		for (int i = 1; i <= A[4]; i++) printf("GR"); printf("\n");
		return;
	}
	if (A[6] == A[3] && A[6] + A[3] == n)
	{
		for (int i = 1; i <= A[6]; i++) printf("VY"); printf("\n");
		return;
	}
	if (A[2] && A[2] >= A[5]) {printf("IMPOSSIBLE\n"); return;}
	if (A[4] && A[4] >= A[1]) {printf("IMPOSSIBLE\n"); return;}
	if (A[6] && A[6] >= A[3]) {printf("IMPOSSIBLE\n"); return;}
	A[1] -= A[4];
	A[3] -= A[6];
	A[5] -= A[2];
	int m = A[1] + A[3] + A[5];
	for (int i = 1; i <= 5; i += 2) if (A[i] * 2 > m) {printf("IMPOSSIBLE\n"); return;}
	int Max = A[1];
	if (A[3] > Max) Max = A[3];
	if (A[5] > Max) Max = A[5];
	int x = 0;
	for (int i = 1; i <= 5; i += 2) if (A[i] == Max)
	{
		while (A[i])
		{
			ans[x] = ID(i);
			A[i]--;
			x += 2;
			if (x >= m) x = 1;
		}
	}
	for (int i = 1; i <= 5; i += 2) if (A[i])
	{
		while (A[i])
		{
			ans[x] = ID(i);
			A[i]--;
			x += 2;
			if (x >= m) x = 1;
		}
	}
	for (int i = 0; i < m; i++)
	{
		printf("%c", ans[i]);
		if (ans[i] == 'R' && A[4])
		{
			for (int j = 1; j <= A[4]; j++) printf("GR");
			A[4] = 0;
		}
		if (ans[i] == 'Y' && A[6])
		{
			for (int j = 1; j <= A[6]; j++) printf("VY");
			A[6] = 0;
		}
		if (ans[i] == 'B' && A[2])
		{
			for (int j = 1; j <= A[2]; j++) printf("OB");
			A[2] = 0;
		}
	}
	printf("\n");
}

int main()
{
//	freopen("B.in", "r", stdin);
//	freopen("B.out", "w", stdout);
	scanf("%d", &T);
	for (int I = 1; I <= T; I++)
	{
		scanf("%d", &n);
		for (int i = 1; i <= 6; i++) scanf("%d", A + i);
		printf("Case #%d: ", I);
		Doit();
	}
	return 0;
}
