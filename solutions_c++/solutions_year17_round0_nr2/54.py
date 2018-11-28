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
	RF("B-large.in");
	WF("Blout.txt");
	CASET{
		LL n;scanf("%lld",&n);
		vector<int> d;
		LL tp=n;
		while(tp){
			d.PB(tp%10);tp/=10;
		}
		reverse(ALL(d));
		bool inc=1;int fp=0;
		REPP(i,1,SZ(d)){
			inc&=d[i]>=d[i-1];
			if(inc&&(d[i]>d[i-1]))fp=i;
		}
		if(inc)printf("Case #%d: %lld\n",case_n,n);
		else{
			string ans;
			REP(i,fp)ans+='0'+d[i];
			ans+='0'+d[fp]-1;
			REPP(i,fp+1,SZ(d))ans+='9';
			if(ans[0]=='0')ans.erase(ans.begin());
			printf("Case #%d: %s\n",case_n,ans.c_str());
		}
		case_n++;
	}
}
