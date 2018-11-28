#include <iostream>
#include <cstdio>
#include <cmath>
#include <vector>
#include <set>
#include <map>
#include <unordered_set>
#include <unordered_map>
#include <utility>
#include <algorithm>
#define ll long long
using namespace std;

const int mod = 1000000000 + 7;
const double eps = 1e-9;

int g[5];

int main()
{
	freopen("0.in", "r", stdin);
	freopen("0.out", "w", stdout);

	int t;
	
	scanf("%d", &t);

	for(int te = 1; te <= t; te++)
	{
		printf("Case #%d: ", te);
		int n, p;

		g[0] = g[1] = g[2] = g[3] = 0;

		scanf("%d %d", &n, &p);

		for(int i = 0; i < n; i++)
		{
			int x;
			scanf("%d", &x);
			g[x % p]++;
		}

		if(p == 2)
		{
			printf("%d\n", g[0] + (g[1] + 1) / 2);
		}
		if(p == 3)
		{
			int ans = g[0] + min(g[1], g[2]);
			int lft = max(g[1], g[2]) - min(g[1], g[2]);

			ans = ans + (lft + 2) / 3;

			cout<<ans<<endl; 
		}
		if(p == 4)
		{
			int ans = g[0] + g[2] / 2 + min(g[1], g[3]);
			int lft_two;
			int lft_one;
			lft_one = max(g[1], g[3]) - min(g[1], g[3]);
			if((g[2] & 1))
			{
				lft_two = 1;
			}
			else
			{
				lft_two = 0;
			}

			if(lft_two)
			{
				if(lft_one >= 2)
				{
					ans = ans + 1;
					lft_one = lft_one - 2;
					ans = ans + (lft_one + 3) / 4;
				}
				else
				{
					ans = ans + 1;
				}
			}
			else
			{
				ans = ans + (lft_one + 3) / 4;
			}
			cout<<ans<<endl;
		}
	}


	return 0;
}