#include <bits/stdc++.h>
using namespace std;

int T, H1, A1, H2, A2, B, D;
int Ans;

int main()
{
	
	freopen("C.in", "r", stdin);
	freopen("C.out", "w", stdout);
	
	scanf("%d", &T);
	for (int Case = 1; Case <= T; ++ Case)
	{
		printf("Case #%d: ", Case);
		scanf("%d%d%d%d%d%d", &H1, &A1, &H2, &A2, &B, &D);
		
		if (A1 >= H2) 
		{
			printf("1\n");
			continue;
		}
		if (A2 - D >= H1)
		{
			printf("IMPOSSIBLE\n");
			continue;
		}
		
		Ans = 1000000000;
		for (int t1 = 0; t1 <= 100; ++ t1)
			for (int t2 = 0; t2 <= 100; ++ t2)
			{
				int flag = 1;
				if (D == 0 && t2 != 0) continue;
				int tH1 = H1; int tA1 = A1;
				int tH2 = H2; int tA2 = A2;
				int tmp = 0;
				for (int i = 1; i <= t2;)
				{
					if (tH1 <= tA2 - D)
					{
						++ tmp; tH1 = H1 - tA2;
						if (tH1 <= tA2 - D)
						{
							flag = 0;
							break;
						}
					} else {
						tA2 = max(0, tA2 - D);
						tH1 -= tA2; ++ i;
					}
				}
				for (int i = 1; i <= t1;)
				{
					if (tH1 <= tA2)
					{
						++ tmp; tH1 = H1 - tA2;
						if (tH1 <= tA2)
						{
							flag = 0;
							break;
						}
					} else {
						tA1 += B; ++ i;
						tH1 -= tA2;
					}
				}
				while (tH2 > 0)
				{
					if (tH1 <= tA2 && tH2 > tA1)
					{
						tH1 = H1 - tA2;
						if (tH1 <= tA2)
						{
							flag = 0;
							break;
						}
						++ tmp;
					} else {
						tH2 -= tA1;
						tH1 -= tA2;
						++ tmp;
					}
				}
				if (flag) Ans = min(Ans, t1 + t2 + tmp);
			}
		if (Ans == 1000000000) printf("IMPOSSIBLE\n");
		else printf("%d\n", Ans);
	}
	return 0;
}

