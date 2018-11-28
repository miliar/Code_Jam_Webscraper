#include <set>
#include <cmath>
#include <stack>
#include <cstdio>
#include <cstring>
#include <iostream>
#include <algorithm>
#include <cstdlib>
#include <numeric>
#include <vector>
#include <ctime>
#include <queue>
#include <list>
#include <map>
#define pi acos(-1.0)
#define INF 0x3f3f3f3f
#define clr(x)  memset(x,0,sizeof(x));
#define clrto(x,siz,y)  for(int xx=0;xx<=siz;xx++)  x[xx]=y;
#define clrset(x,siz)  for(int xx=0;xx<=siz;xx++)  x[xx]=xx;
#define clr_1(x) memset(x,-1,sizeof(x));
#define clrmax(x) memset(x,0x3f,sizeof(x));
#define clrvec(x,siz) for(int xx=0;xx<=siz;xx++)  x[xx].clear();
#define fop2   freopen(".in","r",stdin); //freopen(".out","w",stdout);
#define fop   freopen("in.txt","r",stdin);freopen("out.txt","w",stdout);
#define getfile char fin[11], fout[11]; sprintf(fin, "%d.in", i); sprintf(fout, "%d.out", i); freopen(fin, "r", stdin); freopen(fout, "w", stdout);
#define makefile char fout[11]; sprintf(fout, "%d.in", i); freopen(fout, "w", stdout);
#define myprogram By_135678942570
#define clrcpy(x,siz,y)  for(int xx=0;xx<siz;xx++)  x[xx]=y[xx];
#define pb push_back
using namespace std;
int main()
{
	fop;
	int T, cas = 0;
	scanf("%d", &T);
	while(T--)
	{
		int n, q;
		scanf("%d%d", &n, &q);
		int e[111], s[111];
		long long f[111][111];
		for(int i = 1; i <= n; i++)
			scanf("%d%d", &e[i], &s[i]);
		for(int i = 1; i <= n; i++)
			for(int j = 1; j <= n; j++)
			{
				scanf("%d", &f[i][j]);
				if(f[i][j] == -1)
					f[i][j] = 0x3f3f3f3f3f3f3f3fll;
			}
		for(int k = 1; k <= n; k++)
			for(int i = 1; i <= n; i++)
				for(int j = 1; j <= n; j++)
					f[i][j] = min(f[i][j], f[i][k] + f[k][j]);
		printf("Case #%d:", ++cas);
		while(q--)
		{
			int u, v;
			scanf("%d%d", &u, &v);
			double dd[111];
			int vis[111] = {0};
			for(int i = 1; i <= n; i++)
				dd[i] = 9999999999999999999.0;
			dd[u] = 0;
			int last = u;
			vis[u] = 1;
			while(last != v)
			{
				for(int i = 1; i <= n; i++)
					if(f[last][i] <= e[last])
						dd[i] = min(dd[i], dd[last] + 1.0 * f[last][i] / s[last]);
				int nxt = -1;
				for(int i = 1; i <= n; i++)
					if(vis[i] != 1 && (nxt == -1 || dd[nxt] > dd[i]))
						nxt = i;
				last = nxt;
				vis[last] = 1;
			}
			printf(" %.10f", dd[v]);
		}
		puts("");
	}
}