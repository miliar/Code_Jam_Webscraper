#include<cstdio>
int Hd, Hk, Ad, Ak, B, D;
inline int plus(int x) { return x > 0 ? x : 0; }
int main()
{
	int t, tc;
	scanf("%d", &tc);
	for (t = 1; t <= tc; t++)
	{
		scanf("%d%d%d%d%d%d", &Hd, &Ad, &Hk, &Ak, &B, &D);
		int ans = -1;
		for (int d = 0; (d - 1)*D <= Ak; d++)
		{
			if (!D && d) break;
			for (int b = 0; (b - 1)*B + Ad <= Hk; b++)
			{
				if (!B && b) break;
				int H = Hd, HK = Hk, AD = Ad, AK = Ak, turns = 0, dcnt = 0, bcnt = 0;
				while (dcnt < d && H > 0)
				{
					if (H <= plus(AK - D)) { turns++; H = Hd; H -= AK; }
					dcnt++; turns++; AK = plus(AK - D); H -= AK;
					if (H <= 0) break;
				}
				if (H <= 0) continue;
				while (bcnt < b && H > 0)
				{
					if (H <= AK) { turns++; H = Hd; H -= AK; }
					bcnt++; turns++; AD += B; H -= AK;
					if (H <= 0) break;
				}
				if (H <= 0) continue;
				while (HK > 0 && H > 0)
				{
					if (HK > AD && H <= AK) { turns++; H = Hd; H -= AK; }
					turns++; HK -= AD;
					if(HK > 0) H -= AK;
				}
				if (H <= 0) continue;
				if (ans<0 || ans>turns) ans = turns;
			}
		}
		printf("Case #%d: ", t);
		if (ans == -1) printf("IMPOSSIBLE\n");
		else printf("%d\n", ans);
	}
	return 0;
}
