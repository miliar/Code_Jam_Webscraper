/*
   _  __  U _____ u  _  __    
  |"|/ /  \| ___"|/ |"|/ /    
  | ' /    |  _|"   | ' /     
U/| . \\u  | |___ U/| . \\u   
  |_|\_\   |_____|  |_|\_\    
,-,>> \\,-.<<   >>,-,>> \\,-. 
 \.)   (_/(__) (__)\.)   (_/  
*/
#include <bits/stdc++.h>
using namespace std;

typedef long long ll;
typedef long double ld;
typedef vector<int> vi;
typedef pair<int, int> pii;
typedef pair<long long, long long> pll;
#define zhfs main
#define mp(a, b) make_pair(a, b)
#define fi first
#define se second
#define re return
#define forn(i, n) for (int i = 1; i <= n; i++)
char a[27][27];
bool on[27];
int zhfs()
{
#ifdef LOCAL
	freopen("input.txt", "r", stdin);
#endif
	int t;
	scanf("%d", &t);
	for (int tt = 1; tt <= t; tt++)
	{
		memset(a, 0, sizeof(a));
		memset(on, 0, sizeof(on));
		int n, m;
		scanf("%d %d", &n, &m);
		for (int i = 1; i <= n; i++)
		{
			scanf("%s", a[i]);
			for (int j = m; j >= 1; j--)
			{
				a[i][j] = a[i][j - 1];
			}
		}
		for (int i = 1; i <= n; i++)
		{
			bool have = false;
			for (int j = 1; j <= m; j++)
			{
				if (a[i][j] != '?') have = true;
			}
			if (have)
			{
				for (int j = 1; j <= m; j++)
				{
					if (a[i][j] == '?' && a[i][j - 1] >= 'A' && a[i][j - 1] <= 'Z')
					{
						a[i][j] = a[i][j - 1];
					}
				}
				for (int j = m; j >= 1; j--)
				{
					if (a[i][j] == '?' && a[i][j + 1] >= 'A' && a[i][j + 1] <= 'Z')
					{
						a[i][j] = a[i][j + 1];
					}
				}
				on[i] = true;
			}
			else if (on[i - 1])
			{
				for (int j = 1; j <= m; j++)
				{
					a[i][j] = a[i - 1][j];
				}
				on[i] = true;
			}
		}
		for (int i = n; i >= 1; i--)
		{
			if (!on[i])
			{
				assert(on[i + 1]);
				for (int j = 1; j <= m; j++)
				{
					a[i][j] = a[i + 1][j];
				}
				on[i] = true;
			}
		}
		printf("Case #%d:\n", tt);
		for (int i = 1; i <= n; i++)
		{
			for (int j = 1; j <= m; j++)
			{
				printf("%c", a[i][j]);
			}
			printf("\n");
		}
	}
}

