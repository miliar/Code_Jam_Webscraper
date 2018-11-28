#include<bits/stdc++.h>

#define s(a) scanf("%d",&a)
#define ss(a) scanf("%s",a)

#define MP           make_pair
#define PB           push_back
#define REP(i, n)    for(int i = 0; i < n; i++)
#define INC(i, a, b) for(int i = a; i <= b; i++)
#define DEC(i, a, b) for(int i = a; i >= b; i--)
#define CLEAR(a)     memset(a, 0, sizeof a)

using namespace std;

typedef long long          LL;
typedef unsigned long long ULL;
typedef vector<int>        VI;
typedef pair<int, int>     II;
typedef vector<II>         VII;

int d[105][105];
int e[105], s[105];
double ans[105][105];
double solve(){
	int N,Q,t1,t2;
	s(N);s(t1);
	REP(i,N){s(e[i]);s(s[i]);}
	REP(i,N)REP(j,N)s(d[i][j]);
	s(t1);s(t2);
	for(int i=0;i<N;i++)
		ans[i][i] = 0;
	for(int v1=N-1;v1>=0;v1--)
	for(int v2=v1+1;v2<N;v2++){
		ans[v1][v2] = -1;
		long long int trav = 0;
		for(int nextStop = v1+1;nextStop<N; nextStop++){
			trav = trav + d[nextStop-1][nextStop];
			if(trav<=e[v1] && ans[nextStop][v2]!=-1){
				if(ans[v1][v2] == -1)
					ans[v1][v2] = trav*1.0/s[v1] + ans[nextStop][v2];
				else
					ans[v1][v2] = min(ans[v1][v2], trav*1.0/s[v1] + ans[nextStop][v2]); 
			}
		}
	}
	return ans[0][N-1];
}
int main()
{
	int t;
	s(t);
	REP(tt,t){
		printf("Case #%d: %.15lf\n",tt+1,solve());
	}
    return 0;
}
