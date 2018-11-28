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
#define RF(X) freopen(X,"r",stdin)
#define WF(X) freopen(X,"w",stdout)
typedef long long LL;
using namespace std;
typedef pair<LL,LL> PLL;
typedef pair<int,int> PII;
const LL MOD = (LL)1e9+7;
const int MAXN = 1e5+5;
const LL INF = 1LL<<30;
const long double eps = 1e-10;
const double PI=3.1415926535897932;

int rs[1009];
int po[1009];
vector<int> t[1009];

int main(){
	RF("B-large.in");
	WF("Blout.txt");
	CASET{
		DRIII(n,c,m);
		REP(i,1009)t[i].clear();
		MS0(rs);MS0(po);
		int ans=0;
		REP(i,m){
			DRII(x,p);
			t[p].PB(x);
			rs[x]++;po[x]++;
			ans=max(ans,SZ(t[p]));
		}
		REPP(i,1,n+1){
			rs[i]+=rs[i-1];
		}
		REPP(i,1,n+1){
			ans=max(ans,(rs[i]+i-1)/i);
		}
		int ans2=0;
		REPP(i,1,n+1){
			ans2+=max(po[i]-ans,0);
		}
		printf("Case #%d: %d %d\n",case_n++,ans,ans2);
	}
}
