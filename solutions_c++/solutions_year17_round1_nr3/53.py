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

int main(){
	RF("C-small-attempt1.in");
	WF("Csout1.txt");
	CASET{
		DRIII(hd,ad,hk);DRIII(ak,b,d);
		int mina=1000;
		REP(i,101){
			REP(j,101){
				int damage=(b*i+ad)*j;
				if(damage>=hk)mina=min(mina,i+j);
			}
		}
		//printf("MINA%d\n",mina);
		int mint=1000;
		REP(i,101){//number of debuffs
			int cturn=0,chp=hd,cak=ak;
			REP(j,i){
				if(chp<=cak-d){
					chp=hd-cak;cturn++;
				}
				if(chp<=cak-d){
					cturn=1000;break;
				}
				cak=max(0,cak-d);
				chp-=cak;
				cturn++;
			}
			REP(j,mina){
				if((j!=mina-1)&&chp<=cak){
					chp=hd-cak;
					cturn++;
				}
				if((j!=mina-1)&&chp<=cak){
					cturn=1000;break;
				}
				chp-=cak;
				cturn++;
			}
			mint=min(mint,cturn);
		}
		if(mint==1000){printf("Case #%d: IMPOSSIBLE\n",case_n++);continue;}
		printf("Case #%d: %d\n",case_n++,mint);
	}
}
