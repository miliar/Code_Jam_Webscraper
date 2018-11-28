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
#define M 30
#define INF 1000000000
void RI(){}
template<typename... T>
void RI( int& head, T&... tail ) {
    scanf("%d",&head);
    RI(tail...);
}
using namespace std;
typedef long long LL;
char in[M][M];
int t,n,m;
int mnx[M],mxx[M],mny[M],mxy[M];
int main()
{
	RI(t);
	REP(tt,1,t)
	{
		RI(n,m);
		REP(i,0,M-1) mnx[i]=mny[i]=INF;
		REP(i,0,M-1) mxx[i]=mxy[i]=-INF;
		REP(i,1,n)scanf("%s",in[i]+1);

		REP(i,1,n)REP(j,1,m)if(in[i][j]!='?')
		{
			int x = in[i][j]-'A';
			mnx[x] = min(mnx[x], i);
			mxx[x] = max(mxx[x], i);
			mny[x] = min(mny[x], j);
			mxy[x] = max(mxy[x], j);
		}

		REP(i,0,M-1) if(mnx[i]!=INF) REP(x,mnx[i],mxx[i]) REP(y,mny[i],mxy[i])
			in[x][y] = 'A'+i;

		FORD(i,n-1,1)REP(j,1,m) if(in[i][j]=='?' && in[i+1][j]!='?')
			in[i][j] = in[i+1][j];
		REP(i,2,n)REP(j,1,m) if(in[i][j]=='?' && in[i-1][j]!='?')
			in[i][j] = in[i-1][j];
		FORD(j,m-1,1)REP(i,1,n) if(in[i][j]=='?' && in[i][j+1]!='?')
			in[i][j] = in[i][j+1];
		REP(j,2,m)REP(i,1,n) if(in[i][j]=='?' && in[i][j-1]!='?')
			in[i][j] = in[i][j-1];

		if(in[1][1]=='?') REP(i,1,n)REP(j,1,m) in[i][j]='A';

		printf("Case #%d:\n",tt);
		REP(i,1,n) printf("%s\n", in[i]+1);
	}
	return 0;
}

