#include <iostream>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <algorithm>
#define maxn 1000


using namespace std;


int a[5000];
int lef[5000];
int righ[5000];


int main()
{
	int T;
	scanf("%d",&T);
	for(int cas = 1; cas <= T; cas++)
	{
		printf("Case #%d: ", cas);
		int n, k;
		scanf("%d%d", &n, &k);
		memset(a, 0, sizeof(a));
		memset(lef, 0, sizeof(lef));
		memset(righ, 0, sizeof(righ));
		a[0] = a[n + 1] = 1;
		lef[0] = lef[n+1] = righ[0] = righ[n+1] = -1;
		int ans1, ans2;
		for(int i = 1; i <= k; i++)
		{
			for(int j = 1; j <= n; j++)
			{
				if(a[j] == 0)
				{
					lef[j] = lef[j - 1] + 1;
				}
				else
				{
					lef[j] = -1;
				}
			}
			for(int j = n; j >= 1; j--)
			{
				if(a[j] == 0)
				{
					righ[j] = righ[j + 1] + 1;
				}
				else
				{
					righ[j] = -1;
				}
			}
			int minlsrs = -0x3f3f3f3f, max2 = -0x3f3f3f3f, chos;
			for(int j = 1; j <= n; j++)
			{
				//minlsrs = max(minlsrs, min(righ[j], lef[j]));
				if(minlsrs < min(righ[j], lef[j]))
				{
					minlsrs = min(righ[j], lef[j]);
					max2 = max(righ[j], lef[j]);
					chos = j;
				}
				else if(minlsrs == min(righ[j], lef[j]))
				{
					if(max2 < max(righ[j], lef[j]))
					{
						max2 = max(righ[j], lef[j]);
						chos = j;
					}
				}
			}
			ans2 = max2;
			ans1 = minlsrs;
			a[chos] = 1;
		}

		/*
		int minlsrs = -0x3f3f3f3f;
		int max2 = -0x3f3f3f3f;
		for(int j = 1; j <= n; j++)
		{
			//minlsrs = max(minlsrs, min(righ[j], lef[j]));
			if(minlsrs < min(righ[j], lef[j]))
			{
				minlsrs = min(righ[j], lef[j]);
			}
			if(max2 < max(righ[j], lef[j]))
			{
				max2 = max(righ[j], lef[j]);
			}
		}
		*/
		cout << ans2 << " " <<  ans1 << endl;
	}

	return 0;
}


