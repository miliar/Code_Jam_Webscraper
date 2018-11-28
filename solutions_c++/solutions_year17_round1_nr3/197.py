#include <iostream>
#include <stdlib.h>
#include <algorithm>
#include <string>
#include <vector>
#include <cmath>
using namespace std;

int T;

int Hd, Ad, Hk, Ak, B, D;

void Solve()
{
	scanf("%d %d %d %d %d %d", &Hd, &Ad, &Hk, &Ak, &B, &D);
	int ans = 1000000000;
	for (int i = 0; i < ((D ==0)?0:Ak / D) + 2; i++)
	{	
		for (int j = 0; j < ((B==0)?0:Hk / B) + 2; j++)
		{

			int n_Ak = Ak, n_Hd = Hd, cnt_i = i;
			int n_Ad = Ad, n_Hk = Hk, cnt_j = j;
			int turn = 0;

			while (n_Hk > 0)
			{
				if (n_Hd > n_Ak - D && cnt_i > 0)
				{
					n_Ak -= D;
					cnt_i--;
				}
				else if (n_Hd > n_Ak && cnt_j > 0)
				{
					n_Ad += B;
					cnt_j--;
				}
				else if (n_Hd > n_Ak || n_Hk <= n_Ad)
					n_Hk = max(n_Hk - n_Ad, 0);
				else
					n_Hd = Hd;

				n_Hd = n_Hd - n_Ak;
				turn++;
				if ((n_Hd <= 0 && n_Hk != 0) || turn > 1000)
				{
					turn = 1000000000;
					break;
				}
			}
			ans = min(ans, turn);
		}
	}
	if (ans == 1000000000)
		printf("IMPOSSIBLE\n");
	else
		printf("%d\n", ans);
}

int main()
{
	freopen("C-small-attempt0.in", "r", stdin);
	freopen("C-small-attempt0.out", "w", stdout);
	scanf("%d\n", &T);
	for (int i = 0; i < T; i++)
	{
		printf("Case #%d: ", i + 1);
		Solve();
	}
}