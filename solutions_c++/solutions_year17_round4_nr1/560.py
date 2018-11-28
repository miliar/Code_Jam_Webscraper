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

int dp[102][102][102][102];
int f[4];

int main(){
	RF("A-large.in");
	WF("Alout.txt");
	CASET{
		DRII(n,p);
		MS0(f);
		REP(i,n){
			DRI(x);
			f[x%p]++;
		}
		REP(i,f[0]+1){
			REP(j,f[1]+1){
				REP(k,f[2]+1){
					REP(l,f[3]+1){
						dp[i][j][k][l]=-1<<30;	
					}
				}
			}
		}
		dp[0][0][0][0]=0;
		REP(i,f[0]+1){
			REP(j,f[1]+1){
				REP(k,f[2]+1){
					REP(l,f[3]+1){
						int csum=(j+k*2+l*3)%p;
						if(i!=f[0])dp[i+1][j][k][l]=max(dp[i+1][j][k][l],dp[i][j][k][l]+(csum==0));
						if(j!=f[1])dp[i][j+1][k][l]=max(dp[i][j+1][k][l],dp[i][j][k][l]+(csum==0));
						if(k!=f[2])dp[i][j][k+1][l]=max(dp[i][j][k+1][l],dp[i][j][k][l]+(csum==0));
						if(l!=f[3])dp[i][j][k][l+1]=max(dp[i][j][k][l+1],dp[i][j][k][l]+(csum==0));
					}
				}
			}
		}
		printf("Case #%d: %d\n",case_n++,dp[f[0]][f[1]][f[2]][f[3]]);
	}
}
