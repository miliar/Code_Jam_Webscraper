#include<cstdio>
#include<vector>
using namespace std;
typedef vector<int> VI;
typedef vector<VI> VVI;
bool FindMatch(int i, const VVI &w, VI &mr, VI &mc, VI &seen) {
	for (int j = 0; j < w[i].size(); j++) {
		if (w[i][j] && !seen[j]) {
			seen[j] = true;
			if (mc[j] < 0 || FindMatch(mc[j], w, mr, mc, seen)) {
				mr[i] = j;
				mc[j] = i;
				return true;
			}
		}
	}
	return false;
}
int BipartiteMatching(const VVI &w, VI &mr, VI &mc) {
	mr = VI(w.size(), -1);
	mc = VI(w[0].size(), -1);

	int ct = 0;
	for (int i = 0; i < w.size(); i++) {
		VI seen(w[0].size());
		if (FindMatch(i, w, mr, mc, seen)) ct++;
	}
	return ct;
}
int n, m;
char given[128][128];
int main()
{
	int t, tc;
	scanf("%d", &tc);
	int k;
	int i, j;
	for (t = 1; t <= tc; t++)
	{
		scanf("%d%d", &n, &m);
		VVI perp(n, VI(n, 0)), diag(2*n-1, VI(2*n-1, 0));
		VI mrp, mcp, mrd, mcd;
		for (i = 0; i < n; i++)
		{
			for (j = 0; j < n; j++)
			{
				perp[i][j] = 1;
				diag[i + j][i - j + n - 1] = 1;
				given[i][j] = 0;
			}
		}
		for (k = 1; k <= m; k++)
		{
			int r, c;
			char buf[4];
			scanf("%s%d%d", buf, &r, &c);
			r--; c--;
			given[r][c] = buf[0];
			if (buf[0] != '+')
			{
				for (i = 0; i < n; i++)
				{
					if (i != c) perp[r][i] = 0;
					if (i != r) perp[i][c] = 0;
				}
			}
			if (buf[0] != 'x')
			{
				for (i = 0; i < 2 * n - 1; i++)
				{
					if (i != r + c) diag[i][r - c + n - 1] = 0;
					if (i != r - c + n - 1) diag[r + c][i] = 0;
				}
			}
		}
		BipartiteMatching(perp, mrp, mcp);
		BipartiteMatching(diag, mrd, mcd);
		printf("Case #%d: ", t);
		int tot = 0, cnt=0;
		for (i = 0; i < n; i++)
		{
			for (j = 0; j < n; j++)
			{
				bool f1 = (mrp[i]==j), f2 = (mrd[i + j] == i - j + n - 1);
				tot += (int)(f1)+(int)(f2);
				char ch;
				if (f1 && f2) ch = 'o';
				else if (f1) ch = 'x';
				else if (f2) ch = '+';
				else ch = 0;
				if (given[i][j] != ch) cnt++;
			}
		}
		printf("%d %d\n", tot, cnt);
		for (i = 0; i < n; i++)
		{
			for (j = 0; j < n; j++)
			{
				bool f1 = (mrp[i] == j), f2 = (mrd[i + j] == i - j + n - 1);
				char ch;
				if (f1 && f2) ch = 'o';
				else if (f1) ch = 'x';
				else if (f2) ch = '+';
				else ch = 0;
				if (given[i][j] != ch) printf("%c %d %d\n", ch, i + 1, j + 1);
			}
		}
	}
	return 0;
}
