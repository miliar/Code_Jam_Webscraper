#include<bits/stdc++.h>
#define REP(x,y,z) for(int x=y;x<=z;x++)
#define FORD(x,y,z) for(int x=y;x>=z;x--)
#define MSET(x,y) memset(x,y,sizeof(x))
#define FOR(x,y) for(__typeof(y.begin()) x=y.begin();x!=y.end();x++)
#define F first
#define S second
#define MP make_pair
#define PB push_back
#define SZ size()
#define M 55
void RI(){}
template<typename... T>
void RI( int& head, T&... tail ) {
    scanf("%d",&head);
    RI(tail...);
}
using namespace std;
typedef long long LL;
typedef pair<int,int> P;
int t,n,m;
/*
 * \ = 01 23
 * / = 03 12
 */
int dx[4]={1,0,-1,0};
int dy[4]={0,1,0,-1};
int cant[M][M][2]; //0=-, 1=|
char mp[M][M];
bool vis[M][M][4];
vector<tuple<int,int,int>> option[M][M];
vector<P> res;
////////////////
int n2,id,id2,newid[M][M];
int dfn[M*M*2], low[M*M*2], belong[M*M*2];
int s[M*M*2], top;
bool ins[M*M*2],ans[M*M*2];
vector<int> e[M*M*2];
vector<int> point[M*M*2];
////////////////

bool inside(int x,int y,int d)
{
	return x>=1 && x<=n && y>=1 && y<=m && mp[x][y]!='#' && !vis[x][y][d];
}
int partner(int x)
{
	if(x>n2) return x-n2;
	return x+n2;
}
void go(int x,int y,int d)
{
	while(inside(x,y,d))
	{
		vis[x][y][d] = true;
		res.PB(MP(x,y));

		if(mp[x][y]=='\\')
			d^=1;
		else if(mp[x][y]=='/')
			d^=3;

		x += dx[d];
		y += dy[d];
	}
}
void from(int x,int y,int dir)//d is reversed
{
	MSET(vis, false);
	res.clear();

	int d1=dir, d2=dir+2; //02 or 13
	go(x+dx[d1], y+dy[d1], d1);
	go(x+dx[d2], y+dy[d2], d2);

	bool fail=false;
	for(auto i:res) if(mp[i.F][i.S]!='.')
	{
		fail = true;
		break;
	}
	
	if(fail)
	{
		cant[x][y][dir^1] = true;
	}
	else
	{
		for(auto i:res) option[i.F][i.S].PB( make_tuple(x,y,dir^1) );
	}
}
void dfs(int cur)
{
	dfn[cur] = low[cur] = ++id;
	s[top++] = cur;
	ins[cur] = true;
	for(int i:e[cur])
	{
		if(!dfn[i])
		{
			dfs(i);
			low[cur] = min(low[cur], low[i]);
		}
		else if(ins[i])
			low[cur] = min(low[cur], dfn[i]);
	}
	if(dfn[cur]==low[cur])
	{
		++id2;
		while(true)
		{
			belong[s[top-1]] = id2;
			ins[s[top-1]] = false;
			if(s[--top] == cur) break;
		}
	}
}
void topsort(int cur)
{
	dfn[cur] = 1;
	for(int i:e[cur]) if(!dfn[i]) dfs(i);
	s[top++] = cur;
}
bool work()
{
	int a,b,c;
	int a2,b2,c2;
	int x,y;
	n2 = id = id2 = top = 0;
	MSET(dfn,0);
	MSET(ins,false);
	REP(i,0,n*m*2) e[i].clear();
	REP(i,1,n)REP(j,1,m)if(mp[i][j]=='-' || mp[i][j]=='|')
		newid[i][j] = ++n2;
	
	REP(i,1,n)REP(j,1,m)if(mp[i][j]=='-' || mp[i][j]=='|')
	{
		x = newid[i][j];
		if(cant[i][j][0])
			e[x].PB(x+n2);
		if(cant[i][j][1])
			e[x+n2].PB(x);
	}
	
	REP(i,1,n)REP(j,1,m)if(mp[i][j]=='.')
	{
		if(option[i][j].size()==0) return false;
		if(option[i][j].size()==1)
		{
			tie(a,b,c) = option[i][j][0];
			x = newid[a][b];
			if(c==0)
				e[x+n2].PB(x);
			else
				e[x].PB(x+n2);
		}
		if(option[i][j].size()==2)
		{
			tie(a,b,c) = option[i][j][0];
			tie(a2,b2,c2) = option[i][j][1];

			x = newid[a][b];
			y = newid[a2][b2];

			e[x + (c^1)*n2].PB(y+c2*n2);
			e[y + (c2^1)*n2].PB(x+c*n2);
		}
	}
	
	REP(i,1,2*n2) if(!dfn[i]) dfs(i);
	
	REP(i,1,2*n2) if(belong[i] == belong[partner(i)])
		return false;

	return true;
}
void rebuild_answer()
{
	top = 0;
	MSET(dfn,0);
	MSET(ans,false);
	vector<pair<int,int>> edges;
	REP(i,0,2*n2) point[i].clear();
	REP(i,1,2*n2)
	{
		for(int j:e[i]) edges.PB(MP(i,j));
		e[i].clear();
	}

	for(auto i:edges) if(belong[i.F] != belong[i.S])
		e[belong[i.F]].PB(belong[i.S]);
	REP(i,1,2*n2) point[belong[i]].PB(i);
	REP(i,1,id2) if(!dfn[i]) topsort(i);

	FORD(i,top-1,0)
	{
		REP(j,0,(int)point[i].SZ-1)
		{
			if(ans[partner(point[i][j])])
			{
				int x = belong[partner(point[i][j])];
				REP(k,0,(int)point[x].SZ-1)
					ans[point[x][k]] = false;
			}
			ans[point[i][j]] = true;
		}
	}
}
int main()
{
	RI(t);
	REP(tt,1,t)
	{
		RI(n,m);
		MSET(cant, 0);
		REP(i,1,n)REP(j,1,m) option[i][j].clear();
		REP(i,1,n) scanf("%s",mp[i]+1);

		REP(i,1,n)REP(j,1,m)if(mp[i][j]=='-' || mp[i][j]=='|')
		{
			from(i,j,0);
			from(i,j,1);
		}
		REP(i,1,n)REP(j,1,m)
		{
			sort(option[i][j].begin(), option[i][j].end());
			option[i][j].resize( unique(option[i][j].begin(),option[i][j].end()) - option[i][j].begin() );
			assert(option[i][j].size() <= 2);
		}

		bool flg = work();
		printf("Case #%d: %s\n",tt,flg?"POSSIBLE":"IMPOSSIBLE");
		if(flg)
		{
			rebuild_answer();
			REP(i,1,n)
			{
				REP(j,1,m)
				{
					if(mp[i][j]!='-' && mp[i][j]!='|')
						putchar(mp[i][j]);
					else
					{
						int x = newid[i][j];
						if(ans[x]) putchar('-');
						else putchar('|');
					}
				}
				puts("");
			}
		}
	}
	return 0;
}

