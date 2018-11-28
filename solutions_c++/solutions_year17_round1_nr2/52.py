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

int q[55][55];
int r[55];
int pt[55];

int main(){
	RF("B-large.in");
	WF("Blout.txt");
	CASET{
		DRII(n,p);
		REP(i,n)RI(r[i]);
		REP(i,n){
			REP(j,p)RI(q[i][j]);
			sort(q[i],q[i]+p);
		}
		MS0(pt);
		int ans=0;
		while(1){
			bool done=0;
			REP(i,n){
				if(pt[i]==p){
					done=1;
					break;
				}
			}
			if(done)break;
			int maxmin=0,minmax=1<<30;
			REP(i,n){
				int uv=(q[i][pt[i]]*100)/(90*r[i]);
				int lv=(q[i][pt[i]]*100+110*r[i]-1)/(110*r[i]);
				maxmin=max(maxmin,lv);
				minmax=min(minmax,uv);
			}
			if(maxmin<=minmax){
				ans++;
				REP(i,n)pt[i]++;
			}
			else{
				REP(i,n){
					int uv=(q[i][pt[i]]*100)/(90*r[i]);
					if(uv==minmax){
						pt[i]++;
					}
				}
			}
			//printf("%d %d\n",maxmin,minmax);
			//REP(i,n)printf("%d ",pt[i]);puts("");
		}
		printf("Case #%d: %d\n",case_n++,ans);
	}
}
