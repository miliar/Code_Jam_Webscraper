#include <cstdio>
#include <cstring>
#include <algorithm>

const int inf = 0xc0c0c0c0;

using namespace std;

int f[110][110][110];
int main()
{
	int T; 
	freopen("A-large.in", "r", stdin);
	freopen("a.out", "w", stdout);
	scanf("%d", &T);
	for (int _T = 1; _T <= T; _T++)
	{
		int cnt[4];
		int N, P;
		scanf("%d%d", &N, &P);
		memset(cnt, 0, sizeof(cnt));
		for (int i = 0; i < N; i++)
		{
			int a;
			scanf("%d", &a);
			cnt[a % P]++;
		}
		int ans, U, N1;
		switch (P)
		{
			case 2:
				ans = cnt[0] + (cnt[1] + 1) / 2;
				break;
			case 3:
				U = min(cnt[1], cnt[2]);
				ans = cnt[0] + U + (cnt[1] - U + 2) / 3 + (cnt[2] - U + 2) / 3;
				break;
			case 4:
				memset(f, 0xc0, sizeof(f));
				f[0][0][0] = 0;
				N1 = N - cnt[0];
				for (int i = 0; i < N1; i++)
					for (int j = 0; j <= cnt[1]; j++)
						for (int k = 0; k <= cnt[2]; k++)
						{
							int l = i - j - k, B = ((j + k * 2 + l * 3) % 4 == 0);
							if (j < cnt[1]) f[j + 1][k][l] = max(f[j + 1][k][l], f[j][k][l] + B);
							if (k < cnt[2]) f[j][k + 1][l] = max(f[j][k + 1][l], f[j][k][l] + B);
							if ((l >= 0) && (l < cnt[3])) f[j][k][l + 1] = max(f[j][k][l + 1],f[j][k][l] + B);
						}
				ans = f[cnt[1]][cnt[2]][cnt[3]] + cnt[0];
		}
		printf("Case #%d: %d\n", _T, ans);
	}
	return 0;
}
