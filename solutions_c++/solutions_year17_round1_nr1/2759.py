#include <bits/stdc++.h>
using namespace std;

#define fo(i,s,t) for(int i = s; i <= t; ++ i)
const int maxn = 26;

char s[maxn][maxn];
bool app[maxn];
int n, m, t;

void init()
{
	scanf("%d%d",&n,&m);
	memset(s,0,sizeof(s));
	fo(i,1,n) scanf("%s",s[i]+1);
	memset(app,false,sizeof(app));
	fo(i,1,n) fo(j,1,m) app[s[i][j]-'A'] = true;
}

bool check(char c)
{
	int lx, ly, rx, ry;
	lx = ly = 1<<30;
	rx = ry = 0;
	fo(i,1,n) fo(j,1,m) if(s[i][j] == c)
	{
		lx = min(lx,i); ly = min(ly,j);
		rx = max(rx,i); ry = max(ry,j);
	}
	fo(i,lx,rx) fo(j,ly,ry) if(s[i][j] != c && s[i][j] != '?')
		return false;
	return true;
}

void solve()
{
	fo(i,1,n) fo(j,1,m) if(s[i][j] == '?')
	{
		fo(k,0,25) if(app[k])
		{
			s[i][j] = (char)('A'+k);
			bool ok = true;
			fo(z,0,25) if(!check(z+'A')) {ok = false; break;}
			if(ok) break;
		}
	}
	fo(i,1,n) {fo(j,1,m) printf("%c",s[i][j]); putchar('\n');}
}

int main()
{
	// freopen("1.in","r",stdin);
	// freopen("1.out","w",stdout);
	scanf("%d",&t);
	fo(qwq,1,t)
	{
		init();
		printf("Case #%d:\n",qwq);
		solve();
	}
	return 0;
}