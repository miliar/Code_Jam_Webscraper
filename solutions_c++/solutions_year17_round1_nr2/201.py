#include <bits/stdc++.h>
#define f(x, y, z) for(int x = (y); x <= (z); ++x)
#define g(x, y, z) for(int x = (y); x < (z); ++x)
#define h(x, y, z) for(int x = (y); x >= (z); --x)
using namespace std;

typedef pair<int, int> pii;
#define l first
#define r second

int o[69];
pii q[69][69]; int p[69];

int main()
{
	int T; cin >> T;
	f(_, 1, T)
	{
		int n, m; cin >> n >> m;
		memset(o, 0, sizeof(o));
		memset(q, 0, sizeof(q));
		memset(p, 0, sizeof(p));
		g(i, 0, n) cin >> o[i];
		g(i, 0, n) g(j, 0, m)
		{
			int x; cin >> x;
			int l = (10 * x + 11 * o[i] - 1) / (11 * o[i]);
			int r = (10 * x) / (9 * o[i]);
			q[i][j] = pii(l, r);
		}
		g(i, 0, n) sort(q[i], q[i] + m);
		int ans = 0;
		for(;;)
		{
			bool fin = false;
			g(i, 0, n) if(p[i] == m) fin = true;
			if(fin) break;
			int maxl = -1, minr = 1 << 30;
			g(i, 0, n)
			{
				maxl = max(maxl, q[i][p[i]].l);
				minr = min(minr, q[i][p[i]].r);
			}
			if(maxl <= minr)
			{
				g(i, 0, n) ++p[i];
				++ans;
			}
			else
			{
				g(i, 0, n) if(q[i][p[i]].r == minr) ++p[i];
			}
		}
		printf("Case #%d: %d\n", _, ans);
	}
	return 0;
}
