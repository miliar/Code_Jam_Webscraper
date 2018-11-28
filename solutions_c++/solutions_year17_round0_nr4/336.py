#include <cstdlib>
#include <cstdio>
#include <iostream>
#include <cmath>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <cstring>

using namespace std;

typedef long long LL;
typedef unsigned long long ULL;

#define SIZE(x) (int((x).size()))
#define rep(i,l,r) for (int i=(l); i<=(r); i++)
#define repd(i,r,l) for (int i=(r); i>=(l); i--)
#define rept(i,c) for (__typeof((c).begin()) i=(c).begin(); i!=(c).end(); i++)

#ifndef ONLINE_JUDGE
#define debug(x) { cerr<<#x<<" = "<<(x)<<endl; }
#else
#define debug(x) {}
#endif

#define maxn 1000
	
struct edge
{
	int id, wg, anti;
	edge() {}
	edge(int id, int wg, int anti): id(id), wg(wg), anti(anti) {}
};

vector<edge> e[maxn];

void add(int x, int y, int z)
{
	e[x].push_back(edge(y,z,e[y].size()));
	e[y].push_back(edge(x,0,e[x].size()-1));
}

int source, sink, flow, augc, found;
int h[maxn], vh[maxn], cur[maxn];

void sap(int m)
{
	if (m==sink)
	{
		found=1; flow+=augc;
		return;
	}
	
	int augc2=augc;
	vector<edge>::iterator it=e[m].begin()+cur[m];
	while (it<e[m].end())
	{
		if (it->wg && h[m]==h[it->id]+1)
		{
			cur[m]=it-e[m].begin();
			augc=min(augc,it->wg);
			sap(it->id);
			if (found) break;
			if (h[source]>=sink) return;
			augc=augc2;
		}
		it++;
	}
	
	if (found)
	{
		it->wg-=augc;
		e[it->id][it->anti].wg+=augc;
	}
	else
	{
		int minh=sink-1, minhi=0;
		rept(it,e[m])
			if (it->wg && h[it->id]<minh)
			{
				minh=h[it->id]; minhi=it-e[m].begin();
			}
		vh[h[m]]--; if (vh[h[m]]==0) h[source]=sink;
		h[m]=minh+1;
		vh[h[m]]++;
		cur[m]=minhi;
	}
}

void networkflow()
{
	flow=0; memset(h,0,sizeof h); 
	memset(vh,0,sizeof vh); vh[0]=sink;
	memset(cur,0,sizeof cur);
	while (h[source]<sink)
	{
		augc=0x7fffffff; found=0;
		sap(source);
	}
}

int n;
int g[110][110], og[110][110];
int used1[310], used2[310];

pair<int,int> calc(int mask, int x, int y)
{
	if (mask==1) return make_pair(x,y);
	int c1=x+y-1;
	int c2=x-y+n;
	return make_pair(c1,c2);
}

pair<int,int> remap(int mask, int x, int y)
{
	if (mask==1) return make_pair(x,y);
	int sum=x+1;
	int diff=y-n;
	return make_pair((sum+diff)/2, (sum-diff)/2);
}

void solve(int mask)
{
	int sn;
	if (mask==1) sn=n; else sn=n*2-1;
	memset(used1, 0, sizeof used1);
	memset(used2, 0, sizeof used2);
	rep(i,1,n)
		rep(j,1,n)
			if (g[i][j]&mask)
			{
				pair<int,int> r=calc(mask,i,j);
				used1[r.first]=1;
				used2[r.second]=1;
			}
	
	if (mask==1)
	{
		vector<int> lis1, lis2;
		rep(i,1,sn) if (!used1[i]) lis1.push_back(i);
		rep(i,1,sn) if (!used2[i]) lis2.push_back(i);
		int len=min(lis1.size(), lis2.size());
		rep(i,0,len-1)
		{
			pair<int,int> r=remap(mask,lis1[i],lis2[i]);
			g[r.first][r.second]|=mask;
		}
		return;
	}
	
	source=sn*2+1; sink=sn*2+2;
	rep(i,1,sink) e[i].clear();
	rep(i,1,sn) if (!used1[i]) add(source,i,1);
	rep(i,1,sn) if (!used2[i]) add(i+sn,sink,1);
	rep(i,1,n)
		rep(j,1,n)
		{
			pair<int,int> r=calc(mask,i,j);
			add(r.first, sn+r.second, 1);
		}
	
	networkflow();
	
	rep(i,1,sn)
		rept(it,e[i])
			if (it->wg==0 && sn+1<=it->id && it->id<=sn*2)
			{
				int j=it->id-sn;
				pair<int,int> r=remap(mask,i,j);
				g[r.first][r.second]|=mask;
			}
}
				
void lemon()
{
	int m; scanf("%d%d",&n,&m);
	memset(g,0,sizeof g);
	memset(og,0,sizeof og);
	rep(i,1,m)
	{
		char buf[10]; int x,y;
		scanf("%s%d%d",buf,&x,&y);
		if (buf[0]=='o') g[x][y]=3;
		if (buf[0]=='x') g[x][y]=1;
		if (buf[0]=='+') g[x][y]=2;
	}
	memcpy(og,g,sizeof g);
	
	solve(1);
	solve(2);
	
	int cnt=0, score=0;
	rep(i,1,n)
		rep(j,1,n)
		{
			if (g[i][j]!=og[i][j]) cnt++;
			if (g[i][j]) score++;
			if (g[i][j]==3) score++;
		}
	printf("%d %d\n",score,cnt);
	rep(i,1,n)
		rep(j,1,n)
			if (g[i][j]!=og[i][j])
			{
				if (g[i][j]==1) printf("x %d %d\n",i,j);
				if (g[i][j]==2) printf("+ %d %d\n",i,j);
				if (g[i][j]==3) printf("o %d %d\n",i,j);
			}
}

int main()
{
	ios::sync_with_stdio(true);
	#ifndef ONLINE_JUDGE
		freopen("D.in","r",stdin);
	#endif
	int tcase; scanf("%d",&tcase);
	rep(i,1,tcase)
	{
		printf("Case #%d: ",i);
		lemon();
	}
	return 0;
}

