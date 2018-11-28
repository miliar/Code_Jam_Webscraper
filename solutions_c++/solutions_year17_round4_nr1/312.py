	//     . .. ... .... ..... be name khoda ..... .... ... .. .     \\

#include <bits/stdc++.h>
using namespace std;

inline int in() { int x; scanf("%d", &x); return x; }
const int N = 101;

int dp4[N][N][N], dp3[N][N];
int t[4];

int main()
{
	int _t = in();
	for(int _i = 1; _i <= _t; _i++)
	{
		printf("Case #%d: ", _i);
		int n = in(), p = in();
		fill(t, t + 4, 0);
		for(int i = 0; i < n; i++)
			t[in() % p]++;
		int ans = t[0];
		if(p == 2)
			ans += (t[1] + 1)/2;
		if(p == 3)
		{
			for(int i = 0; i <= t[1]; i++)
				for(int j = 0; j <= t[2]; j++)
				{
					int &x = dp3[i][j];
					x = 0;
					int sum = i + 2 * j;
					if(i)
						x = max(x, dp3[i - 1][j] + (sum % 3 == 1));
					if(j)
						x = max(x, dp3[i][j - 1] + (sum % 3 == 2));
				}
			ans += dp3[t[1]][t[2]];
		}
		if(p == 4)
		{
			for(int i = 0; i <= t[1]; i++)
				for(int j = 0; j <= t[2]; j++)
					for(int k = 0; k <= t[3]; k++)
					{
						int &x = dp4[i][j][k];
						x = 0;					
						int sum = i + 2 * j + 3 * k;
						if(i)
							x = max(x, dp4[i - 1][j][k] + (sum % 4 == 1)) ;
						if(j)
							x = max(x, dp4[i][j - 1][k] + (sum % 4 == 2));
						if(k)
							x = max(x, dp4[i][j][k - 1] + (sum % 4 == 3));
					}
			ans += dp4[t[1]][t[2]][t[3]];
		}
		cout << ans << endl;
	}
}
