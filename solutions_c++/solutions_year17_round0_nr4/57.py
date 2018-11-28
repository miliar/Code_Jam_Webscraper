#include <bits/stdc++.h>
#define SZ(X) ((int)(X).size())
#define ALL(X) (X).begin(), (X).end()
#define REP(I, N) for (int I = 0; I < (N); ++I)
#define REPP(I, A, B) for (int I = (A); I < (B); ++I)
#define RI(X) scanf("%d", &(X))
#define RII(X, Y) scanf("%d%d", &(X), &(Y))
#define RIII(X, Y, Z) scanf("%d%d%d", &(X), &(Y), &(Z))
#define DRI(X) int (X); scanf("%d", &X)
#define DRII(X, Y) int X, Y; scanf("%d%d", &X, &Y)
#define DRIII(X, Y, Z) int X, Y, Z; scanf("%d%d%d", &X, &Y, &Z)
#define RS(X) scanf("%s", (X))
#define CASET int ___T, case_n = 1; scanf("%d ", &___T); while (___T-- > 0)
#define MP make_pair
#define PB push_back
#define MS0(X) memset((X), 0, sizeof((X)))
#define MS1(X) memset((X), -1, sizeof((X)))
#define LEN(X) strlen(X)
#define F first
#define S second
#define RF(x) freopen(x,"r",stdin)
#define WF(x) freopen(x,"w",stdout)
typedef long long LL;
using namespace std;
typedef pair<LL,LL> PLL;
typedef pair<int,int> PII;
const LL MOD = (LL)1e9+7;
const int SIZE = 2e5+5;
const LL INF = 1LL<<60;
const double eps = 1e-4;
const double PI=3.1415926535897932;

int l[309],vis[309];
vector<int> adj[309];
char d[109][109];
char ans[109][109];
bool fd[309],fr[309];

int aug(int x){
	if(fr[x]||fd[x])return 0;
	if(vis[x])return 0;
	vis[x]=1;
	for(int i:adj[x]){
		if(l[i]==-1||aug(l[i])){
			l[i]=x;return 1;
		}
	}
	return 0;
}

int main(){
	RF("D-large.in");
	WF("Dlout.txt");
	CASET{
		DRII(n,m);
		MS0(fd);MS0(fr);MS1(l);
		int mcbm=0;
		REP(i,n)REP(j,n)ans[i][j]='.',d[i][j]='.';
		REP(i,m){
			char c;scanf(" %c",&c);
			DRII(a,b);a--;b--;
			d[a][b]=c;
			if(c=='x'||c=='o'){
				adj[a].PB(b);
				l[b]=a;mcbm++;
				fr[a]=1;
			}
			if(c=='+'||c=='o'){
				adj[n+a+b].PB(n+n+a-b);
				l[n+n+a-b]=n+a+b;mcbm++;
				fd[n+a+b]=1;
			}
		}
		REP(i,n){
			if(fr[i]==0){
				REP(j,n)adj[i].PB(j);
			}
		}
		REP(i,n){
			REP(j,n){
				if(fd[n+i+j])continue;
				adj[n+i+j].PB(n+n+i-j);
			}
		}
		REP(i,3*n){
			MS0(vis);
			mcbm+=aug(i);
		}
		REP(i,n){
			if(l[i]!=-1){
				ans[l[i]][i]='x';
			}
		}
		REP(i,2*n){
			if(l[i+n]!=-1){//x-y+n=i,x+y+n=j;
				int j=l[i+n];
				//printf("DM%d %d",i,j);
				if(ans[(i+j)/2-n][(j-i)/2]=='.')ans[(i+j)/2-n][(j-i)/2]='+';
				else ans[(i+j)/2-n][(j-i)/2]='o';
			}
		}
		vector<pair<char,PII> >v;
		REP(i,n){
			REP(j,n){
				if(ans[i][j]!=d[i][j]){
					v.PB(MP(ans[i][j],MP(i+1,j+1)));
				}
			}
		}
		REP(i,3*n){
			adj[i].clear();
		}
		printf("Case #%d: %d %d\n",case_n++,mcbm,SZ(v));
		for(auto i:v){
			printf("%c %d %d\n",i.F,i.S.F,i.S.S);
		}
	}
}
