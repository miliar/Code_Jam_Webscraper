#include <bits/stdc++.h>
#define f(x, y, z) for(int x = (y); x <= (z); ++x)
#define g(x, y, z) for(int x = (y); x < (z); ++x)
#define h(x, y, z) for(int x = (y); x >= (z); --x)
using namespace std;

char a[66][66];

int main()
{
	int T; cin >> T;
	f(_, 1, T)
	{
		int n, m; cin >> n >> m;
		memset(a, 0, sizeof(a));
		g(i, 0, n) cin >> a[i];
		g(i, 0, n)
		{
			char c = '?';
			g(j, 0, m) if(a[i][j] != '?')
			{
				c = a[i][j]; break;
			}
			if(c == '?') continue;
			g(j, 0, m) if(a[i][j] != '?') c = a[i][j]; else a[i][j] = c;
		}
		int li = 0; while(li < n && a[li][0] == '?') ++li;
		if(li == n) throw 233;
		g(i, 0, n) if(a[i][0] == '?') memcpy(a[i], a[li], sizeof(a[i])); else li = i;
		printf("Case #%d:\n", _);
		g(i, 0, n) cout << a[i] << endl;
	}
	return 0;
}
