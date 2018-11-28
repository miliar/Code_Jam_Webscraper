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
int t,n,m,ans;
int g[M],in[M][M];
pair<int,int> rng[M][M];
////
int pos[M];
set<pair<int,int>> s[M];
////

int main()
{
	RI(t);
	REP(tt,1,t)
	{
		ans = 0;
		RI(n,m);
		REP(i,1,n)RI(g[i]);
		REP(i,1,n)REP(j,1,m) RI(in[i][j]);
		REP(i,1,n) sort(in[i]+1, in[i]+m+1);
		REP(i,1,n)REP(j,1,m)
		{
			int mn = ceil(in[i][j] / 1.1 / g[i]);
			int mx = floor(in[i][j] / 0.9 / g[i]);
			rng[i][j] = MP(mn,mx);
		}

		////////////
		REP(i,1,n) pos[i]=1;
		REP(i,1,n) s[i].clear();

		REP(pack,1,1000000)
		{
			//pop
			REP(i,1,n)
			{
				while(s[i].size() && pack > (*s[i].begin()).F)
					s[i].erase(s[i].begin());
			}

			//push
			REP(i,1,n)
			{
				while(pos[i]<=m && rng[i][pos[i]].F<=pack)
				{
					if(rng[i][pos[i]].F <= rng[i][pos[i]].S)
						s[i].insert( MP(rng[i][pos[i]].S, pos[i]) );
					pos[i]++;
				}
			}

			//check
			int cnt=2000000000;
			REP(i,1,n) cnt=min(cnt, (int)s[i].size());

			//add
			REP(ii,1,cnt)
			{
				ans++;
				REP(i,1,n) s[i].erase(s[i].begin());
			}
		}

		printf("Case #%d: %d\n",tt,ans);
	}
	return 0;
}


