#include <cmath>
#include <cstdio>
#include <vector>
#include <cstring>
#include <algorithm>

using namespace std;

#define pb push_back

typedef vector<int> vi;

vi e[1010];
bool v[1010][1010];
int s[1010];

int main()
{
	freopen("ha.in","r",stdin);
	freopen("ha.out","w",stdout);
	int test;scanf("%d",&test);
	for (int T=1;T<=test;T++)
	{
		int n,c,m;scanf("%d%d%d",&n,&c,&m);
		for (int i=1;i<=n;i++) e[i].clear();
		for (int i=1;i<=m;i++)
		{
			int x,y;scanf("%d%d",&x,&y);
			e[x].pb(y);
		}
		for (int i=1;i<=m;i++)
			memset(v[i]+1,0,c*sizeof(bool));
		memset(s+1,0,m*sizeof(int));
		bool ok=1;
		int l =0 ;
		for (int i=1;i<=n;i++)
		{
			for (vi::iterator p=e[i].begin();p!=e[i].end();p++)
			{
				bool ok2=0;
				for (int j=1;j<=m;j++)
					if (s[j]<i&&!v[j][*p])
					{
						s[j]++;v[j][*p]=1;
						ok2=1;
						l = max(l,j);
						break;
					}
				if (!ok2) {ok=0;break;}
			}
			if (!ok) break;
		}
		int ans=0;
		for (int i=1;i<=n;i++)
		{
			int s=0;
			for (vi::iterator p=e[i].begin();p!=e[i].end();p++) s++;
			ans+=max(0,s-l);
		}
		printf("Case #%d: %d %d\n",T,l,ans);
	}
	return 0;
}