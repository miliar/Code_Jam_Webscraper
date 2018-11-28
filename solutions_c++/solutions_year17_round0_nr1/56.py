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
	RF("A-large.in");
	WF("Alout.txt");
	CASET{
		string s;int n,k;cin>>s>>k;
		n=SZ(s);
		bitset<1500> b;
		REP(i,n){
			b[i]=(s[i]=='+');
		}
		int ans=0;
		deque<int> f;
		REP(i,n){
			while(SZ(f)&&f.front()<i)f.pop_front();
			if(SZ(f)%2)b.flip(i);
			if(b[i])continue;
			if(i+k>n)continue;
			ans++;
			b.flip(i);f.push_back(i+k-1);
		}
		REP(i,n){
			if(!b[i])ans=-1;
		}
		if(ans==-1)printf("Case #%d: IMPOSSIBLE\n",case_n);
		else printf("Case #%d: %d\n",case_n,ans);
		case_n++;
	}
}
